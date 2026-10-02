# Cross-Layer Benchmark Blueprint

Status: design hypothesis; not frozen.

## Purpose

Create a common experimental interface linking network conditions, edge resources, XR fidelity, semantic/task utility, and digital-twin freshness.

## Layer A — Network

Inputs:
- channel state
- bandwidth
- packet loss/error model
- mobility
- uplink/downlink capacity

Outputs:
- rate
- latency
- reliability
- communication cost

## Layer B — Edge/cloud

Inputs:
- compute capacity
- queue/load
- task demand
- cache state
- placement/offloading decision

Outputs:
- compute delay
- energy
- utilization
- placement/offloading cost

## Layer C — Semantic representation

Inputs:
- modality
- source data
- task objective
- model/codec

Outputs:
- representation size
- semantic fidelity
- task success
- encoder/decoder inference cost

## Layer D — XR/application

Inputs:
- viewport/scene/task
- rendering quality
- delivered semantic/content state

Outputs:
- QoE
- rendering quality
- motion-to-photon/application latency
- successful interaction/task completion

## Layer E — Physical-virtual synchronization

Inputs:
- sensing/update process
- network/compute delays
- DT update policy

Outputs:
- age/freshness
- synchronization error
- downstream task impact

## Experimental principle

Methods are evaluated at the layer they actually control, while the benchmark records downstream effects across all layers. This avoids claiming that a network algorithm, semantic codec, and resource allocator solve the same optimization problem.

## Candidate experiment families

1. network/resource allocation with fixed conventional codec;
2. network/resource allocation with semantic representation;
3. adaptive XR fidelity under network/edge constraints;
4. DT update scheduling under network/edge constraints;
5. joint semantic + edge adaptation under distribution shift.

## Required outputs

Each run must produce machine-readable per-layer metrics plus scenario/configuration metadata.
