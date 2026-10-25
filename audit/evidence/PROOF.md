# Diamond graph Steiner diversities: a generation-set certificate

Version 2, 2026-10-25. Status: VERIFIED by the fresh Stage 2 audit in PROOF-AUDIT.md and accepted in ADJUDICATION.md. This post-audit change updates status only; PROOF-v2.md preserves the submitted bytes. Private artifact; novelty unresolved.

**Theorem.** Let D_d be obtained from a single edge by d rounds of replacing every edge with two internally disjoint paths of two unit edges. For every integer d>=1,
\[
c_1(D_d)\ge L_d:=\frac{6d+7+2/4^d}{9}.
\]
There are N_d=(2*4^d+4)/3 vertices. Each D_d is planar with treewidth exactly two. Consequently both P and T in BRIEF.md are false, already for unweighted graphs and treewidth two. Graph Steiner diversity permits every graph vertex as a Steiner point and requires one embedding for every terminal subset simultaneously.

This version explicitly adopts the alternative argument in the sealed isolated examiner report assignments/02-initial-report.md. That initial report remains NOT-BROKEN; verification comes from the subsequent fresh full audit. PROOF-v1.md is preserved separately and remains unexamined.

## 1. Cut representation and duality

Write chi_S(A)=1 if A meets both S and S^c, and zero otherwise. Every finite coordinate-range L1 diversity h is a finite nonnegative sum h=sum_S w_S chi_S. For each coordinate, sort its distinct values and assign each consecutive gap to its upper threshold cut. A set crosses exactly the thresholds between its minimum and maximum. Conversely, the coordinate w_S*1_S realizes w_S chi_S.

If nonnegative measures alpha,beta on subsets satisfy
\[
\sum_A\alpha_A\chi_S(A)\le\sum_A\beta_A\chi_S(A)
\quad\hbox{for every cut }S,\qquad
\sum_A\beta_A\delta(A)=1,
\]
then delta<=h<=D*delta implies
\[
\sum_A\alpha_A\delta(A)\le
\sum_A\alpha_A h(A)\le
\sum_A\beta_A h(A)\le D.
\]
Thus such a pair is an exact dual certificate for every allowed finite dimension.

## 2. Geometry and graph class

Keep vertices from earlier generations, writing V_0 subset V_1 subset ... subset V_d. Each round replaces E edges with 4E edges and adds 2E vertices. Hence E_d=4^d and N_d=2+2 sum_(i=0)^(d-1)4^i=(2*4^d+4)/3.

Each old edge at generation j has an edge-disjoint descendant gadget D_(d-j), whose interior meets no other gadget. Its terminal distance is 2^(d-j), and it has 2^(d-j) edge-disjoint terminal paths. Both assertions follow inductively: a diamond consists of two parallel branches, each a series composition of two smaller diamonds. Distances double; corresponding paths concatenate within each branch and the two branch collections are edge-disjoint.

Each D_j, j>=1, is bridgeless. Every final edge lies in the four-cycle replacing its parent edge. Since D_j is connected, every nontrivial vertex cut in D_j therefore crosses at least two edges.

Planarity follows by replacing each edge of a planar drawing within a narrow neighborhood by its two new paths. An explicit width-two tree decomposition survives replacement. Start with bag {u,v} for the original edge. When an edge xy is replaced through new vertices a,b, attach bags {x,y,a} and {x,y,b} to an existing bag containing x,y. Such a bag exists by old edge coverage. New edges are covered, and occurrences of each vertex remain connected in the bag tree. Old bags may be retained after their edges disappear. All bags have at most three vertices. Since D_d contains a cycle for d>=1, its treewidth is exactly two.

## 3. A simultaneous inequality for every cut

Define a_j=2^(d-j) for 1<=j<d, and a_d=2. For every cut S of D_d,
\[
\sum_{j=1}^d a_j\chi_S(V_j)\le |\partial_{D_d}S|. \tag{1}
\]
Trivial cuts have both sides zero. For a nontrivial cut, let q be the first generation in {1,...,d} with chi_S(V_q)=1. It exists because V_d is the whole vertex set. Nesting implies the indicators are zero before q and one thereafter.

The restriction S intersect V_q is a nontrivial cut of D_q and crosses at least two edges. Their descendant D_(d-q) gadgets are edge-disjoint. In each, S separates the endpoints and must cross all 2^(d-q) edge-disjoint terminal paths. Hence
\[
|\partial_{D_d}S|\ge2^{d-q+1}
=\sum_{j=q}^d a_j
=\sum_{j=1}^d a_j\chi_S(V_j).
\]
This includes q=d and d=1. It is a pointwise inequality for arbitrary cuts, not a pairwise separation estimate.

## 4. Exact Steiner costs of generation sets

For 1<=j<=d,
\[
\delta_{D_d}(V_j)=2^{d-j}(N_j-1). \tag{2}
\]
For the upper bound, choose a spanning tree of D_j. In each of its N_j-1 edge gadgets choose a shortest terminal path of length 2^(d-j). Their union is connected and contains V_j.

For the lower bound, let H be any connected subgraph containing V_j. Retain a coarse edge of D_j whenever H connects that edge's endpoints within its descendant gadget. The retained coarse edges connect V_j: a simple H-path between old vertices, divided at its successive old vertices, consists of passages through single gadgets between their endpoints. Different gadgets meet only at old endpoints. Each passage gives a retained coarse edge. At least N_j-1 gadgets are retained. Each costs at least 2^(d-j) edges, and their edge sets are disjoint. This proves (2) even when H uses arbitrary newer Steiner vertices.

## 5. Exact certificate and objective

Put alpha_(V_j)=a_j/4^d and zero elsewhere. Put beta_({u,v})=1/4^d on every final graph edge and zero elsewhere. These are nonnegative rational measures with only d alpha support sets. Every final edge pair has Steiner cost 1, so sum beta_A delta(A)=1. Equation (1), divided by 4^d, gives all-cut dual feasibility.

The objective is exactly
\[
\begin{aligned}
\sum_A\alpha_A\delta(A)
&=\frac{1}{4^d}\left[
\sum_{j=1}^{d-1}\frac{4^{d-j}(2\cdot4^j+1)}3
+\frac{2(2\cdot4^d+1)}3\right]\\
&=\frac{2(d-1)}3+\frac19(1-4^{-(d-1)})
+\frac43+\frac{2}{3\cdot4^d}\\
&=\frac{6d+7+2/4^d}{9}.
\end{aligned}
\]
The sum is empty for d=1. Cut duality proves the theorem. Since N_d is proportional to 4^d, the lower bound grows as (2/3) log_4 N_d+O(1). Its divergence refutes P and the k=2 instance of T. No assertion is made that L_d equals c1(D_d) for every d.

## 6. Controls, dependencies, and scope

Trees with positive lengths have c1=1 by their weighted edge-cut representation. Unit cycles and complete graphs have c1(C_n)=c1(K_n)=2(n-1)/n (n>=3); exact derivations are in KILLS.md. D_1=C4 gives L_1=3/2 and D_2 gives L_2=17/8, matching independently verified rational primal/dual certificates. Finite computations are controls, not premises of this all-d proof.

The theorem is self-contained apart from elementary graph/cut facts proved or explained above. The external O(log N) upper bound for graph Steiner diversities follows from Bryant–Tupper, arXiv:1712.01960, Theorem 2; it is used only to identify growth order, not to establish the refutation. Graph and shortest-path metric Steiner costs agree: substitute graph paths for metric tree edges in one direction and view a graph Steiner tree as a metric-edge tree in the other.

Uniform lengths are a sufficient witness choice, not an assumption in P or T: those universal statements include these unit-length examples. No conclusion about every possible length assignment on diamonds is asserted. No hypergraph lower bound or #089 metric theorem is used in the certificate.

