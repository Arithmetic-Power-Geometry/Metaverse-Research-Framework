# Network/Edge Candidate Gap Revision — Batch 02

## Why the hypothesis changed

The expanded primary-study search found substantial contrary evidence to broad claims that Metaverse resource-allocation research is single-objective or lacks algorithm comparison.

Examples include:

- federated-learning resource allocation jointly considering energy, completion time, and model accuracy;
- anti-jamming resource allocation considering latency, energy, QoE, and disruption risk;
- O-RAN federated RL combining energy efficiency, video quality, communication delay, and computation delay;
- cooperative VR rendering leasing GPU, CPU, and outbound bandwidth with QoE and utilization objectives;
- safe RL for interactive VR under a motion-to-photon constraint, sensor-information age, and device-power objectives;
- an existing 2024 survey that compares 35 strategies and benchmarks 19 algorithms.

## Revised CG-NE-01

**Old candidate:** the field lacks common benchmarking as system models become more sophisticated.

**Revised candidate:**

> Despite increasingly rich within-paper evaluation and at least one substantial cross-algorithm benchmark, it remains to be tested whether independently reusable benchmark environments, workloads, metric definitions, configurations, and implementations permit cross-paper reproduction of newer heterogeneous formulations.

This is intentionally narrower.

## What would invalidate the revised candidate

The gap should be invalidated if the audit finds one or more maintained benchmark suites that:

1. expose shared workloads/scenarios;
2. implement representative algorithm families;
3. normalize metric definitions;
4. preserve environment/configuration details;
5. cover newer multi-objective formulations;
6. support independent reproduction or extension.

## Next audit

Search specifically for:

- public benchmark repositories;
- code supplements for PNE011–PNE019;
- datasets/traces used by these studies;
- simulator/testbed reuse across papers;
- shared definitions of QoE, MTP latency, energy, fairness, accuracy, and resource utilization.

No paper-level gap claim is promoted yet.
