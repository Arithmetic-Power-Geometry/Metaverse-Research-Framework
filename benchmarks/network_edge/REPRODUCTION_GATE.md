# Reproduction Gate

No new algorithm will be designed until this gate is passed.

## A — Existing benchmark reuse
Determine whether an existing public benchmark can represent the target problem with acceptable fidelity. If yes, extend/reuse it rather than create a competing benchmark without need.

## B — Baseline reconstruction
At least three scientifically relevant baseline families must be reproducible under a common protocol: a classical/optimization baseline, a representative RL/DRL baseline, and where applicable a newer adaptive, multi-agent, meta, or safe method.

## C — Metric compatibility
Numerical comparisons require compatible definitions of latency, energy/power, QoE/utility, visual quality, reliability/risk, resource utilization, and convergence/sample efficiency where relevant.

## D — Scenario compatibility
Document workload, channel/network model, compute capacities, state/action spaces, constraints, randomization, and evaluation horizon.

## E — Failure condition
A new method is considered only after a measurable failure or trade-off of existing reproducible baselines is demonstrated under the common protocol.

Passing the gate establishes experimental need; it does not guarantee novelty.
