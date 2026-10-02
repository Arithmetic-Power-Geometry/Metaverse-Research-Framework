# Candidate Benchmark: Dynamic Metaverse Edge Resource Management

Status: **candidate only — not frozen**

## Motivation

The seed literature shows an evolution from wireless latency/reliability optimization toward joint decisions involving computation offloading, bandwidth/power allocation, digital-twin synchronization, adaptive rendering, caching, heterogeneous task classes, and QoE.

The benchmark should test whether methods remain effective when these dimensions are introduced under a common environment.

## Candidate decision layers

- user/channel association
- computation offloading
- compute allocation
- bandwidth allocation
- optional power allocation
- adaptive rendering/resolution
- optional cache placement/replacement
- digital-twin update/synchronization

Not every baseline must control every layer. Capability differences must be made explicit.

## Candidate state variables

- number of users
- task arrival process
- task type
- input/output size
- CPU-cycle demand
- wireless channel condition
- edge CPU availability
- bandwidth availability
- device energy state
- user mobility
- DT age/freshness
- content/resolution demand
- cache state where applicable

## Candidate objectives/metrics

### System metrics

- end-to-end latency
- deadline violation / successful delivery rate
- throughput
- energy consumption / energy efficiency
- compute utilization
- bandwidth utilization
- cache hit rate where applicable

### User-experience metrics

- QoE
- fairness / horizon fairness
- rendering quality or resolution utility

### Learning/algorithm metrics

- convergence behavior
- training sample efficiency
- adaptation after distribution shift
- inference time
- training time
- memory/compute overhead

### Robustness metrics

- increasing user count
- mobility change
- channel distribution shift
- task-mix shift
- DT update delay
- resource scarcity

## Candidate baseline families

- random allocation/offloading
- greedy/heuristic allocation
- classical optimization where tractable
- whale/metaheuristic family for appropriate formulations
- DDPG-style RL
- continual DDPG variants
- actor-critic caching methods
- meta-RL/hierarchical RL when reproducible

## Critical design principle

A method is not declared superior merely because it controls more decision variables. Comparisons should distinguish:

1. objective coverage;
2. information available to the policy;
3. action-space complexity;
4. training/optimization cost;
5. performance under matched scenarios.

## Candidate hidden-gap test

Test the hypothesis:

> Increasing system-model sophistication has not been matched by a common reproducible benchmark that jointly reports user experience, systems performance, adaptation, and computational cost.

The hypothesis is accepted only if the expanded literature and artifact audit support it.
