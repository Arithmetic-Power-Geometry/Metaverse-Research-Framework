# Benchmark Readiness Decision

## Purpose

Select the first executable benchmark by evidence completeness rather than by novelty preference.

## Current result

The immersive-VR edge-resource family remains the strongest common scientific core, but faithful execution is blocked by incomplete source recovery. PNE017 and PNE016 are therefore not promoted to executable benchmarks.

The federated-learning-aware family (PNE011/PNE015) is the next candidate for parallel audit because it has a clear shared optimization theme and multiple primary studies. This does not mean it is more novel; it means it may provide an alternate route to an executable common protocol if its mathematical and experimental specification is more accessible.

## Selection rule

A family is promoted from candidate to implementation-ready only when:

1. the problem and decision variables are explicitly specified;
2. metric definitions are recoverable;
3. scenario parameters are documented or transparently benchmark-defined;
4. at least two meaningful baselines can be reconstructed;
5. unresolved assumptions are isolated rather than hidden;
6. the comparison does not require changing the scientific meaning of the source methods.

## Parallel strategy

- Track A: continue PNE017/PNE016 source recovery.
- Track B: audit PNE011/PNE015 for a reproducible FL-aware common core.
- Track C: finish the 2024 19-algorithm benchmark artifact audit.
- Track D: continue broad domain mining so experimental work does not bias the review toward resource allocation.

The first track to satisfy the implementation gate becomes the initial executable benchmark.
