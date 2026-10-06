# P1 prospective search — execution status (2026-10-06)

## Purpose
Close the COMST search-reproducibility objection without reconstructing unavailable historical counts.

## What was executed in this environment
A prospective public-web, publisher-targeted validation search was run on 2026-10-06 across discoverable official publisher/index pages for:
- IEEE Xplore
- ACM Digital Library
- ScienceDirect / Elsevier
- Springer Nature

The search confirms that relevant 2023–2026 literature exists across the intended technical strata, including semantic communication, digital twins, edge/MEC, security/privacy, federated learning, and Metaverse systems.

## Critical boundary
This environment does **not** expose authenticated Scopus or Web of Science result sessions, nor does general web search reproduce IEEE Xplore/ACM database result counts. Therefore:
- returned_n for Scopus/WoS/IEEE/ACM is NOT reported;
- no PRISMA identification count is invented;
- no database-specific deduplication count is invented;
- no final PRISMA diagram is claimed.

P1 is therefore **protocol-complete and public-web validation-executed, but formal database-count execution remains externally blocked**.

## Formal P1 completion criterion
P1 becomes complete only after exact queries in FORMAL_DATABASE_QUERY_PROTOCOL.md are executed inside IEEE Xplore, Scopus, Web of Science and ACM DL and their exports/counts are deposited here. The PRISMA generator can then calculate the flow from the ledgers.
