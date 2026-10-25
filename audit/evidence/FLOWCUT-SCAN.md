# FLOWCUT-SCAN (2026-10-25)
Raw: arxiv_*.xml (5 arXiv API queries), csw.pdf (arXiv 1008.2136, downloaded, NOT read in full).
## Local source reads
- sources/bryant-tupper-2014.txt: Thm 1 (line 121), Thm 2 (line 129), Thm 17 (line 870), Thm 18 (line 884); MaxHSP LP (11) lines ~714-727. Statement: for every hypergraph H (graphs = rank 2), k1(H) = max over C supported on H, D of MinHypCut/MaxHSP.
- sources/jozefiak-shepherd.txt: line 878 "there is an Omega(log n) lower bound for distortion of l1 embeddings" (generic, from metrics); line 276 flow-cut gap equals diversity distortion, restated; no planar/sp/treewidth lower bound found by grep (planar|series|treewidth|diamond give none).
- openai-treewidth/planar/bryant-tupper-open: grep for diversit/Steiner: only bryant-tupper-open (generic).
## arXiv API (OK)
1 abs:"Steiner tree packing" -> 15 hits, none relevant besides BT2014 (Diversities and the Geometry of Hypergraphs)
2 abs:"Steiner multiflow" -> 0
3 abs:"hypergraph sparsest cut" -> 0 (JS paper 2303.04199 uses different abstract wording)
4 diversity AND embedding AND Steiner -> BT2014 only
5 multicommodity AND Steiner tree AND flow-cut -> 0
## WebSearch (OK, 9 queries) - no source states (a) or (b)
Hits: 1203.4041 (Chakrabarti-Fleischer-Weibel, cut condition sp, pairs); 1008.2136 (CSW flow-cut gaps, pairs; sp integer gap 5); 2507.06576 (sp flow-cut gap 2); 2303.04199 (Jozefiak-Shepherd); GNRS Combinatorica 24 (2004) abstract: Omega(log n) lower bound for series-parallel graphs into distributions over dominating trees (metric); Lau Combinatorica 27 (2007) Steiner packing vs Steiner cut (single set, constant); Aazami-Cheriyan-Jampani planar element-disjoint packing (NP-hardness); Chekuri et al element-forest-packing (planar Omega(k) element-disjoint fractional claim).
## gh (OK): positive control `gh search code treewidth --repo openai/math` HIT (openai/math preprints L1-Embeddings-of-Graphs-of-Bounded-Treewidth..., lean/docs/089.md)
- gh search code Steiner multiflow: OK, irrelevant (rebiber STOC bib entries "multiflow problems in series-parallel networks" = CFW)
- gh search repos steiner diversity: OK, 0 relevant (output empty/irrelevant)
- gh search code hypergraph sparsest cut: OK; nveldt/HyperCutMatch (algorithm code), openai/math overview (uniform sparsest cut) - irrelevant
- gh search code Steiner packing series-parallel / hexagonmath Steiner diversity / Steiner diversity embedding / diamond graph Steiner tree packing: OK, irrelevant
- First attempt of three queries as quoted single string failed (command not found) -> NOT PERFORMED, rerun correctly above.
## NOT PERFORMED
hexagonmath.org site fetch; Zenodo search; Google Scholar citing-papers listing for BT2014/JS2023; full-text read of GNRS, Lee-Naor, CSW, Lau, Chekuri element-forest paper.
