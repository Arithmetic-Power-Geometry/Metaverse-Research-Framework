# Modular Benchmark Architecture — Candidate

## Rationale

PNE016 and PNE017 share a sufficiently strong immersive-VR/edge-resource core to justify a common benchmark skeleton, but they should not be collapsed into one objective. Dynamic resource leasing and safe motion-to-photon constraints represent distinct scientific extensions.

## Core environment

Common state should support:

- users and session demand;
- wireless bandwidth/channel state;
- edge compute capacity;
- device compute capacity where applicable;
- rendering workload/quality level;
- task/frame arrivals;
- latency components;
- resource utilization.

## Core decisions

- bandwidth/resource assignment;
- compute assignment;
- rendering location/mode/quality;
- optional admission or scheduling decision.

## Core outputs

- end-to-end or motion-to-photon latency;
- latency violation probability;
- visual quality;
- resource utilization;
- device energy/power where modeled;
- QoE components reported separately before any aggregate QoE score.

## Optional module L — Leasing/economics

Represents PNE016-type dynamic GPU/CPU/bandwidth leasing. Adds resource prices, leasing decisions, provider/user utility, and economic cost.

## Optional module S — Safety/queues

Represents PNE017-type safe interactive VR. Adds queue dynamics, sensor-information age, hard/soft MTP constraints, and violation statistics.

## Benchmark principle

The benchmark should compare methods on a shared physical/system core while preserving problem-specific modules. A single weighted score must not erase incompatible objectives.

## Current status

Candidate architecture only. Implementation is blocked until exact equations, parameter ranges, baselines and metric definitions are recovered from primary sources or scientifically reconstructed with transparent provenance.
