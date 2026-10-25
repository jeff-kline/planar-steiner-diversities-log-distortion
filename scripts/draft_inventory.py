"""Explicit local draft inventory and unchanged source-copy checks; no release actions."""
import argparse
import hashlib
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "quarantine/steiner-diversity-tw-2026-10-25"
EVIDENCE = {
    "PROOF.md": "PROOF.md", "CERTIFICATE.md": "CERTIFICATE.md",
    "PROOF-AUDIT.md": "PROOF-AUDIT.md", "ADJUDICATION.md": "ADJUDICATION.md",
    "STRENGTHENING.md": "STRENGTHENING.md", "SMALL_CASES.md": "SMALL_CASES.md",
    "LITERATURE.md": "LITERATURE.md",
    "FLOWCUT-SCAN.md": "searches/flowcut/FLOWCUT-SCAN.md",
    "CITING-SCAN.md": "searches/citing/CITING-SCAN.md",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory():
    names = []
    for directory, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if d not in {".git", "build", "__pycache__"})
        for name in sorted(files):
            path = Path(directory) / name
            if name == ".DS_Store" or name.endswith(".pyc") or path == ROOT / "MANIFEST.sha256":
                continue
            assert not path.is_symlink(), ("unexpected symlink", path)
            names.append(path.relative_to(ROOT).as_posix())
    return sorted(names)


def evidence():
    copied = {}
    rows = []
    for name, source_name in EVIDENCE.items():
        destination = ROOT / "audit/evidence" / name
        assert destination.read_bytes() == (SOURCE / source_name).read_bytes(), name
        sha = digest(destination)
        copied[destination.relative_to(ROOT).as_posix()] = sha
        rows.append(f"| `{name}` | `{sha}` |")
    sources = sorted((SOURCE / "results").glob("*.json"))
    assert len(sources) == 57
    assert {p.name for p in sources} == {p.name for p in (ROOT / "data").glob("*.json")}
    for source in sources:
        destination = ROOT / "data" / source.name
        assert destination.read_bytes() == source.read_bytes(), source.name
        copied[destination.relative_to(ROOT).as_posix()] = digest(destination)
    predecessor = ROOT.parent / "covering-hitting-diversities"
    assert (ROOT / "LICENSE").read_bytes() == (predecessor / "LICENSE").read_bytes()
    (ROOT / "audit/imports.sha256").write_text("".join(
        f"{sha}  {name}\n" for name, sha in sorted(copied.items())))
    document = """# Copied evidence and provenance

Pre-release draft. Not admitted, not peer reviewed.

Source: `~/Documents/hm-ai/quarantine/steiner-diversity-tw-2026-10-25/`.
The source is a read-only non-Git directory, so there is no source commit.
Its original manifest was checked first: 150 entries passed, none failed.
The later flow-cut and citing scan logs are outside that original 150-file
manifest; their individual copied hashes are pinned below.

The seven named research records below came from the source root. The two
scan logs came from `searches/flowcut/FLOWCUT-SCAN.md` and
`searches/citing/CITING-SCAN.md`. All nine are copied byte for byte into
`audit/evidence/`. They retain historical paths, references and scope labels.
References into the larger research directory are not all bundled here.
The requirement to copy raw evidence unchanged retains earlier papers'
historical bibliographic identifiers in those records; none identifies this
draft. Draft metadata and paper title material have no assigned publication
identifier. Raw records will need the coordinator's normal release review.

| Copied record | SHA-256 |
|---|---|
""" + "\n".join(rows) + "\n\n"
    document += f"Original source manifest SHA-256: `{digest(SOURCE / 'MANIFEST.sha256')}`.\n\n"
    document += """All 57 top-level `results/*.json` files are copied unchanged to `data/`:
28 graph/certificate records, 28 saved size estimates, and the earlier
independent-verification summary. The 28 graph records hold the exact edges,
Steiner costs and rational primal/dual weights. Their hashes, along with the
nine evidence records, are in `audit/imports.sha256` (66 entries).
The new verifier recomputes the mathematical finite checks and does not
trust the earlier summary's verdict in place of checking the certificates.

The GPL license was copied with `cp` from the read-only predecessor
`covering-hitting-diversities` at `60d135d`; its bytes match. That predecessor
also supplies the repository organization and clean double-build workflow.
Its metadata, dates and publication status are not inherited by this draft.

Run the following to check imported file bytes locally:

```sh
shasum -a 256 -c audit/imports.sha256
```

For a deliberate recheck against the source directory, the named inventory
script verifies equality before rewriting this evidence index:

```sh
~/.venvs/claude/bin/python scripts/draft_inventory.py --evidence
```

`MANIFEST.sha256` covers every current draft file except itself and ignored
build/cache/Git files. The inventory script updates it only on explicit
`--manifest`; the verifier never rewrites it. This is local integrity
bookkeeping, not a release freeze, admission or archive action.
"""
    (ROOT / "audit/EVIDENCE.md").write_text(document)
    print("PASS source copies: 9 evidence records, 57 JSON files, predecessor LICENSE")


def main():
    assert sys.prefix != sys.base_prefix, "Use the explicitly selected virtual environment"
    assert not sys.flags.optimize
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", action="store_true")
    parser.add_argument("--manifest", action="store_true")
    args = parser.parse_args()
    assert args.evidence or args.manifest, "Choose an explicit operation"
    if args.evidence:
        evidence()
    if args.manifest:
        names = inventory()
        (ROOT / "MANIFEST.sha256").write_text("".join(
            f"{digest(ROOT / name)}  {name}\n" for name in names))
        print(f"WROTE local draft manifest: {len(names)} files")


if __name__ == "__main__":
    main()
