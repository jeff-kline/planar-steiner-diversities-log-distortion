# Stage 0 — 2026-10-25

Post-refinement adjacency check on 2026-10-25: web-10-nested.json records three queries pairing diamond graphs with diversities, Steiner diversity with diamond, and diversity with series-parallel embedding. Results were mostly relaxed irrelevant matches; no source settling the all-set claim was identified. An older dominating-tree metric lower bound surfaced via secondary indexes, which is a nearby result but does not itself establish a lower bound against all L1 diversities. No originality claim follows from this search.

Status: no source settling P or T located in the recorded bounded scan. This is a source-negative observation, not novelty certification. All queries and returned hits are preserved in `searches/`; failed web fetches are NOT PERFORMED, even where a later direct retrieval succeeds.

Positive control: GitHub code search `treewidth repo:openai/math` found #089 and source files. Initial restrictive `Bounded-distortion ... path:lean/docs/089.md` returned no hit; it did not pass the control. A prior sandbox failure was retried with authorized network access.

GitHub: queried `diversity treewidth`, `Steiner diversity planar`, `Steiner diversity extension:tex`, repositories `Steiner diversity`, `planar L1`, `diversity embeddings`; queried identifiers `PlanarL1` and `BoundedTreewidthL1` excluding openai/math. Results include mirrors, audit repositories, and Keith Adler's planar-l1-companion/planar-l1-lean. Code search for diversity in these two companions returns []. Broad searches have noisy, truncated-to-limit result sets; they are not exhaustive. Plain-output identifier searches were tool-truncated and repeated as JSON metadata (gh-12/13).

Web: paired Steiner diversity/diversity embeddings with treewidth, planar, series-parallel, outerplanar; searched recent/post-release and arXiv/Zenodo/Hexagon-specific queries. Raw queries and sources are in web-01 through web-07 JSON. Irrelevant broad/relaxed results do not count as evidence of a theorem.

Direct retrievals: `https://hexagonmath.org/search?q=diversity` returns zero matching works; `https://zenodo.org/api/records?q=%22Steiner%20diversity%22&size=20` returns zero. Web-tool versions of these requests failed; curl succeeded. The arXiv API broad diversities query is overly broad due stemming (105409 hits, first 25 saved) and does not constitute a focused scan; focused primary-paper and web/arXiv searches supply the relevant coverage.

## Checked sources and scope

- OpenAI #089 scope: https://github.com/openai/math/blob/main/lean/docs/089.md. Both results are explicitly about shortest-path metrics. Papers downloaded to `sources/openai-planar.pdf` and `sources/openai-treewidth.pdf`; extracted text beside them. Treewidth paper Section 1.2 outlines exact bag marginals, bounded-state Markov transport, and a lower bound for each pair. Planar paper Sections 1.3 and 9 outline cut separation at each pair's distance scale. No simultaneous all-set lower bound is stated.
- Jozefiak–Shepherd https://arxiv.org/abs/2303.04199: submission history checked, only v1 dated 2023-03-07 listed. Author page https://www.mit.edu/~jozefiak/ says minor revision at DMTCS; no published revised theorem verified. DBLP records the 2023 preprint. Primary PDF saved. Its general graph-supply bound is O(log n), not a constant for planar/treewidth classes.
- Bryant–Tupper https://arxiv.org/abs/1712.01960: Theorem 2 gives O(log n) for metric Steiner diversities via dominating random trees. Graph Steiner diversity equals the metric Steiner diversity of its shortest-path metric (replace metric tree edges by graph paths in one direction, and use the graph's optimum tree in the other). This does not give the proposed constants.
- Bryant–Tupper https://dmtcs.episciences.org/2080/pdf: graph/hypergraph fractional Steiner tree packing and diversity flow-cut duality. Saved source; this motivates checking multi-terminal cut certificates rather than one-terminal-set integrality gaps.
- The released local paper at 60d135d is hypergraph-specific; its affine supply edges have size q+1. No graph conclusion is inherited.

Primary source downloads used curl with the five URLs stated above or the full OpenAI preprint URLs in the handoff, on 2026-10-25; all succeeded. No authors contacted.

## Focused follow-up coverage

`searches/focused-requests.json` records direct API requests after the initial web scan. The arXiv query `ti:diversities AND (cat:math.MG OR cat:math.CO OR cat:cs.DS)`, newest first, returned 134 results; the first 50 extend back to April 2024, including all results after the September 2026 trigger within this indexed query. Titles/abstracts screened: Bryant–Tupper, Submodular and strongly submodular functions and diversities (2608.11468v1); Bryant et al., Subtree Distances, Tight Spans and Diversities (2501.13202v2); Bryant–Tupper, Linear and Sublinear Diversities (2412.07092v3); Aishwarya et al., Metric complexity is a Bryant–Tupper diversity (2507.09698v2). These abstracts concern other embedding/representation questions; no P/T theorem identified. This is abstract-level screening, not full-paper exclusion.

The expanded Zenodo Boolean API query returned HTTP 400: NOT PERFORMED. The exact-phrase Steiner-diversity search did succeed with zero results. Direct Hexagon `q=Steiner` also retrieved successfully (HTML saved). Narrow diamond/Steiner-packing search queries are in web-08 and web-09; no settled all-set diamond-distortion claim identified. Search limitations remain explicit.
