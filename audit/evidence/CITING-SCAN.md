# CITING-SCAN (2026-10-25)
No email/key sent anywhere. Files here: raw JSON (js_cites.json, bt_cites.json, ht_cites.json, oa_*.json), pdf/ (arXiv PDFs + pdftotext .txt).

## Requests
1. S2 /paper/arXiv:2303.04199/citations: 429 (x3 incl. one retry after sleep 20) -> NOT PERFORMED; 4th try (after sleep 20 + other calls) HTTP 200, 2 citers (js_cites.json).
2. S2 /paper/arXiv:1312.5408 (id check): 429, NOT PERFORMED (id verified instead via OpenAlex: "Diversities and the Geometry of Hypergraphs", arXiv 1312.5408, DMTCS doi 10.46298/dmtcs.2080).
3. S2 citations of DOI 10.46298/dmtcs.2080: 200, 25 citers (bt_cites.json).
4. S2 citations of DOI 10.1016/j.aim.2012.08.008 (Hyperconvexity): 200, 49 citers (ht_cites.json; titles scanned only).
5. OpenAlex search x3 (ids): OK. W1943297633 (BT DMTCS), W2952455252 (BT arXiv), W2051986117 (Hyperconvexity), W6961193918 (JS).
6. OpenAlex cites: BT DMTCS 18 citers; BT arXiv record 0; Hyperconvexity (oa_cites_ht.json) ~36; JS record 0 (coverage gap; S2 gives 2).
7. Full texts via curl arxiv: 2303.04199, 2412.07092, 2608.11468, 2501.13202, 1712.01960, 1604.01863, 1606.09183, 1312.5408, 2010.11442 (all OK).
Caveat: S2/OpenAlex counts are low and incomplete (JS is 2023; S2 lists only 2 citers, both diversity-theory papers).

## Screened citers (BT 2014; union S2+OA, 25)
Only graph-class/lower-bound-relevant candidates; the rest (Urysohn/universal diversities, ultradiversities, Fraisse limits, automorphism groups, Parsimonious Labeling (vision), consecutive-ones, thesis items, Lower Ricci curvature for hypergraphs, Topological k-metrics, generalized circumradius, lattice diversities, negative-type diversities (abstract-only), Steiner Wiener index (abstract/grep only, no diversity embeddings)) are not relevant by title/abstract.
- 1712.01960 Bryant-Tupper Open Problem, 2017: FULL TEXT. States worst-case L1 diversity distortion as open; Open question 2 (p.7): "Expander graphs have proven to be a good source for lower bounds ... Expander hypergraphs are far less understood". No planar/sp result.
- 1604.01863 Constant distortion embeddings of symmetric diversities, 2016: FULL TEXT grep. "motivated by a search for provable lower bounds for diversity embeddings"; no lower bound proven for Steiner diversity on any graph class.
- 2303.04199 Jozefiak-Shepherd (seed): FULL TEXT. O(log n) L1 embedding of diameter diversities; hardness (n^{1-eps}, P!=NP) for arbitrary diversities; line 878: "As noted in [7], there is an Omega(log n) lower bound for distortion of l1 embeddings" (general, via metrics/expanders). Flow-cut Omega(log n) cited via constant-degree expanders (l.223-231). Nothing on planar/sp/treewidth.
- 2412.07092 Linear and Sublinear Diversities, 2024: FULL TEXT grep: Steiner only mentioned as an example diversity. No lower bound.
- 2608.11468 Submodular functions and diversities, 2026: grep: Steiner mentioned only as example. No.
- 2501.13202 Subtree distances, tight spans, diversities, 2025: grep: no relevant hits.
- 1606.09183 Graphlike families of multiweights: grep: no hits for planar/Steiner/lower bound.
- 2010.11442 Lattice diversities: no.
- Hyperconvexity citers (49, titles only): none on embedding L1/Steiner/flow/cut/planar/treewidth beyond the same diversity papers above; 2506.xxxx etc unrelated (biodiversity, phylogenetics, Banach spaces).
- JS citers (S2): only 2608.11468 and 2412.07092 (above). OpenAlex fulltext search "Diversity embeddings and the hypergraph sparsest cut" (25 hits, oa_js_fulltext.json): one extra potentially related: 2607.13218 "Graph Partitioning with Demands: Generalized Conductance" (abstract only, NOT full-text checked; pairs/vertex-demand graph partitioning, likely not Steiner-set). Not decisive.

## CSW (arXiv 1008.2136, csw.pdf; pdftotext)
Demand graph H = (V,E(H)): PAIR demands only. grep for steiner|hypergraph|set demand|terminal set|diversit: zero hits. Results: series-parallel integer flow-cut gap 5; fractional gap >= 2 - o(1) (abstract). Not about set demands.

## Verdict
SOURCE-NEGATIVE: no citing paper found (of those reachable) proves Omega(log n) L1 diversity distortion or set-demand/hypergraph flow-cut gap on planar/sp/bounded-treewidth/outerplanar/diamond graphs. Only general-graph/expander Omega(log n) statements appear. Limited by API coverage.
