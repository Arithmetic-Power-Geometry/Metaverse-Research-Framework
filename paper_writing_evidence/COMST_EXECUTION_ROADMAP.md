# COMST Execution Roadmap

Primary target: **IEEE Communications Surveys & Tutorials (COMST)**.

Current working readiness: approximately **55–60%**. Manuscript writing is intentionally deferred until evidence saturation, reproducibility/benchmark decisions, validated gaps, final artifacts, and a COMST non-redundancy gate are complete.

## Sequential master queue

| Run | Work package | Required output | Priority |
|---|---|---|---|
| RUN 01 | CI/repository integrity and latest workflow verification | Green CI + integrity log | BLOCKER |
| RUN 02 | Closest-review saturation expansion | Expanded closest-review matrix + novelty-overlap map | CRITICAL |
| RUN 03 | Foundations/history deep mining | Verified historical timeline register | HIGH |
| RUN 04 | 5G/6G/network primary saturation | Network evidence register + saturation log | HIGH |
| RUN 05 | XR streaming/rendering saturation | XR algorithm/metric/workload matrix | HIGH |
| RUN 06 | Edge/cloud/resource saturation | Expanded primary corpus + dedup links | HIGH |
| RUN 07 | Digital-twin saturation | DT evidence + metric matrix | HIGH |
| RUN 08 | Semantic-communications saturation | Semantic baseline + metric matrix | HIGH |
| RUN 09 | AI/ML saturation | AI role × problem × evidence matrix | HIGH |
| RUN 10 | GenAI/autonomous-agent saturation | GenAI/agent evidence register | MEDIUM-HIGH |
| RUN 11 | Security/privacy/identity/trust saturation | Threat–control–metric–evidence matrix | HIGH |
| RUN 12 | Interoperability/standards saturation | Verified standards matrix | HIGH |
| RUN 13 | Sustainability deep mining | Sustainability measurement register | MEDIUM-HIGH |
| RUN 14 | Applications/deployment evidence | Deployment maturity corpus | HIGH |
| RUN 15 | Datasets/testbeds/platforms | Dataset/testbed landscape | CRITICAL |
| RUN 16 | 2024 19-algorithm benchmark dissection | Benchmark reconstruction dossier | CRITICAL |
| RUN 17 | PNE011/PNE015 FL-aware source reconstruction | FL-aware implementation gate | CRITICAL |
| RUN 18 | PNE016 source reconstruction | PNE016 implementation gate | CRITICAL |
| RUN 19 | PNE017 source reconstruction | Resolve SR01–SR18 + fidelity decision | CRITICAL |
| RUN 20 | Artifact/reproducibility audit | Reproducibility landscape dataset | CRITICAL |
| RUN 21 | Search saturation + dedup freeze | Final included corpus + flow counts | BLOCKER |
| RUN 22 | Gap validation freeze | Validated gap register | BLOCKER |
| RUN 23 | Benchmark Go/No-Go | Frozen benchmark protocol | BLOCKER |
| RUN 24 | Baseline implementation/reproduction | Reproduction results + logs | CONDITIONAL |
| RUN 25 | Sensitivity/statistics/failure frontier | Failure-frontier evidence | CONDITIONAL |
| RUN 26 | Novel algorithm decision | Algorithm Go/No-Go memo | CONDITIONAL |
| RUN 27 | Novel method evaluation if approved | Experimental evidence package | CONDITIONAL |
| RUN 28 | Generate final manuscript artifacts | Final figures/tables + provenance | BLOCKER |
| RUN 29 | COMST novelty/non-redundancy gate | COMST Go/No-Go report | BLOCKER |
| RUN 30 | Evidence freeze | Versioned evidence release | BLOCKER |
| RUN 31 | Write COMST manuscript | 28–30 page submission-ready manuscript | FINAL |
| RUN 32 | Pre-submission reviewer audit | Final submission gate | FINAL |

## Current contribution candidate

The review is being developed around an evidence-centered and reproducibility-aware chain:

**Problem → Algorithm → Workload/Dataset → Baseline → Metric → Environment → Evidence → Reproducibility → Deployment → Validated Gap**

Candidate gaps are not accepted directly:

**Candidate Gap → Contrary-Evidence Search → Validation/Refutation → Final Gap**

No claim of being the first such review is permitted until RUN 29.

## Current corpus anchors

- Network/edge/resource stream: PNE001–PNE019.
- Closest-review register: R001–R015.
- Separate streams exist for 6G/XR/semantic communications, security/interoperability/standards, AI/GenAI/agents, and sustainability/deployment.
- The 2024 resource-allocation review is a critical contrary-evidence anchor because it reports 35 strategies and a 19-algorithm benchmark.
- PNE011/PNE015, PNE016, and PNE017 are active source-reconstruction/benchmark candidates.

## Run discipline

Each future “do next” instruction advances to the first unfinished run. Every run must save structured outputs, commit them, verify critical paths, update the run ledger, and return the GitHub links.

A new algorithm is **conditional**, not mandatory for COMST. It is developed only if a common-protocol reproduction exposes a defensible unresolved failure frontier.
