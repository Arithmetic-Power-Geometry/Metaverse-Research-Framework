# Metric Normalization Protocol

## Principle

Metrics with similar names are not assumed equivalent.

Examples:

- latency may mean radio transmission delay, queueing delay, computation delay, motion-to-photon latency, or total end-to-end latency;
- reliability may mean packet success, deadline satisfaction, task completion, or service availability;
- QoE may be measured by an analytical utility, objective visual metric, or human-subject response;
- semantic quality may be measured by task accuracy, learned similarity, intelligibility, or application-specific utility.

## Normalized metric record

For every extracted metric record:

- metric_name_reported
- normalized_metric_family
- formal_definition
- unit
- aggregation
- evaluation_window
- higher_or_lower_is_better
- layer
- objective_or_constraint
- human_or_objective
- comparable_group
- notes

## Numerical comparison gate

Two reported values may enter the same direct numerical comparison only when:

1. their definitions are materially equivalent;
2. units/normalization are reconcilable;
3. evaluation windows are compatible;
4. workload/scenario is compatible;
5. aggregation/statistical treatment is compatible.

Otherwise they may be compared qualitatively at the method/evidence level but not ranked numerically.
