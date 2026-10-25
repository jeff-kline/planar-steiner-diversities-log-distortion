"""Exact finite verification; standard library only, no LP solver."""
from fractions import Fraction as F
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
from draft_inventory import inventory

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "path8": "1", "star8": "1",
    "K3": "4/3", "K4": "3/2", "K5": "8/5", "K6": "5/3", "K8": "7/4",
    "C4": "3/2", "C5": "8/5", "C6": "5/3", "C7": "12/7", "C8": "7/4",
    "C10": "9/5", "C12": "11/6", "diamond2": "17/8",
    "fan5": "8/5", "fan8": "7/4", "wheel5": "5/3", "wheel8": "38/21",
    "grid2x3": "5/3", "grid2x4": "7/4", "grid2x5": "9/5",
    "grid2x6": "11/6", "grid3x3": "11/6", "grid3x4": "29/15",
    "random2tree8-seed17": "4/3", "random2tree8-seed31": "14/11",
    "random2tree8-seed53": "26/19",
}


def hits(terminal, cut):
    inside = terminal & cut
    return inside != 0 and inside != terminal


def diamond(depth):
    edges, n, generations = [(0, 1, 1)], 2, [3]
    for _ in range(depth):
        new_edges = []
        for u, v, _ in edges:
            for _ in range(2):
                new_edges.extend([(u, n, 1), (n, v, 1)])
                n += 1
        edges = new_edges
        generations.append((1 << n) - 1)
    return n, edges, generations


def steiner_costs(n, edges):
    """MST of each induced vertex set, then minimize over supersets.

    Every connected subgraph contains a spanning tree on its vertex set.
    Conversely each induced-subgraph MST is a feasible connector. Prim's
    algorithm and the superset transform use only integer arithmetic.
    """
    adjacency = [[] for _ in range(n)]
    for u, v, weight in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        assert isinstance(weight, int) and weight > 0
        adjacency[u].append((v, weight))
        adjacency[v].append((u, weight))
    infinity = sum(w for _, _, w in edges) + 1
    costs = [infinity] * (1 << n)
    costs[0] = 0
    for mask in range(1, 1 << n):
        tree = mask & -mask
        cost = 0
        while tree != mask:
            choices = [(w, v) for u in range(n) if tree & (1 << u)
                       for v, w in adjacency[u]
                       if mask & (1 << v) and not tree & (1 << v)]
            if not choices:
                break
            weight, v = min(choices)
            tree |= 1 << v
            cost += weight
        if tree == mask:
            costs[mask] = cost
    for v in range(n):
        bit = 1 << v
        for mask in range(1 << n):
            if not mask & bit:
                costs[mask] = min(costs[mask], costs[mask | bit])
    assert max(costs) < infinity, "Disconnected input"
    return costs


def lower_bound(depth):
    return F(6 * depth + 7, 9) + F(2, 9 * 4**depth)


def scale(values):
    rationals = {int(k): F(v) for k, v in values.items()}
    denominator = 1
    for value in rationals.values():
        denominator = denominator * value.denominator // math.gcd(
            denominator, value.denominator)
    return rationals, denominator, {
        k: int(v * denominator) for k, v in rationals.items()}


def verify_certificate(record, costs):
    n, full = record["n"], (1 << record["n"]) - 1
    distortion = F(record["rational_candidate"])
    weights, denominator, integer_weights = scale(record["weights"])
    assert distortion >= 1 and all(v >= 0 for v in weights.values())
    assert all(0 < s < 1 << (n - 1) for s in weights)
    ratios = []
    for terminal in range(1, full + 1):
        value = sum(w for s, w in integer_weights.items() if hits(terminal, s))
        assert value >= denominator * costs[terminal], ("primal lower", terminal)
        assert value * distortion.denominator <= (
            denominator * costs[terminal] * distortion.numerator
        ), ("primal upper", terminal)
        if costs[terminal]:
            ratios.append(F(value, denominator * costs[terminal]))
    alpha = {int(k): F(v) for k, v in record["dual_lower"].items()}
    beta = {int(k): F(v) for k, v in record["dual_upper"].items()}
    assert all(0 < a <= full and a & (a - 1) for a in [*alpha, *beta])
    assert all(v >= 0 for v in [*alpha.values(), *beta.values()])
    difference = dict(alpha)
    for terminal, weight in beta.items():
        difference[terminal] = difference.get(terminal, F(0)) - weight
    _, _, integers = scale({str(k): str(v) for k, v in difference.items()})
    for cut in range(1, 1 << (n - 1)):
        assert sum(w for a, w in integers.items() if hits(a, cut)) <= 0, (
            "dual cut", cut)
    normalization = sum(w * costs[a] for a, w in beta.items())
    objective = sum(w * costs[a] for a, w in alpha.items())
    assert normalization == 1
    assert objective == distortion == max(ratios)
    return str(distortion)


def check_diamonds():
    results = []
    for depth in (1, 2):
        n, edges, generations = diamond(depth)
        print("SIZE diamond d={}: vertices={}, induced subsets={}, cuts={} "
              "(including empty representative)".format(
                  depth, n, 1 << n, 1 << (n - 1)), flush=True)
        assert n == (2 * 4**depth + 4) // 3 and len(edges) == 4**depth
        coefficients = {j: 2**(depth-j) if j < depth else 2
                        for j in range(1, depth+1)}
        for cut in range(1 << (n-1)):
            boundary = sum(bool(cut & (1 << u)) != bool(cut & (1 << v))
                           for u, v, _ in edges)
            demand = sum(a * hits(generations[j], cut)
                         for j, a in coefficients.items())
            assert demand <= boundary, (depth, cut)
        costs = steiner_costs(n, edges)
        generation_costs = []
        for j in range(1, depth+1):
            exact = costs[generations[j]]
            predicted = 2**(depth-j) * ((2*4**j+4)//3 - 1)
            assert exact == predicted
            generation_costs.append(exact)
        objective = sum(F(a * costs[generations[j]], 4**depth)
                        for j, a in coefficients.items())
        assert objective == lower_bound(depth)
        results.append({"depth": depth, "vertices": n,
                        "cut_representatives": 1 << (n-1),
                        "generation_costs": generation_costs,
                        "objective": str(objective)})
        print("PASS diamond d={}: all cuts, exact costs {}, objective={}".format(
            depth, generation_costs, objective), flush=True)
    for depth in range(1, 13):
        objective = sum(
            F(2**(depth-j) * 2**(depth-j) * ((2*4**j+4)//3-1), 4**depth)
            for j in range(1, depth))
        objective += F(2 * ((2*4**depth+4)//3-1), 4**depth)
        assert objective == lower_bound(depth)
    print("PASS objective identity: d=1..12 (exact Fraction arithmetic)")
    return results


def check_integrity():
    """Check a present draft manifest; the initial bootstrap may omit it."""
    manifest = ROOT / "MANIFEST.sha256"
    if not manifest.exists():
        print("INFO manifest absent during draft bootstrap")
        return 0
    count = 0
    listed = set()
    current_files = set(inventory())
    for line in manifest.read_text().splitlines():
        expected, name = line.split("  ", 1)
        assert name not in listed, ("duplicate manifest path", name)
        assert name in current_files, ("unexpected manifest path", name)
        listed.add(name)
        path = ROOT / name
        assert path.is_file(), name
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
        count += 1
    assert listed == current_files, ("manifest inventory mismatch",
                                     current_files ^ listed)
    print("PASS draft manifest: {} files".format(count))
    return count


def main():
    assert sys.prefix != sys.base_prefix, "Use the explicitly selected virtual environment"
    assert not sys.flags.optimize, "Assertions must be enabled"
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, default=ROOT / "build/verify.json")
    args = parser.parse_args()
    start_cpu, start_wall = time.process_time(), time.monotonic()
    records = []
    for path in sorted((ROOT / "data").glob("*.json")):
        record = json.loads(path.read_text())
        if "name" in record:
            records.append((path, record))
    assert {r["name"] for _, r in records} == set(EXPECTED)
    assert len(records) == 28 and all(r["n"] <= 12 for _, r in records)
    print("SIZE saved certificates: 28 instances; {} induced subsets; {} "
          "cut representatives; {} nonempty terminal sets; <=32 MiB, "
          "<30 seconds expected.".format(
              sum(1 << r["n"] for _, r in records),
              sum((1 << (r["n"]-1))-1 for _, r in records),
              sum((1 << r["n"])-1 for _, r in records)), flush=True)
    diamond_results = check_diamonds()
    results = []
    for path, record in records:
        assert record["status"] == 0 and record["exact_certified"]
        costs = steiner_costs(record["n"], record["edges"])
        assert costs == record["steiner_costs"], record["name"]
        value = verify_certificate(record, costs)
        assert value == EXPECTED[record["name"]]
        results.append({"name": record["name"], "exact_c1": value,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        print("PASS {}: c1={}".format(record["name"], value), flush=True)
    integrity_count = check_integrity()
    report = {"pid": os.getpid(), "python": sys.executable, "prefix": sys.prefix,
              "base_prefix": sys.base_prefix, "diamonds": diamond_results,
              "algebra_depths": list(range(1, 13)), "certificates": results,
              "manifest_files": integrity_count,
              "cpu_seconds": time.process_time()-start_cpu,
              "wall_seconds": time.monotonic()-start_wall}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2)+"\n")
    print("PASS: 2 diamond constructions; 12 exact objective identities; "
          "28 rational primal/dual certificates; no LP solves.")
    print("CPU {:.6f}s; wall {:.6f}s".format(
        report["cpu_seconds"], report["wall_seconds"]))


if __name__ == "__main__":
    main()
