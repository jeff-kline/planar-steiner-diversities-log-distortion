# Stage S: lengths and the exact limit of the generation-set method

Date: 2026-10-25. Role: separate fresh strengthener, dispatch 3/6.

**Verdict on deleting H: NEEDED.** The proposed lower bound for *every*
positive-length assignment on the underlying diamond is false, at every
depth. Common positive rescaling is REMOVABLE. A uniformly bounded ratio of
edge lengths still gives a logarithmically divergent lower bound, with a
factor depending on that ratio. The version 2 objective is optimal for the
specified restricted dual method; this is not an assertion of optimal
embedding distortion at arbitrary depth.

This report supplies arguments for separate adoption/audit. It does not
promote the owner's proof or resolve novelty.

## 1. Exact positive-length counterexample, on all subsets

The following observation applies to any finite connected graph, so in
particular to the underlying graph of every D_d. Choose a spanning tree T.
Give every edge of T length 1 and every other edge length N, where N is the
number of vertices. All lengths are strictly positive. Then

\[
\delta_{G,\ell}(A)=\delta_T(A)\qquad\text{for every }A\subseteq V.
\]

Indeed, T is a subgraph, so the left side is at most the right side. Conversely,
replace every non-tree edge uv of any connected subgraph H containing A by
the unique T-path between u and v. That path has at most N-1 edges and costs
less than the replaced edge. The resulting union is a connected subgraph of
T containing A, whose cost is no greater than the cost of H. Minimizing
gives the reverse inequality. This argument allows all vertices as Steiner
points and establishes one identity simultaneously for all terminal sets.

For each tree edge e, let S_e be one component of T-e. The map with
coordinates f_e(v)=1_{S_e}(v) satisfies

\[
\delta_f(A)=\sum_{e\in E(T)}\chi_{S_e}(A)=\delta_T(A).
\]

Thus the weighted diamond has c1=1, in a single embedding of dimension N-1.
Because L_d>1 for every d>=1, it violates the proposed strengthening.

Small explicit cases:

* **d=1:** label the cycle 0-1-2-3-0 and give its consecutive edges lengths
  1,1,1,3. The edge 3-0 can be replaced, at equal cost, by the path 3-2-1-0.
  Thus its diversity equals that of the unit path 0-1-2-3. An explicit exact
  embedding is f(0)=(0,0,0), f(1)=(1,0,0), f(2)=(1,1,0), f(3)=(1,1,1).
  Its coordinate ranges count precisely the edges of the path hull of A.
  Therefore c1=1<3/2=L_1. Even the long edge has length equal to its graph
  shortest-path distance; the example does not rely on an edge longer than
  that distance.
* **d=2:** start D_1 with old edges 0-2, 2-1, 0-3, 3-1. In D_2 replace
  these, respectively, through new vertex pairs (4,5), (6,7), (8,9), (10,11).
  Thus an old edge uv replaced through (a,b) gives ua,av,ub,bv. Choose
  T with edges
  {0-4,4-2,0-5,2-6,6-1,2-7,0-8,8-3,0-9,3-10,3-11}.
  These 11 edges connect all 12 vertices and form a tree. Give them length 1
  and the other five edges {5-2,7-1,9-3,10-1,11-1} length 12. The preceding
  replacement proof gives c1=1<17/8=L_2.

There is also a strict-shortest-edge d=1 counterexample. Give the cycle
lengths 1,1,1,5/2, and retain the unit three-edge path T. Every edge is now
strictly shorter than the alternative path between its endpoints. Replacing
the fourth edge by its T-path multiplies its cost by 6/5; replacing the other
edges has factor 1. Hence

\[
\delta_G\le\delta_T\le(6/5)\delta_G
\]

on every subset, and the same tree embedding proves c1(G)<=6/5<3/2.
No optimality claim for this last example is needed.

## 2. What consumes uniform lengths; what survives

The cut inequality in PROOF.md Section 3 is purely combinatorial. It survives
every assignment of edge lengths, since its right side counts boundary edges.
The terminal path multiplicity also survives. Uniform lengths enter in:

1. Section 2's numerical terminal distance 2^(d-j).
2. Section 4's numerical generation-set cost
   c_j=2^(d-j)(N_j-1).
3. Section 5's assertion that every final edge pair has diversity 1, and
   consequently the normalization beta(edge)=1/4^d.

For arbitrary lengths, an edge pair has diversity equal to shortest-path
distance, which need not be the assigned edge length. Failure of these
formulas alone would not refute the strengthening; Section 1's exact
all-subset embeddings do refute it.

**Common rescaling.** If all edge lengths are multiplied by r>0, every
Steiner cost is multiplied by r. Multiplying every coordinate of an
embedding by r, and conversely dividing by r, proves c1(r delta)=c1(delta).
The displayed certificate may be scaled by 1/r. Thus the numerical choice
of unit, as opposed to one arbitrary common positive length, is removable.

**Bounded edge-length ratio.** Suppose m<=ell(e)<=M for every final edge and
put R=M/m. Minimizing the same connected-subgraph costs gives, on all sets,

\[
m\delta_{\rm unit}\le\delta_\ell\le M\delta_{\rm unit}.
\]

If delta_ell<=h<=D delta_ell, then h/m is a noncontracting embedding for
delta_unit with distortion at most DR. Taking infima proves

\[
c_1(D_d,\ell)\ge\frac{c_1(D_d,1)}R
\ge\frac{L_d}R,
\qquad
c_1(D_d,\ell)\ge\max\{1,L_d/R\}.
\]

The reverse comparison c1(D_d,ell)<=R c1(D_d,1) follows by multiplying a
unit-diversity embedding by M. For a fixed R, the displayed lower bound
still diverges as a positive constant times log N_d. The arbitrary-length
tree-equivalent construction has ratio N_d in its general form, so it does
not contradict this statement. A fixed ratio bound does not restore the
*same exact* L_d bound in general: the d=1 counterexample with ratio 3
already disproves that assertion.

## 3. Exact optimum of the restricted dual method

First use unit lengths. Fix beta(edge)=1/E, where E=4^d, and require that
alpha is nonnegative and supported on V_1,...,V_d. Write
x_j=E alpha(V_j). Define

\[
b_q=2^{d-q+1}\quad(1\le q\le d),\qquad
y_q=\sum_{j=q}^d x_j.
\]

**The all-cut feasible region is exactly**

\[
x_j\ge0,\qquad y_q\le b_q\quad(1\le q\le d). \tag{S1}
\]

For necessity, take a vertex v born in generation q. Its degree is 2 at
birth and doubles in every later replacement, so its degree in D_d is
b_q. The singleton cut S={v} crosses V_j exactly when j>=q. Its dual
constraint is therefore y_q<=b_q. Such a vertex exists for every q.

For sufficiency, let q be the first generation for which a given nontrivial
cut crosses V_q. The nested-set indicators are exactly those for j>=q.
The Section 3 argument gives boundary size at least b_q, so (S1) implies
the constraint for that cut. Trivial cuts have both sides zero. Thus there
are no hidden stronger cut constraints within this restricted support.

Let c_j=delta(V_j). For unit diamonds, the Section 4 formula gives

\[
c_j=\frac{2^{d-j}(2\cdot4^j+1)}3,
\qquad
c_j-c_{j-1}=\frac{2^{d-j}(4^j-1)}3>0\quad(j\ge2).
\]

Summation by parts gives the objective

\[
\frac1E\sum_{j=1}^d c_jx_j
=\frac1E\left(c_1y_1+
 \sum_{j=2}^d(c_j-c_{j-1})y_j\right).
\]

Every coefficient on the right is positive. Consequently its maximum over
(S1) is attained by y_q=b_q for all q. These simultaneous equalities are
feasible, because b_q is decreasing, and they give uniquely

\[
x_j=b_j-b_{j+1}=2^{d-j}\ (j<d),\qquad x_d=b_d=2.
\]

These are precisely version 2's coefficients. Its already displayed
objective evaluation is therefore the exact restricted optimum L_d.
Uniqueness here concerns the alpha coefficients with this fixed beta and
these d support sets, not a full dual optimum or an embedding.

Small cases verify the endpoints without enumeration:

| Depth | Costs (c_j) | Tail caps (b_q) | Optimal (x_j) | Objective |
|---|---|---|---|---|
| 1 | (3) | (2) | (2) | 6/4=3/2 |
| 2 | (6,11) | (4,2) | (2,2) | 34/16=17/8 |

At d=2 the first tail cap is witnessed by a generation-1 vertex of final
degree 4, and the second by a generation-2 vertex of degree 2. These witnesses
also check simultaneous satisfiability of the sharp constraints.

**Weighted extension of the method limit.** For arbitrary positive lengths,
write

\[
B_\ell=\sum_{uv\in E(D_d)}\delta_\ell(\{u,v\}),
\qquad \beta(uv)=1/B_\ell.
\]

This is the normalized uniform beta; using the sum of assigned edge lengths
instead can give a different normalization. Set x_j=B_ell alpha(V_j).
The same feasible region (S1) holds because it only counts graph edges.
The actual costs c_j=delta_ell(V_j) are nondecreasing by nesting. The same
summation-by-parts argument, now with nonnegative differences, proves that
x_j=2^(d-j) for j<d and x_d=2 is still an optimizer. The exact restricted
optimum is therefore

\[
\frac{\sum_{j=1}^{d-1}2^{d-j}\delta_\ell(V_j)
      +2\delta_\ell(V_d)}{B_\ell}. \tag{S2}
\]

Uniqueness need not survive equal successive costs. Since c_j>=m times its
unit cost and B_ell<=ME, (S2) also recovers L_d/R. Formula (S2), rather than
the unit numerical value L_d, is the surviving arbitrary-length result.

## 4. Other hypotheses and controls

* **Depth d>=1:** the lower-bound formula extends to d=0: D_0 is one edge,
  c1=1, and L_0=1. The generation-set certificate is empty at d=0 and must
  be replaced by tree exactness. The claim of treewidth exactly two does
  not extend to d=0; that treewidth is one. Integer depth is a construction
  domain, not an additional analytic restriction.
* **Diamond recursion and generation geometry:** these supply the boundary
  caps, gadget interfaces, and exact costs. Planarity and treewidth two
  alone do not supply the numerical bound. A four-vertex triangle with a
  pendant edge is planar with treewidth two, but has c1=4/3<3/2. To check
  this, the unit triangle has delta(A)=|A|-1 and the sum of its three
  singleton cut diversities, each weighted 2/3, has distortion 4/3.
  For the matching lower bound take beta=1/3 on its three edges and
  alpha(V)=2/3; every nontrivial cut crosses two edges. Adding the pendant
  edge adds its exact bridge cut to the projected triangle diversity, so
  the same upper distortion holds; restricting to the triangle gives the
  lower bound. This is an all-subsets control, not a metric substitute.
* **One embedding for all subsets:** this is indispensable. The unit C4
  shortest-path metric embeds isometrically as the corners of the unit
  square in R^2 with L1 distance, but its full-set coordinate-range value
  is 2 while its Steiner cost is 3. Thus pairs-only distortion is 1, below
  the claimed diversity lower bound. If the embedding could be chosen
  separately for each set A, one coordinate with range delta(A) would
  attain distortion 1 on that set; the dual summation would no longer
  compare values of a single cut combination.
* **Arbitrary graph vertices as Steiner points:** retained throughout this
  report. For D_2, the induced graph on V_1 has no edges, yet its graph
  Steiner cost in D_2 is 6. For a unit three-leaf star, the leaf-set graph
  Steiner cost is 3, whereas a tree using only the terminal vertices in
  the shortest-path completion costs 4. These distinguish the allowed
  object from terminal-induced or terminal-only alternatives.
* **Positivity, connectivity, finiteness:** positivity and connectivity
  make the stated finite-graph costs positive and finite for every
  nontrivial set, as required by the distortion ratios. A zero-length
  single edge has a zero pair cost; two isolated vertices have infinite
  pair cost. They are outside the stated diversity/ratio domain. Zero
  edges could be studied after contraction and a changed definition, but
  no such extension is claimed. There is no finite small case violating
  finiteness. Connectivity is automatic from the diamond construction.
* **Planarity and treewidth:** in version 2 these are proved conclusions
  used to place the witness family in P/T, not premises used by the cut
  duality argument. One cannot violate them while retaining the underlying
  diamond graph. The length counterexamples retain both properties.
* **Finite-dimensional coordinate-range L1 target:** this is precisely
  what yields a nonnegative cut representation. All embeddings used here
  are finite-dimensional. No claim about a different target-diversity
  class is being made.

Trees give the positive-length exactness control by their weighted edge
cuts. For completeness, unit C4 also has an all-subsets upper embedding
matching 3/2: average the tree diversities of its four spanning paths.
Every such tree diversity is a sum of nonnegative cuts. For adjacent
pairs, opposite pairs, triples, and the full set, this average equals,
respectively, 3/2, 2, 5/2, and 3, while the graph costs are 1, 2, 2, and 3.
It is therefore noncontracting with distortion 3/2. The depth-1 certificate
gives the matching lower bound. This is an analytic classification of the
11 nontrivial subsets (4+2+4+1), not an executed enumeration.

The hypotheses used jointly are satisfiable: every unit D_d supplies the
graph, strict positivity, nested sets, terminal paths, and all sharp tail
cut witnesses at once. Each weighted counterexample also satisfies all
of the original graph/class/positivity hypotheses except uniformity.

## 5. The external logarithmic upper comparison

Checked in sources/bryant-tupper-open.txt, lines 99-133: Bryant--Tupper,
arXiv:1712.01960, Theorem 2, states that the Steiner diversity of an n-point
metric space has an L1 embedding with distortion O(log n). This check
confirms the stated theorem and its intended all-subsets target; it is not
an independent audit of the cited random-tree theorem.

Its graph transfer is exact. Complete V with shortest-path distances d_G.
Replacing each edge of a metric Steiner tree by a graph shortest path
produces a connected graph subgraph of no greater cost. Conversely, a
graph Steiner tree is a tree in the metric completion with no greater
cost. Minimization in both directions proves equality of the two Steiner
diversities, including the availability of all V as Steiner points.

Thus the external theorem gives O(log N_d) for every weighted diamond.
Together with L_d and N_d=(2*4^d+4)/3, the unit family has order log N_d;
the same order follows for uniformly bounded R, with the lower constant
depending on R. This is an order comparison, not an exact optimal c1
formula. It is not a logarithmic bound for every abstract diversity.

## 6. Exposure, resources, and disposition

Read: assignments/03-strengthener.md; BRIEF.md; PROOF.md version 2;
CERTIFICATE.md version 2; the installed idea-generator SKILL.md and its
references/templates.md; and the specified Bryant--Tupper source excerpt.
PROOF.md itself discloses that an alternative argument was adopted from a
sealed examiner report; this report's author was exposed to that disclosure
and the adopted proof, but did not open the sealed report. No other review,
initial report, KILLS.md, owner script, or private correspondence was read.
Owner feedback concerned distinguishing the bounded edge-ratio growth
statement from the exact arbitrary-length claim, and finishing without
additional experiments or generalizations.

All reasoning and checks here are analytic. No LP, enumeration program,
experiment, Python workload, package installation, long job, or nested
dispatch was run. Therefore experimental CPU consumption is 0 and there
are no job PIDs to terminate; read/write tooling overhead was not separately
CPU-instrumented. No Python interpreter was used, so no environment was
borrowed or bootstrapped. The only new file is this quarantine report.
The work was conducted within the 180-CPU-second / 20-minute allocation;
procedural elapsed time was not independently instrumented.

No email, contact, external service mutation, publication, or public-repository
operation occurred. No novelty search was attempted; novelty is UNRESOLVED.

Retire the proposed universal exact L_d strengthening to unrestricted
positive lengths: its earliest mathematical kill is the positive weighted
four-cycle above. Preserve common-scale invariance, the L_d/R comparison,
and the exact restricted optimum as separate claims for the owner's audit.

Recommended next action: **repair** the scope record to incorporate these
distinctions, then subject the adopted statements to the separately assigned
audit before promotion.
