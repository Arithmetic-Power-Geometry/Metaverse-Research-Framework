# Common Core vs. Scientific Extensions

## Finding

The strongest current candidates do not indicate that one existing algorithm is simply missing. Instead, they expose a benchmark-design problem.

PNE016 and PNE017 share:

- immersive VR;
- edge/device resource constraints;
- rendering decisions;
- wireless/compute coupling;
- latency-sensitive QoE;
- adaptive control.

They diverge in scientifically important ways:

- PNE016 adds dynamic multidimensional resource leasing and economic/resource-utilization structure.
- PNE017 adds queue dynamics, sensor-information age, and explicit safety constraints on motion-to-photon performance.

## Consequence

Flattening both into a single objective would produce an artificial comparison. The defensible design is a common core with optional modules.

## Testable research question

Can representative algorithms retain their reported advantages when evaluated on the same physical workload and resource model while problem-specific leasing and safety modules are activated separately?

This question is benchmarkable and falsifiable. It does not yet justify a new algorithm.

## New-algorithm trigger

A novel method becomes justified only if the common benchmark reveals a reproducible regime in which existing methods fail to handle a combination of constraints or objectives without unacceptable degradation, and that failure cannot be removed by fair retuning or a simpler baseline.
