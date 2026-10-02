# Candidate Gaps — Evidence Tracking

These are hypotheses under active testing. None should be described as a confirmed literature gap until its validation checklist is complete.

## CG-NE-01 — Benchmark standardization lag

**Hypothesis:** Metaverse edge/resource-management models increasingly combine wireless, compute, digital-twin, rendering, caching, mobility, and heterogeneous task decisions, but the field lacks a common reproducible benchmark that allows these methods to be compared under matched conditions.

**Current support:** Seed studies use materially different objectives, decision spaces, and evaluation setups.

**Required validation:**
- expand primary-study corpus;
- audit public code/data;
- inspect the 2024 resource-allocation survey's 19-algorithm benchmark;
- identify any later common benchmark/testbed;
- compare metric definitions and environment assumptions;
- search specifically for reproducibility/benchmark papers.

**Status:** open.

## CG-NE-02 — Adaptation cost is under-characterized

**Hypothesis:** Dynamic/time-varying methods report adaptation benefits but do not consistently expose adaptation cost, retraining cost, communication overhead, inference overhead, or sample efficiency under comparable distribution shifts.

**Current support:** Continual/meta-RL studies emphasize adaptation; standardized adaptation-cost reporting has not yet been established in the seed set.

**Required validation:** full-text metric extraction across dynamic RL/meta-RL studies.

**Status:** open.

## CG-NE-03 — Cross-objective evaluation

**Hypothesis:** Latency, QoE, reliability, energy, synchronization freshness, fairness, caching efficiency, and learning overhead are frequently optimized/evaluated in different subsets, limiting evidence about Pareto trade-offs.

**Required validation:** construct metric-coverage matrix over expanded corpus and identify studies with genuine multi-objective/Pareto analysis.

**Status:** open.

## CG-NE-04 — Reproducibility deficit

**Hypothesis:** A meaningful portion of Metaverse resource-management algorithms cannot be independently reproduced from public code/data/configuration.

**Current support:** Initial targeted code searches did not confirm study-specific public implementations for several high-value seed studies; this is insufficient for a field-wide claim.

**Required validation:** systematic repository/artifact search and author-supplement inspection for every benchmark candidate.

**Status:** open.
