# Fresh proof and finite-certificate audit

STAGE: PROOF-AUDIT — cold-examiner Stage 2, dispatch 4/6.

VERDICT: **VERIFIED for the version 2 theorem and certificate, C1–C11 below.**
C12 is verified as a consequence of the cited external theorem, with its
source statement and substitution checked but its random-tree dependency not
independently reproved. C13 and novelty are outside this audit and remain
unresolved. The universal extension of the same numerical lower bound to
arbitrary positive lengths is **REFUTED**, as correctly reported by Stage S.

CLAIM: For every integer d>=1, the unit-edge diamond D_d is planar, has
treewidth exactly two, and its all-subsets graph Steiner diversity satisfies

    c1(D_d) >= L_d = (6d+7+2/4^d)/9.

All graph vertices are permitted Steiner points, and a single finite-dimensional
coordinate-range L1 embedding must work for every terminal subset. This implies
that P is false and that T is false at k=2. This audit verifies the adopted
version 2 argument itself, not the superseded v1 argument or the initial
examiner's NOT-BROKEN verdict.

## Claim-level disposition

IDs refer to the reviewed snapshot of CLAIMS.md.

| ID / claim | Verdict | Scope and evidence |
|---|---|---|
| C1: finite cut representation and converse | VERIFIED | Threshold gaps in each coordinate; weighted indicators realize the converse. The dual comparison therefore covers every allowed dimension and all subsets. |
| C2: counts, planarity, treewidth two | VERIFIED | Recursive counts, local planar replacement, explicit retained-bag decomposition, and cycle lower bound on treewidth. |
| C3: simultaneous nested-cut inequality | VERIFIED | First split generation q, bridgeless D_q, edge-disjoint descendant gadgets and terminal paths; tail sum is exactly 2^(d-q+1). |
| C4: exact generation-set Steiner costs | VERIFIED | Upper construction from a coarse spanning tree; lower projection of simple paths through gadgets whose interiors are disjoint. |
| C5: rational certificate and L_d | VERIFIED | Nonnegative weights, exact normalization 1, C3 feasibility, C4 costs, and checked geometric-sum algebra, including d=1. |
| C6: P/T refutation | VERIFIED | L_d diverges and the witnesses are unit-length planar graphs of treewidth two. No external theorem or finite LP is needed. |
| C7: all 28 finite exact values | VERIFIED | Fresh exact cost/certificate check of every saved case; all values agree with SMALL_CASES.md and the earlier independent report. |
| C8: positive lengths can give c1=1 | VERIFIED | Replacing each expensive non-tree edge by its cheaper spanning-tree path gives equality of diversities on every subset. |
| C9: rescaling and bounded-ratio comparison | VERIFIED | Common scaling is exact; all-subset inequalities m delta_unit <= delta_ell <= M delta_unit give both comparisons and max(1,L_d/R). |
| C10: unique unit restricted optimum | VERIFIED | Singleton cuts make every tail cap necessary; C3 makes them sufficient; strictly positive summation-by-parts coefficients force every cap tight. |
| C11: weighted restricted optimum (S2) | VERIFIED | Same feasible tails, actual nondecreasing costs, and normalization by the sum of shortest-path edge-pair distances. Uniqueness is not asserted. |
| C12: logarithmic growth order | VERIFIED AS CITED CONSEQUENCE | Theorem 2 states the required all-subsets upper bound; the shortest-path metric substitution is exact. This does not independently verify the underlying random-tree theorem. |
| C13: literature non-finding / originality | INCOMPLETE IN THIS AUDIT | No additional search or audit of the literature log was assigned or performed. Novelty is unresolved. |
| Same L_d for every positive-length assignment | REFUTED | The all-depth tree-equivalent lengths have c1=1; already the cycle with lengths 1,1,1,3 gives 1<3/2. |
| Full optimum c1(D_d)=L_d at arbitrary d | INCOMPLETE / NOT ASSERTED | Verified only at d=1,2. Restricted dual optimality does not imply this equality. |

## EVIDENCE

### The complete universal inference chain

For one coordinate, sorting its finitely many distinct values decomposes the
range on every A into consecutive positive gaps crossed by A. Empty sets and
singletons contribute zero. Summing coordinates gives a finite nonnegative
cut combination; one weighted indicator coordinate realizes each cut. Thus
the cutwise inequality may be integrated against the same weights for all
sets. If beta has Steiner-cost mass 1, then

    alpha.delta <= alpha.h <= beta.h <= D beta.delta = D.

Taking the infimum over all feasible embeddings preserves the lower bound;
attainment of the infimum is unnecessary.

Each replacement creates four edges and two new vertices per old edge. Hence
E_d=4^d and N_d=2+2(4^d-1)/3. A descendant gadget has only its two coarse
endpoints in the coarse vertex set; different gadget interiors and edge sets
are disjoint. Its two parallel branches each comprise two smaller gadgets in
series. Induction gives both terminal distance 2^(d-j) and 2^(d-j)
edge-disjoint terminal paths. D_0, used as a descendant gadget when j=d,
has one edge and one terminal path, so this boundary case is included.

Every edge of D_j, j>=1, belongs to its last-round replacement four-cycle.
Thus D_j is connected and bridgeless. A nontrivial vertex cut cannot have
zero boundary edges by connectivity or exactly one by bridgelessness.

For a nontrivial final cut, let q be the first split generation among
V_1,...,V_d. All later generations split and all earlier ones do not.
The split D_q has at least two boundary edges. Each corresponding descendant
gadget contributes at least 2^(d-q) final boundary edges because the cut must
hit each of its edge-disjoint terminal paths. These contributions are
disjoint across gadgets. The coefficient tail is

    sum_(j=q)^d a_j = 2^(d-q+1),

including q=d and d=1. This proves the simultaneous inequality, not merely
separate estimates later added without justification. A new vertex born at
generation d has degree two and splits only V_d. A generation-q singleton
cut has final degree 2^(d-q+1) and splits exactly V_q,...,V_d, so each tail
bound is sharp. Cuts separating the original endpoints also split V_1;
the argument applies with q=1. There is no missing generation-zero case.

For C4, a tree of D_j and a shortest path in each selected descendant cell
give a connected graph containing V_j with cost 2^(d-j)(N_j-1). Conversely,
take any connected subgraph H containing V_j and any simple H-path between
coarse vertices. Divide the path at every visit to V_j. Each segment has
interior disjoint from V_j, so it stays in one gadget and joins that gadget's
two endpoints. It cannot jump between gadget interiors. The coarse edges
represented by these segments connect every pair of coarse vertices; hence
at least N_j-1 gadgets contain an endpoint connection. Each contributes at
least 2^(d-j) edges, and these edge resources are disjoint. This establishes
the exact formula while allowing all newer vertices as Steiner points.

In the certificate, each final edge pair has diversity 1. There are 4^d
such pairs of beta weight 4^-d, so the normalization is exactly 1. Dividing
the established cut inequality by 4^d gives feasibility. Substituting the
cost formula gives

    (2(d-1))/3 + (1-4^(-(d-1)))/9 + 4/3 + 2/(3*4^d)
    = (6d+7+2/4^d)/9.

The empty sum at d=1 gives 3/2; d=2 has costs 6 and 11 and alpha weights
1/8, giving 17/8. For all d, L_d=(2/3)d+O(1) and tends to infinity.

Local replacement in a thin neighborhood of each embedded edge proves
planarity. For treewidth, attaching {x,y,a} and {x,y,b} to an existing bag
containing x,y preserves the running-intersection property, covers every
new edge, and keeps all bags of size at most three. A retained bag need not
induce a current graph edge. The lower bound follows from the surviving
four-cycles: a graph with width at most one is a forest. To discharge that
elementary fact, prune redundant leaf bags in a width-one decomposition;
a remaining leaf bag has a vertex occurring nowhere else, of degree at
most one. Repeated deletion cannot leave a cycle. Thus the treewidth is
exactly two. These verified class properties and divergence refute P and
the k=2 instance of T; k=1 remains the tree exactness case.

### Strengthening audit

The spanning-tree construction assigns tree edges length 1 and other edges
length N. Each non-tree edge can be replaced by a tree path of length at
most N-1. Replacing all such edges preserves connectivity and terminals,
and shared replacement edges only reduce the resulting union's cost.
Together with the reverse inequality from T being a subgraph, this proves
delta_G,ell(A)=delta_T(A) for every A simultaneously. The usual tree-edge
cut coordinates are a single exact embedding, proving c1=1.

The listed D_2 tree has eleven edges, reaches every one of its twelve
vertices, and its five listed complement edges are exactly the missing
replacement edges. The separate cycle example 1,1,1,3 permits equal-cost
replacement and all its edges realize their endpoint distances. The strict
example 1,1,1,5/2 has every edge strictly shorter than its alternative path;
replacement by the unit path costs at most 6/5 times the original connected
subgraph. Consequently its claimed upper bound 6/5<3/2 is valid without
needing to know its exact optimum.

Multiplying all lengths and all embedding coordinates by r>0 proves exact
scale invariance, with alpha and beta divided by r. For bounded edge ratio,
minimizing the same subgraph costs establishes the comparison on every A.
Dividing a noncontracting ell-embedding by m gives a unit embedding of
distortion at most DR. Multiplying a unit embedding by M proves the reverse
factor-R comparison. Fixed R therefore preserves logarithmic divergence;
it does not preserve the same exact L_d at every depth.

For the restricted method, a vertex born in generation q has degree
b_q=2^(d-q+1). Its singleton cut forces y_q<=b_q. The main cut argument
proves that these caps and x_j>=0 are also sufficient. With x_j=y_j-y_(j+1),
the objective is

    [c_1 y_1 + sum_(j=2)^d (c_j-c_(j-1)) y_j] / E.

The unit cost differences are 2^(d-j)(4^j-1)/3>0, and c_1>0. Setting every
y_q=b_q is feasible because the caps decrease. Every coefficient is
positive, so equality in the objective bound uniquely forces these tails.
This gives exactly the v2 coefficients. For weighted costs the differences
are nonnegative by nesting, so the same tails still maximize the objective,
with no need for uniqueness. Dividing by B_ell=sum_edge delta_ell(edge)
normalizes beta correctly; assigned edge lengths need not be shortest-path
distances. This yields precisely (S2) and its L_d/R consequence.

The additional controls in STRENGTHENING.md also check analytically: d=0
uses tree exactness and has treewidth one; triangle plus pendant edge has
c1=4/3 by the triangle singleton-cut embedding and exact bridge cut; the
square coordinate map has pair isometry but full-set range 2 instead of
Steiner cost 3; D_2's old vertex set costs 6 despite its edgeless induced
graph; and the three-leaf star has leaf-set cost 3 versus terminal-only
metric-tree cost 4. The displayed C4 spanning-path average gives values
3/2,2,5/2,3 on adjacent pairs, opposite pairs, triples, and all vertices.
These checks respect one embedding and arbitrary graph Steiner vertices.

### Finite-certificate workflow

I read small_cases.py and verify_small.py in full. The generation algorithm
computes an induced-subgraph MST for every vertex set B, then the minimum
over B containing A. This equals graph Steiner cost: every connected
subgraph contains a spanning tree on its vertex set, and every such induced
MST is a feasible connected subgraph. Positive integer lengths in these
inputs make the computation exact. The Kruskal implementation and superset
transform implement this identity correctly.

The separate verify_small.py uses shortest-path closure and the usual
terminal-subset tree DP. At a root, combining every proper partition of a
terminal mask and then propagating through shortest paths permits all
vertices as Steiner points. The first-bit condition removes duplicate
partitions without omitting one. The initialization and final minimum over
roots handle singletons and arbitrary terminal trees. Its finite sentinel
and int64 additions are far beyond the costs of these particular inputs;
no overflow occurs in this scope. This is a different cost algorithm, not
the generator's MST procedure rerun under another name.

The LP includes all 2^n-n-1 nonsingleton terminal sets, and one representative
of each of the 2^(n-1)-1 nontrivial cuts, chosen to omit the highest vertex.
Its primal inequalities are delta<=h<=D delta. The saved nonnegative dual
measures have cutwise alpha<=beta and beta-cost mass at most 1, which suffices
for weak duality. All twenty-eight saved normalizations in fact equal 1.
Fraction reconstruction is only a candidate-generation step: the exact
integer/Fraction checks, not floating-point solver status, certify it.
The generator's integer-vector overflow guard is safe for its hit sums;
the independent verifier uses Python integers for those sums.

The upper-edge reduction is exact. For any cut sum h and Steiner tree T
spanning A, every cut hitting A crosses T, so h(A)<=sum_(e in T) h(e).
Edge-pair upper constraints therefore imply

    h(A) <= D sum_(e in T) delta_G(e)
         <= D sum_(e in T) ell(e) = D delta_G(A).

The reduced solver actually uses shortest-path edge-pair costs, which only
strengthens the intermediate assigned-length inequality. All subset lower
constraints remain. The final certificates were checked against every
original subset upper constraint. The three preserved initial full-LP
files have status 1 and null objective; they are correctly not treated as
certificates.

Fresh evidence is in assignments/proof-audit-check.py and
assignments/proof-audit-check.json. The checker imports no owner module and
invokes no LP solver. It reconstructs the cycle, complete graph, path, star,
fan, wheel, grid, diamond, and seeded weighted 2-tree instances; checks the
raw 2-tree predecessor-edge invariant; computes every cost using a new
Prim implementation plus superset minima; checks every saved primal and
dual with unbounded integers and Fractions; and checks exact matching
objectives and normalization. The Prim calculation independently implements
the MST identity, not a third distinct mathematical characterization. The
owner's separate DP supplies that algorithmic distinction and was audited
above. Every raw cost entry and every one of the 28 optima passed.

The new checker also verifies the v2 d=2 cut inequality on all 2047 cuts.
For C4, three deliberate in-memory corruptions are rejected: increasing a
dual-lower coefficient fails at cut mask 1; reducing the claimed distortion
to 1 fails the upper inequality at terminal mask 3; deleting all primal
weights fails the lower inequality at terminal mask 3. Owner files remain
unchanged.

Tree exactness and the formulas c1(C_n)=c1(K_n)=2(n-1)/n, n>=3, were also
checked analytically from KILLS.md. For K_n the singleton weights give all
subset lower bounds and the maximum ratio on pairs; summing pair upper
bounds supplies the matching lower bound. For C_n, averaging spanning paths
dominates every subset and the edge reduction gives the upper bound;
every nontrivial cycle cut crosses at least two edges, giving the matching
lower bound from the full set. These arguments do not extrapolate a finite
table.

### External upper comparison

The supplied Bryant–Tupper source, sources/bryant-tupper-open.txt, Theorem 2
in section 2.2, explicitly states an O(log n) L1 embedding for the Steiner
diversity of an n-point metric space. Its displayed proof compares all
finite A simultaneously through expected tree diversities. An expectation
on finite X can be grouped into finitely many nonnegative cut weights,
so it fits the finite-dimensional target convention here.

Completing the graph on V with shortest-path distances preserves Steiner
diversity: replace metric-tree edges by graph shortest paths, delete any
cycles from the union, and obtain graph cost no larger; conversely, view
a graph Steiner tree as a metric-edge tree with cost no larger. Taking
minima proves equality. Both directions permit all V as Steiner points.
Together with the verified lower bound, this supplies the claimed growth
order for unit lengths and uniformly bounded R.

The source has imprecise wording that its Steiner tree's "leaves include"
A; taken literally with vertex set contained in X, that is impossible for
A=X and |X|>2. The operative proof uses a tree connecting A, which is the
standard Steiner convention used in this audit. The source also phrases
its random-tree premise as a bijection to a tree with vertex set X. I did
not independently rederive or audit that random-tree representation or its
underlying cited theorem. Accordingly this is a source/substitution check
of the stated Theorem 2, not a new proof of that external result. Neither
wording issue is a dependency of C1–C11 or the P/T refutation.

## COVERAGE

All load-bearing steps of PROOF.md v2 and CERTIFICATE.md v2, all mathematical
strengthening claims, all 28 exact finite entries, and the requested
external theorem statement/substitution were covered. The finite checks
remain at n<=12 and are controls, not universal premises.

KILLS.md was read in full. Its tree/cycle/complete controls, cut representation,
pair-cost identity, and upper-edge reduction are verified here. Its source
interpretation of the two #089 papers and its affine-incidence discussion
were not independently audited against their original sources; these
noncentral claims are not needed for any C1–C12 conclusion. No novelty
claim, full optimal c1 formula for d>=3, superseded v1 proof, privacy audit
of unrelated repository content, or publication-readiness claim is covered.
Saved performance estimates and solver memory accounting were not replayed.

## DEPENDENCIES

C1–C6 and C8–C11 are elementary checked arguments with the required graph
and cut facts discharged above. C7 additionally uses the exact saved inputs
and rational certificates, the inspected algorithms, and the fresh checker.
C12 relies on the stated Bryant–Tupper Theorem 2 as an external cited result.
C13 remains outside scope. The complete main proof does not depend on C7,
C12, an absence of prior art, a hypergraph result, or a pairs-only embedding.

## ERRATA

No correctness repair is required for the v2 theorem or the audited Stage S
arguments. Keep the distinction between the restricted optimum and the full
optimal distortion. Keep the arbitrary-length counterexample alongside the
bounded-ratio result. If quoting the external source's definition, explain
the ordinary "tree connecting A" convention rather than repeating its
literal leaves wording. Tree exactness here concerns trees with at least
two vertices; c1 on a one-vertex graph needs a convention for the maximum
over an empty set, which is irrelevant to all diamond claims.

## EXPOSURE

I read the dispatch and assignment first, then the installed cold-examiner
skill, PROOF.md v2, CERTIFICATE.md v2, STRENGTHENING.md, BRIEF.md, KILLS.md,
SMALL_CASES.md, the full two computational scripts, the Bryant–Tupper source
through line 180, the prior independent report, environment_check.py,
run_job.py, and the prior verification job record. The raw D2 JSON was first
displayed in part and then completely processed by the fresh checker. All
28 current raw case files and top-level result JSON metadata were read by
that checker. I then read the sealed initial report in full, followed by
CLAIMS.md and the three preserved failed full-LP records. The sealed report
was read only after the proposed argument and finite workflow had been
examined. Its earlier NOT-BROKEN verdict was never used as proof evidence.

The parent's follow-up identified the new claim registry and clarified that
the external upper bound was supplemental. I reported progress and the fresh
check results to the parent. No other agent was spawned. No owner proof,
certificate, result, or sealed report was changed.

Reviewed hashes are recorded completely in
assignments/proof-audit-reviewed.sha256, whose SHA-256 is
521360d4a98731c1d470ea650007b80b9a3cd2eeee34588326da7e6e0139abcb.
The record distinguishes file identity from coverage: the source file is
hashed in full although only its first 180 lines were inspected, and size
metadata was read without auditing every resource estimate.

Key reviewed SHA-256 values:

- PROOF.md: 80c16dd8331c95cbad94bbe094badfe6a67e84f72f2254c4dfb05f0b4d80a381
- CERTIFICATE.md: 098c338918659d1d1aae377aa0fd7366ae03c3cc227f7534f341dc0e928f284c
- STRENGTHENING.md: d92ad1fdef28e722e3bfd11b80a2cf314e903f60da2daf80ab8e74a74fdac44c
- Sealed initial report: d3f9fd57029ad1d1a420e0020bce35655369eba404d7f456959f772be3d37f57
- Fresh checker: 3297d8edf1703cedc10cf841ce9a2df2bd09a2a615962d7e3f14d95494ac0de2
- Fresh output: 385faf13b042c5f85d133bea0653471554e84e5a31e8aab1cbf1b0d5fc1c73d4

## RESOURCES

Allocation: at most 300 local CPU seconds and 25 minutes procedural wall,
dispatch 4/6, no nested agents. Only the named script
assignments/proof-audit-check.py ran as a Python workload, explicitly with
/Users/klinellc/.venvs/claude/bin/python. It asserted sys.prefix !=
sys.base_prefix and recorded executable/prefix/base_prefix. It imports only
the standard library and installs nothing. No owner script or LP was rerun.

Before enumeration it printed these total sizes: 28 instances, maximum 12
vertices, 21,992 induced vertex subsets, 21,964 nonempty terminal masks,
10,968 unoriented nontrivial cuts, at most 7,139,344 Prim neighbor scans,
474,717 primal hit tests, and 157,592 dual hit tests. The additional d=2
inequality check covers 2047 cuts. Its stated estimate was 30 wall seconds
and 32 MiB; an RLIMIT_CPU ceiling of 90 seconds was installed.

The single successful run (PID 14770) recorded 0.549096 CPU seconds,
0.563912 wall seconds, and 11,390,976 bytes peak RSS. The tool returned
exit code 0. A subsequent ps query found no such PID. No kill or outstanding
job remains. Read/write shell and tool overhead was not separately CPU
instrumented; the computational workload is far below the allocation.

The first explicit UTC clock measurement during review was 13:53:26 on
2026-10-25; the assignment's UTC creation time was 13:47:12, which predates
dispatch and can supply a conservative procedural upper bound. Completion
time is recorded with the final report hash in the companion receipt.
All four substantive new artifacts are in the assigned quarantine: this
report, the prefixed checker, its output, and the prefixed hash manifest.
No email, other external contact, external service mutation, installation,
public-repository operation, publication, or literature search occurred.
