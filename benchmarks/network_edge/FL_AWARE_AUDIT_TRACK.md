# FL-Aware Benchmark Audit Track

## Candidate studies

- PNE011: Resource Allocation of Federated Learning for the Metaverse With Mobile Augmented Reality.
- PNE015: Federated Reinforcement Learning-Based Resource Allocation in O-RAN Slicing for Metaverse.

## Why audit this pair

Both couple distributed/federated learning with wireless and computing resource allocation and experience-related outcomes. Their algorithmic approaches differ, which may provide a useful classical-optimization versus learning-based comparison if the underlying scenario can be normalized without distorting either study.

## Required extraction before implementation

- exact learning objective and aggregation assumptions;
- local/global training schedule;
- communication payload/update size;
- bandwidth, power, CPU/PRB constraints;
- delay decomposition;
- energy model;
- learning-quality/accuracy metric;
- video/QoE metric;
- baseline algorithms;
- parameter table;
- training/evaluation repetitions;
- code/data availability.

## Guardrail

No direct numerical comparison is permitted until the learning task, communication workload, resource model and metrics are compatible. A common label such as federated learning is not sufficient evidence of comparability.
