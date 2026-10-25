# Prior work and search limits

Version 0.1.0, admitted October 25, 2026. Not peer reviewed.
Novelty: **UNRESOLVED**. Three bounded scans were **SOURCE-NEGATIVE**;
no matching source was found within their inspected coverage. That outcome
is not a proof of priority or of absence from the literature.

## The result under comparison

Unit graph diamonds have logarithmically growing coordinate-range L1
Steiner-diversity distortion, already in planar graphs of treewidth two.
The mechanism is a pointwise cut inequality on nested generation sets and
their exact Steiner costs, with a dual certificate of logarithmically many
support sets. Priority must be assessed for both the theorem and this
mechanism, including its set-demand Steiner-packing form.

## Three inherited scans

The source root is `../quarantine/steiner-diversity-tw-2026-10-25/` relative
to the draft repository. The following logs are copied unchanged in
`audit/evidence/` and their hashes are in `EVIDENCE.md`.

| Scan | Source path | Coverage and limits |
|---|---|---|
| Diversity terminology | `LITERATURE.md`, with underlying `searches/` | Bounded web, arXiv, GitHub, archive and hexagon-oriented queries; noisy and failed responses retained. No exhaustive indexing or novelty certification. |
| Flow–cut terminology | `searches/flowcut/FLOWCUT-SCAN.md` | Read the BT2014 definitions and correspondence; bounded arXiv, web and GitHub queries. Several databases, full citer retrieval and GNRS full text were not performed. |
| Citing papers | `searches/citing/CITING-SCAN.md` | Selected Semantic Scholar/OpenAlex citers of BT2014, BT2012 and JS2023; rate limits, coverage gaps and selective full-text inspection. A 2026 candidate remained abstract-only and unresolved. |

The current draft task added only bibliographic checks of named references.
It did not extend these scans. The copied logs' relative references often
point into the larger read-only research workspace, which is not wholly
bundled here. Do not represent them as a complete portable search archive.

## Credit and nearest analogues

Bryant and Tupper (2012) introduced diversities. Their 2014 paper supplies
cut representations and the general hypergraph flow–cut correspondence.
The paper here checks its normalization directly for the proposed demands.
Their arXiv:1712.01960v1 Theorem 2 is the cited logarithmic upper bound for
metric Steiner diversities. The shortest-path metric completion has exactly
the graph Steiner costs when all graph vertices remain available. This
transfer is explained in the draft. The external random-tree theorem and
its cited proof are not independently audited here. The saved PDF's printed
2021 date differs from the arXiv version date of 2017; no later version is
inferred from that discrepancy.

Jozefiak–Shepherd arXiv:2303.04199v1 discusses general-graph logarithmic lower
bounds via expander metrics. That does not give the planar theorem here.
Gupta–Newman–Rabinovich–Sinclair (2004) gives a nearby lower bound for
series-parallel metrics in random dominating trees, a different target.
The current bibliographic check read its publisher abstract, not the full
proof. Chekuri–Shepherd–Weibel arXiv:1008.2136 is another nearby flow–cut
reference examined in the inherited scans; its demands are pairs. Neither
comparison is evidence that no earlier set-demand construction exists.

The metric upper bound of two for series-parallel graphs is attributed to
Chakrabarti–Jaffe–Lee–Vincent in the saved OpenAI planar and treewidth papers.
The original CJLV paper was not read. The draft states this as a secondary
attribution and does not assert isometric embeddability of diamond metrics.
The OpenAI papers concern pair metrics, and are contextual rather than
premises of the lower-bound certificate. Their proofs are not audited here.

Kline's predecessor uses hypergraph supplies and an affine covering-versus-
hitting mechanism. Its compact-realization priority also remained unresolved.
It is credited as earlier work, not used to imply that the new graph result
has established priority.

## Questions retained for the coordinator

- Does the planar set-demand statement or generation-set mechanism occur in
  older Steiner-packing, cut-condition or diamond-graph literature?
- Should CJLV and GNRS primary full texts be inspected before public claims
  about those analogues are expanded beyond the present qualified wording?
- Can the printed date discrepancy in the Bryant–Tupper upper-bound source
  be explained without inferring an unverified revision?
- Do the recorded unresolved citing candidates change the priority assessment?

These questions do not trigger new searches under the current bounded draft
instruction. Full bibliographic exposure and access failures are recorded in
`BIBLIOGRAPHY-EXTRACTION.md`.
