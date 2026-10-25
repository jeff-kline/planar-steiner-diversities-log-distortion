# Planar Steiner diversities need logarithmic L1 distortion

Pre-release draft. Not admitted, not peer reviewed.

A graph's Steiner diversity assigns to each vertex set the minimum cost of a
connected subgraph containing it. An $\ell_1$ diversity sums coordinate ranges.
This paper proves that one such embedding cannot preserve every Steiner set
cost within a constant factor, even for planar graphs of treewidth two.
Read the [paper](paper/main.pdf) or its [TeX source](paper/main.tex).

## What is new

Bryant and Tupper developed diversities, their cut representation and their
flow–cut correspondence, and proved an $O(\log n)$ upper bound for metric
Steiner diversities. Jozefiak and Shepherd record a general-graph logarithmic
lower bound inherited from expander metrics. Those results do not give the
planar, treewidth-two witness proved here.

**Principal result.** Let $D_d$ be the unit graph obtained from an edge by
replacing every edge with two internally disjoint two-edge paths, for
$d\ge1$ rounds. It is planar, has treewidth exactly two, and satisfies

```math
N_d=\frac{2\cdot4^d+4}{3},\qquad
c_1(D_d)\ge L_d:=\frac{6d+7+2/4^d}{9}.
```

Thus no constant bounds graph Steiner-diversity distortion on either class.
Together with Bryant and Tupper's upper bound, this gives
$c_1(D_d)=\Theta(\log N_d)$.

**Set-demand consequence.** On the same graph with unit edge capacities,
give demand $a_j=2^{d-j}$ to the generation set $V_j$ for $1\le j\le d-1$,
and demand $a_d=2$ to $V_d$. Every cut condition holds, but fractional
Steiner-tree routing of the full demands requires congestion at least $L_d$.
This is an explicit instance of Bryant and Tupper's flow–cut framework.

**Secondary results.** Among dual certificates supported on those generation
sets with uniform edge weights on the other side, the optimal lower bound
is exactly $L_d$. If positive edge lengths have ratio at most $R$, the bound
becomes $c_1(D_d,\ell)\ge\max(1,L_d/R)$. There are also positive length
assignments on each underlying diamond with $c_1=1$.

These are the results whose priority is being assessed. Three bounded scans
found no matching theorem or mechanism; novelty remains unresolved.

## Claim and scope

All graph vertices are available as Steiner points, and a single finite-
dimensional coordinate-range embedding must work for every terminal subset.
The proof is an all-depth rational dual certificate with only $d$ demand
sets. The lower bound does not use the recent metric theorems associated
with [OpenAI's problem #089 materials](https://github.com/openai/math/blob/main/lean/docs/089.md).
Those concern pairs. The series-parallel metric bound of two is attributed
to Chakrabarti, Jaffe, Lee and Vincent in the planar paper's Section 1.2;
that secondary attribution is the scope of our source exposure.

The result concerns graph edges, each joining two vertices. It differs from
the hypergraph construction in the [predecessor paper](https://github.com/jeff-kline/covering-hitting-diversities).
Unit lengths provide the witness. The bound is not asserted for every
positive-length assignment, and $c_1(D_d)=L_d$ is not claimed for $d\ge3$.
The secondary optimality result fixes the dual support and uniform edge
weights; it does not solve the unrestricted embedding problem.

## A small example

The diamond $D_2$ has 12 vertices and 16 edges. Its four old vertices form
$V_1$; all vertices form $V_2$. The [paper's diagram](paper/main.pdf) marks
these sets. Their exact Steiner costs are 6 and 11. The cut inequality is

```math
2\chi_S(V_1)+2\chi_S(V_2)\le |\partial S|.
```

Normalizing by the 16 edges gives objective $(2\cdot6+2\cdot11)/16=17/8$.
The saved matching upper certificate proves $c_1(D_2)=17/8$. The checker
covers all 2,048 cut representatives, including the empty cut, and enumerates
all 4,096 vertex subsets. This finite check does not prove the general theorem.

## Earlier work

Bryant and Tupper's *Hyperconvexity and tight-span theory for diversities*
(2012) introduces the framework. Their [*Diversities and the Geometry of
Hypergraphs*](https://dmtcs.episciences.org/articles/2080) (2014) develops cut
representations and the equality between worst flow–cut gaps and diversity
distortion. Their [open-problem statement](https://arxiv.org/abs/1712.01960v1),
Theorem 2, supplies the cited upper bound. Its arXiv version is dated 2017,
while the saved PDF prints a 2021 date; the audit records that discrepancy.

[Jozefiak and Shepherd](https://arxiv.org/abs/2303.04199v1) give general-graph
context and approximation results. Gupta, Newman, Rabinovich and Sinclair's
*Cuts, Trees and L1-Embeddings of Graphs* (2004) gives a nearby logarithmic
obstruction for series-parallel metrics mapped into distributions of
dominating trees, a different target. Only its publisher abstract was read
for this draft. The CJLV primary paper was not inspected.

[PRIOR_WORK.md](audit/PRIOR_WORK.md) summarizes all three scans and their
limits. [BIBLIOGRAPHY-EXTRACTION.md](audit/BIBLIOGRAPHY-EXTRACTION.md) records
which source supports each entry. Unchecked full texts and bounded negative
search results do not establish novelty.

## Evidence and artifacts

The general lower bound rests on the proof. The exact finite checks cover
28 copied rational primal/dual certificates and two small diamonds; they do
not establish the all-depth claim. The source proof audit and adjudication
are preserved unchanged with their qualifications. AI-assisted proof review
is not peer review or formal proof-assistant certification.

- [BUILD.md](BUILD.md): dependencies and reproducible commands.
- [VERIFICATION.md](VERIFICATION.md): checks, runtime, build and visual review.
- [AUDIT_LEDGER.md](AUDIT_LEDGER.md): research review scope and draft preparation.
- [EVIDENCE.md](audit/EVIDENCE.md): provenance and hashes of copied evidence.
- [CORRECTIONS.md](CORRECTIONS.md): correction policy.
- [CITATION.cff](CITATION.cff): draft citation metadata.
- [MANIFEST.sha256](MANIFEST.sha256): local draft file integrity.
- [NOTICE](NOTICE): provenance and licensing scope.

## Reproduction

Use the explicitly selected virtual environment and pdfLaTeX:

```sh
make paper PYTHON="$HOME/.venvs/claude/bin/python" PDFLATEX=/opt/local/bin/pdflatex
make verify PYTHON="$HOME/.venvs/claude/bin/python"
```

The verifier uses only the Python standard library. No solver or package
installation is needed. The PDF builder requires two clean two-pass builds
to have identical bytes and warning-free final logs. See [BUILD.md](BUILD.md)
for resource caps and cross-installation limits.

## AI assistance and responsibility

AI systems assisted with research, adversarial examination, exact certificate
checks, bibliography extraction and draft preparation under Jeff Kline's
direction. AI is not an author or referee. Jeff Kline is responsible for the
claims and presentation. The preserved records distinguish a statement-only
attack from the later full proof audit.

## Citation and status

Jeff Kline. *Planar Steiner diversities need logarithmic L1 distortion*.
Pre-release draft, October 25, 2026.

Pre-release draft. Not admitted, not peer reviewed.
This local repository has no remote, release tag, archive or publication
identifier. The coordinating session owns any later review and release.

## License

Original paper, source, prose and code: copyright 2026 Jeff Kline,
GNU General Public License version 3 only (`GPL-3.0-only`); see [LICENSE](LICENSE).
Earlier works retain their authors' rights and are cited rather than bundled.
