# Search Strategy

## Coverage objective

Retrieve foundational work and current research relevant to the networked Metaverse through the search freeze date, with explicit backward and forward snowballing for influential studies and closest surveys.

## Source families

Primary scholarly discovery should include, where accessible:

- IEEE Xplore
- ACM Digital Library
- Scopus
- Web of Science
- ScienceDirect
- SpringerLink
- Wiley
- major publisher databases relevant to communications, networking, computing, HCI, security, and digital twins

Crossref, DBLP, OpenAlex, Google Scholar, and publisher metadata may be used for metadata verification and citation chasing. Preprints may be retained for frontier surveillance but must be labeled and must not silently replace a peer-reviewed version.

## Search blocks

### S0 — Core Metaverse

`("metaverse" OR "networked metaverse" OR "mobile metaverse" OR "industrial metaverse")`

### S1 — Communications and networking

`S0 AND (communication* OR network* OR wireless OR 5G OR 6G OR B5G OR "beyond 5G" OR latency OR bandwidth OR QoS OR QoE)`

### S2 — Edge/cloud/resource management

`S0 AND ("edge computing" OR MEC OR fog OR cloud OR offload* OR schedul* OR "resource allocation" OR placement OR orchestrat*)`

### S3 — XR and immersive media

`S0 AND ("extended reality" OR XR OR "virtual reality" OR VR OR "augmented reality" OR AR OR "mixed reality" OR holograph* OR rendering OR streaming)`

### S4 — Digital twins and cyber-physical systems

`S0 AND ("digital twin*" OR "cyber physical" OR CPS OR IoT OR "Internet of Things")`

### S5 — AI and intelligent systems

`S0 AND ("artificial intelligence" OR AI OR "machine learning" OR "deep learning" OR "federated learning" OR "distributed learning" OR "generative AI" OR LLM OR agent*)`

### S6 — Semantic communications

`S0 AND ("semantic communication*" OR "goal-oriented communication*" OR "task-oriented communication*")`

### S7 — Security/privacy/identity/trust

`S0 AND (security OR privacy OR authentication OR identity OR trust OR attack* OR threat* OR intrusion OR anomaly OR biometric*)`

### S8 — Blockchain/Web3

`S0 AND (blockchain OR Web3 OR "Web 3.0" OR NFT OR "non-fungible token*" OR decentralized)`

### S9 — Interoperability and standards

`S0 AND (interoperab* OR standard* OR portability OR migration OR "cross-platform" OR "cross-world" OR semantic*)`

### S10 — Sustainability

`S0 AND (sustainab* OR energy OR carbon OR "energy efficiency" OR green)`

### S11 — Algorithms and benchmarking

`S0 AND (algorithm* OR optim* OR heuristic OR metaheuristic OR benchmark* OR dataset* OR simulator OR testbed OR experiment*)`

### S12 — Review surveillance

`S0 AND (survey OR review OR "systematic literature review" OR taxonomy OR tutorial OR bibliometric)`

## Time handling

No lower year boundary is imposed on foundational searches. The year of the term's literary origin is not treated as the beginning of technical Metaverse research. Search results are classified into:

- conceptual/foundational precursors;
- early virtual-world and 3-D Internet work;
- modern Metaverse research;
- current frontier work.

## Search freeze

The final search freeze date must be recorded before analysis is frozen. Any later studies are logged separately as post-freeze surveillance.

## Snowballing

For each closest survey and each influential technical study:

1. inspect references for foundational and missed studies;
2. inspect citing literature for newer developments;
3. identify peer-reviewed versions of relevant preprints;
4. inspect datasets, code repositories, standards, and testbeds explicitly referenced by the study.

## Deduplication

Primary key preference:

1. DOI
2. other persistent identifier
3. normalized title + first author + year

Conference-to-journal extensions remain separate records but are linked.

## Verification

Bibliographic facts should be verified against DOI/publisher metadata when possible. Search-engine snippets are discovery evidence, not final bibliographic authority.
