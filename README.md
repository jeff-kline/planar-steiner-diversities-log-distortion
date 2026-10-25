# Planar Steiner diversities need logarithmic L1 distortion

Pre-release draft. Not admitted, not peer reviewed.

A diversity assigns a value to every finite set of points, extending a
metric from pairs to sets. The Steiner diversity of a graph gives each set of
vertices the length of the shortest connected subgraph that contains it. An
$\ell_1$ diversity comes from placing the vertices in $\mathbb{R}^m$ and adding,
over the coordinates, how far each set spreads. The distortion $c_1$ of a
diversity is the least factor $D$ such that some $\ell_1$ diversity lies
between it and $D$ times it, on every set at once.

This paper shows that the Steiner diversities of planar graphs cannot be
matched by $\ell_1$ diversities within any constant factor. The examples are
the diamond graphs, which are planar and have treewidth two. Distances between
pairs of vertices in these graphs embed in $\ell_1$ with distortion at most 2
(Chakrabarti, Jaffe, Lee and Vincent), but the diamond with $n$ vertices needs
distortion of order $\log n$ once all sets are counted. A known upper bound
shows that $\log n$ is the right order.

Read the [paper](paper/main.pdf) or its [TeX source](paper/main.tex).

## What is new

Bryant and Tupper showed that, for each hypergraph, the worst $\ell_1$
distortion of the diversities it supports equals the worst flow–cut gap for
demands on vertex sets, and proved that every Steiner diversity on $n$ points
has distortion $O(\log n)$. The lower bounds of order $\log n$ noted before
came from expander graphs, by way of their metrics.

**Principal result.** For $d\ge1$, build $D_d$ from a single edge by
replacing every edge, $d$ times, with two parallel paths of two unit edges.
Then $D_d$ is planar, has treewidth exactly two and has $N_d$ vertices, and
its Steiner diversity has distortion at least $L_d$:

```math
N_d=\frac{2\cdot4^d+4}{3},\qquad
c_1(D_d)\ge L_d=\frac{6d+7+2/4^d}{9}.
```

So no constant bounds the $\ell_1$ distortion of Steiner diversities on planar
graphs, or on graphs of treewidth two. With Bryant and Tupper's upper bound,
$c_1(D_d)$ grows exactly in proportion to $\log N_d$.

**Flow–cut form.** Give every edge of $D_d$ capacity one and ask that the
vertices present after round $j$ be connected with demand $2^{d-j}$ for
$j<d$, and demand $2$ for all vertices. These demands pass every cut test, yet
routing them fractionally by Steiner trees needs congestion at least $L_d$.
For demands between pairs on these graphs, the corresponding gap is at most 2.

**Further results.** Among certificates that weight every edge equally and
weight only the $d$ vertex sets present after each round, the certificate
behind the main bound is the unique best, and its value is exactly $L_d$. If
edge lengths vary by at most a factor $R$, the distortion is still at least
$\max(1,L_d/R)$. Some positive lengths on the same graphs give distortion 1,
so the unit lengths matter.

The upper bound of order $\log n$ is Bryant and Tupper's, and the reduction of
graph Steiner costs to their metric setting is routine. Bounded searches found
no earlier statement of the principal result or its certificate, but novelty
is not established; see the [prior-work record](audit/PRIOR_WORK.md).

## Claim and scope

One embedding must work for every set of vertices at once, and any vertex of
the graph may serve as a Steiner point. The proof is a short explicit
certificate built from $d$ nested vertex sets and does not use the recent
planar and bounded-treewidth metric theorems of
[OpenAI's problem #089](https://github.com/openai/math/blob/main/lean/docs/089.md),
which concern pairs only.

The result is about graphs, whose edges join two vertices. The
[predecessor paper](https://github.com/jeff-kline/covering-hitting-diversities)
studies hypergraphs. The bound is proved for unit edge lengths, not for every
choice of lengths. The exact value of $c_1(D_d)$ is determined here only for
$d\le2$.

| Statement | Status |
|---|---|
| Lower bound $c_1(D_d)\ge L_d$, planarity, treewidth two | proved on paper |
| Order $\log N_d$ | lower bound proved; upper bound cited from Bryant and Tupper |
| Flow–cut form | proved on paper |
| Best certificate of that shape; length dependence | proved on paper |
| 28 exact values in the paper's table | certified computation |

## A small example

The diamond $D_2$ has 12 vertices and 16 edges. Its four oldest vertices form
$V_1$ and all twelve form $V_2$; the paper's figure marks them. Connecting
$V_1$ takes 6 edges and connecting $V_2$ takes 11. Every cut $S$ of the vertex
set satisfies

```math
2\chi_S(V_1)+2\chi_S(V_2)\le |\partial S|,
```

where $\chi_S(V)$ is 1 when $S$ splits $V$ and 0 otherwise, and $|\partial S|$
counts the edges leaving $S$. Weighting both sides by $1/16$ gives the bound
$(2\cdot6+2\cdot11)/16=17/8$. A matching embedding shows that
$c_1(D_2)=17/8$ exactly. The checker confirms the inequality on all 2,048
cuts (one per complementary pair) and computes the exact Steiner cost of every
one of the 4,096 vertex sets, including the costs 6 and 11.

## Earlier work

David Bryant and Paul Tupper introduced diversities in
[*Hyperconvexity and tight-span theory for diversities*](https://doi.org/10.1016/j.aim.2012.08.008)
(2012). Their [*Diversities and the geometry of hypergraphs*](https://dmtcs.episciences.org/articles/2080)
(2014) relates $\ell_1$ distortion to flow–cut gaps. Their
[open-problem note](https://arxiv.org/abs/1712.01960v1) derives the
$O(\log n)$ bound for Steiner diversities from the random-tree approximation
of Fakcharoenphol, Rao and Talwar, and notes the general lower bound of order
$\log n$ inherited from expander metrics. Jozefiak and Shepherd's
[*Diversity embeddings and the hypergraph sparsest cut*](https://arxiv.org/abs/2303.04199v1)
(2023) gives algorithms and repeats that lower bound.

Gupta, Newman, Rabinovich and Sinclair (2004) showed that some
series-parallel graphs need distortion of order $\log n$ when embedded in
random trees, although series-parallel graphs embed in $\ell_1$ with constant
distortion. With Bryant and Tupper's random-tree upper bound, the present
result shows that, for Steiner diversities of diamonds, $\ell_1$ does no better
than random trees, up to a constant factor. Chakrabarti, Jaffe, Lee and
Vincent (2008) proved the series-parallel $\ell_1$ bound of 2. We quote both of
these results from the surveys in OpenAI's #089 papers and have not read the
originals.

## Evidence and artifacts

The general bound rests on the proof in the paper. Separate AI reviews checked
the source proofs and then this paper's full text, including the flow–cut
form; the records are listed in [audit/EVIDENCE.md](audit/EVIDENCE.md) and
[AUDIT_LEDGER.md](AUDIT_LEDGER.md). The finite checks cover the two smallest
diamonds and 28 exact certificates; they do not prove the general bound.

- [BUILD.md](BUILD.md): dependencies and reproducible commands.
- [VERIFICATION.md](VERIFICATION.md): what the checker and build verify.
- [AUDIT_LEDGER.md](AUDIT_LEDGER.md): review scope and dispositions.
- [audit/EVIDENCE.md](audit/EVIDENCE.md): provenance and hashes of the research records.
- [audit/PRIOR_WORK.md](audit/PRIOR_WORK.md): searches, sources and their limits.
- [CORRECTIONS.md](CORRECTIONS.md): correction policy.
- [CITATION.cff](CITATION.cff): citation metadata.
- [MANIFEST.sha256](MANIFEST.sha256): hashes of all tracked files.

## Reproduction

From the repository root, with Python 3 (standard library only) and pdfLaTeX:

```sh
make paper PYTHON=python3 PDFLATEX=pdflatex
make verify PYTHON=python3
```

The checker uses exact rational arithmetic; no solver is needed. The paper
build runs twice and requires identical PDF bytes and warning-free logs. See
[BUILD.md](BUILD.md) for the checked installation.

## AI assistance and responsibility

AI systems helped find the result, attack and check the proof, verify the
finite certificates, extract bibliographic data and draft the text, under
Jeff Kline's direction. AI is not an author or a referee, and AI review is not
peer review. Jeff Kline is responsible for the claims and their presentation.

## Citation and status

Jeff Kline. *Planar Steiner diversities need logarithmic L1 distortion*.
Pre-release draft, October 2026. See [CITATION.cff](CITATION.cff).

## License

Original paper, source, prose and code: copyright 2026 Jeff Kline, GNU General
Public License version 3 only (`GPL-3.0-only`); see [LICENSE](LICENSE). Cited
works keep their authors' rights and are not bundled.
