# Bibliographic extraction for the pre-release draft

Date: 2026-10-25. Status: bibliographic extraction, not a proof review or a
novelty determination. The owner controls all paper wording and citation choices.

## Exposure and limits

The local source root below is
`/Users/klinellc/Documents/hm-ai/quarantine/steiner-diversity-tw-2026-10-25/sources/`.
Line references refer to the saved `.txt` files there, without alteration.
The predecessor root is
`/Users/klinellc/Documents/hm-ai/covering-hitting-diversities/`.

Read the destination's `AGENTS.md` and `PLAN.md`. At extraction time, `BUILD.md`,
`audit/PRIOR_WORK.md`, and `audit/EVIDENCE.md` were not yet present. The owner
explicitly directed this source-only extraction to proceed while those records
were being drafted.

Saved title pages, specified scope passages, and bibliographies were inspected.
External access was limited to exact bibliographic records, the official OpenAI
#089 index and its paper links, and the GNRS publisher abstract. Exact-title
searches were used only to resolve BT2012 publisher metadata and the CJLV
conference DOI. No new prior-art campaign, proof verification, experiment,
installation, repository mutation outside this file, contact, or email occurred.
Search results unrelated to these requested bibliographic records were not
investigated. Browser-returned records can be cached; the access date here is
not a claim that every record was freshly fetched from its origin.

## Bryant and Tupper (2012)

Verified fields: David Bryant and Paul F. Tupper. **Hyperconvexity and tight-span
theory for diversities**. *Advances in Mathematics* **231**(6), 3172–3198 (2012).

- Saved `bryant-tupper-2014.txt`, lines 959–960, gives authors, title, journal,
  volume, issue, pages, year, and DOI.
- Saved `bryant-tupper-open.txt`, lines 354–355, independently repeats the
  bibliographic fields except DOI.
- Predecessor `paper/main.tex`, lines 669–672, agrees.
- The [ScienceDirect publisher record](https://www.sciencedirect.com/science/article/pii/S0001870812003167),
  returned by the exact-title search, confirms the full author names and all
  above fields, with issue date **20 December 2012**. A subsequent direct page
  open returned HTTP 403; the DOI resolver also was inaccessible through the
  browsing tool.

Exposure gap: no separate BT2012 full text was in the specified saved-source
directory, and none was read for this task. Publisher metadata was visible in
the search-returned record, not a successfully opened full article.

## Bryant and Tupper (2014)

Verified fields: David Bryant and Paul F. Tupper. **Diversities and the Geometry
of Hypergraphs**. *Discrete Mathematics & Theoretical Computer Science*
**16**(2), 1–20 (2014).

- Saved `bryant-tupper-2014.txt`, line 1: journal, volume/issue, year, pages;
  lines 6–7: title and authors; line 13: received 21 December 2013, revised
  28 March 2014, accepted 31 March 2014.
- The [journal record](https://dmtcs.episciences.org/articles/2080) confirms
  title, authors, volume 16:2, publication date **23 April 2014**, and DOI.
  Its displayed author name is “Paul Tupper”; the saved article title page
  supplies “Paul F. Tupper.” The page's imported date, 20 December 2013,
  is distinct from its publication date.
- Predecessor `paper/main.tex`, lines 642–645, supplies the same journal
  citation and original journal URL, without the DOI.

Exposure: the saved article is available, but this task inspected bibliographic
material, not its flow–cut proof. The normalization verification belongs to the
separately assigned task.

## Bryant and Tupper open-problem statement

Verified fields: David Bryant and Paul Tupper. **Open Problem Statement: Minimal
Distortion Embeddings of Diversities in ℓ₁**.
[arXiv:1712.01960v1](https://arxiv.org/abs/1712.01960v1), submitted
**5 December 2017**.

- Saved `bryant-tupper-open.txt`, lines 1–4: title, authors, and printed date
  **October 25, 2021**; line 9: **arXiv:1712.01960v1, 5 Dec 2017**.
- The arXiv record gives title and authors and lists only v1, timestamp
  **5 December 2017, 23:02:39 UTC**.
- Predecessor `paper/main.tex`, lines 639–641, cites the 2017 v1 record.
- Requested upper-bound locator: saved text lines 99–108, Section 2.2,
  Theorem 2, states the logarithmic ℓ₁ embedding bound for the Steiner
  diversity of an n-point metric space. This is a source locator, not an
  independent proof check.

Date caveat: the printed 2021 date and arXiv v1's 2017 date do not agree. Both
are recorded exactly; this extraction has not established why. The printed
date is not evidence of a separate arXiv revision or a journal publication.

## Jozefiak and Shepherd

Verified fields: Adam D. Jozefiak and F. Bruce Shepherd. **Diversity Embeddings
and the Hypergraph Sparsest Cut**.
[arXiv:2303.04199v1](https://arxiv.org/abs/2303.04199v1), submitted
**7 March 2023**.

- Saved `jozefiak-shepherd.txt`, line 1: title; line 4: authors; line 13:
  v1 identifier and date.
- The arXiv record confirms these fields and lists only v1, timestamp
  **7 March 2023, 19:37:51 UTC**.
- Predecessor `paper/main.tex`, lines 632–634, is explicitly a v1 citation.
- Saved abstract lines 20–25 give the graph-supply or graph-demand
  logarithmic approximation and the bounded-hyperedge result. Lines 26–35
  distinguish the diameter-diversity result and restricted-query algorithmic
  hardness. These passages were located, not independently audited.

Exposure gap: no revised journal article was verified. The previous
`LITERATURE.md`, line 18, reports a minor revision at DMTCS from an author
page; that historical report does not establish a published journal version.

## OpenAI, planar paper (September 23, 2026)

Verified fields: **OpenAI**. **Planar Graph Metrics Embed into L₁ with Constant
Distortion**. Dated **September 23, 2026**.

- Saved `openai-planar.txt`, lines 1–5: title, corporate author, date;
  lines 8–11: abstract concerns shortest-path metric embeddings on finite
  connected planar graphs with arbitrary positive real edge lengths.
- Saved `openai-treewidth.txt`, lines 1545–1547, identifies this as an
  “OpenAI Math Release preprint” with identifier
  `OAI:Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026`.
- The [official #089 index](https://github.com/openai/math/blob/main/lean/docs/089.md)
  links to the [official planar PDF](https://github.com/openai/math/blob/main/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf).
  Its scope description is explicitly about weighted shortest-path metrics.

Unverified/not supplied: no journal venue, DOI, or arXiv identifier was found
in these inspected bibliographic sources. No such field is inferred.
The preprint's proof and formalization were not audited by this extraction.

## OpenAI, bounded-treewidth paper (September 23, 2026)

Verified fields: **OpenAI**. **L₁ Embeddings of Graphs of Bounded Treewidth**.
Dated **September 23, 2026**.

- Saved `openai-treewidth.txt`, lines 1–4: title, author, date; lines 7–11:
  abstract; lines 46–71: shortest-path metric scope and bag-size convention.
- Saved `openai-planar.txt`, lines 2231–2232, identifies this as an
  “OpenAI Math Release preprint” with identifier
  `OAI:L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026`.
- The [official #089 index](https://github.com/openai/math/blob/main/lean/docs/089.md)
  links to the [official bounded-treewidth PDF](https://github.com/openai/math/blob/main/preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf).
  Its scope is explicitly metric, with a constant depending on the bag-size
  bound. Saved lines 53–54 specify that bag size k means treewidth at most k−1.

Unverified/not supplied: no journal venue, DOI, or arXiv identifier was found
in these inspected bibliographic sources. No such field is inferred.
The preprint's proof and formalization were not audited by this extraction.

## Chakrabarti–Jaffe–Lee–Vincent (2008)

Verified in saved bibliographies: Amit Chakrabarti, Alexander Jaffe,
James R. Lee, and Justin Vincent. **Embeddings of Topological Graphs: Lossy
Invariants, Linearization, and 2-Sums**. In *49th Annual IEEE Symposium on
Foundations of Computer Science* (FOCS 2008), 761–770. IEEE, 2008.

- Saved `openai-planar.txt`, lines 2182–2185: authors, title, conference,
  pages, publisher “IEEE Computer Society,” and year.
- Saved `openai-treewidth.txt`, lines 1484–1487: the same entry and DOI.
- Requested attribution: `openai-planar.txt`, lines 114–117, attributes
  constant distortion for series-parallel metrics to GNRS and the sharp
  upper bound 2 to CJLV, with the matching lower bound assigned to
  Lee–Raghavendra. `openai-treewidth.txt`, lines 98–100, repeats that
  distinction for the treewidth-two case.

Exposure gap: the CJLV primary paper was not retrieved or read. Direct DOI
opening failed; exact-title searches restricted to IEEE Xplore and the IEEE
Computer Society returned no results. A general exact-title metadata search
returned a matching DBLP entry, but it is not a substitute for primary-paper
exposure. This audit verifies the saved citations and attribution as such;
it does not independently verify the sharp-bound theorem.

## Gupta–Newman–Rabinovich–Sinclair (2004)

Verified fields: Anupam Gupta, Ilan Newman, Yuri Rabinovich, and Alistair
Sinclair. **Cuts, Trees and ℓ₁-Embeddings of Graphs**. *Combinatorica*
**24**(2), 233–269 (2004).

- Saved `bryant-tupper-2014.txt`, lines 968–969: authors, title, journal,
  volume/issue, pages, year, DOI.
- Saved `openai-planar.txt`, lines 2197–2199: full author names, journal
  citation, and preliminary version in FOCS 1999, pages 399–408.
- Saved `openai-treewidth.txt`, lines 1515–1517: journal citation and DOI.
- The Springer publisher record for this exact title
  was successfully opened. Its title/author header and “Cite this article”
  section confirm the fields above except the issue number, which is supplied
  by the saved bibliographies. It gives issue date **April 2004**, received
  27 November 2000, revised 7 August 2002, and confirms the FOCS 1999
  preliminary version.

Abstract exposure: item 2 of that publisher abstract reports a logarithmic
lower bound for embedding series-parallel graph metrics into distributions
over dominating tree metrics. Item 1 reports constant distortion into ℓ₁
for series-parallel graphs. The inspected abstract therefore distinguishes
these target classes. This is an abstract-level scope check, not a reading
of the lower-bound proof. No diversity theorem is inferred from it.

Exposure gap: GNRS full text was not read. The earlier saved
`searches/flowcut/FLOWCUT-SCAN.md`, lines 14 and 22, likewise records an
abstract-level GNRS check and full text not performed.

## Predecessor Kline paper

Verified from the predecessor repository: Jeff Kline. **Covering versus hitting
in diversity embeddings: an affine obstruction and matching bounds**.
Version **0.1.0**, **September 13, 2026**.

- Predecessor `paper/main.tex`, lines 15–18: title, author, version, date, DOI.
- Predecessor `CITATION.cff`, lines 4–9: title, author, version, repository URL;
  lines 22–23: DOI and release date.
- Repository URL recorded in that file:
  [jeff-kline/covering-hitting-diversities](https://github.com/jeff-kline/covering-hitting-diversities).
- Predecessor `paper/main.tex`, lines 22–38 and 609–614, and `CITATION.cff`,
  lines 16–21, retain the stated hypergraph scope and unresolved compact-
  realization priority. This extraction does not revise those qualifications.

Exposure gap: attempts to open the DOI and the direct Zenodo record through
the browser failed. The metadata above is verified against local title and
citation files, not independently against the live archive. No journal
publication or peer-review status is inferred.

## Remaining gaps for the owner

The substantive exposure gaps are BT2012 full text, CJLV primary full text,
GNRS full text, any revised journal version of Jozefiak–Shepherd, and a live
archive check for the predecessor. The OpenAI proofs/formalization and all
other cited proofs remain outside this bibliographic assignment. The
Bryant–Tupper open-problem date discrepancy remains unexplained. These gaps
are recorded, not silently filled by extrapolation from abstracts or later
citations. No further searches are proposed or performed here.
