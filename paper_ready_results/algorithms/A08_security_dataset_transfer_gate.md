# Algorithm A08 — Security Dataset Transfer Gate

Input: security model study s and target Metaverse claim c.

1. Record exact dataset, version and provenance.
2. Record traffic-generation environment/topology.
3. Record attack families and benign behavior.
4. Record sampling, balancing, feature selection and preprocessing.
5. Record train/test split and leakage controls.
6. Record target Metaverse workload claimed by the paper.
7. Compare device, protocol, traffic, temporal and adversary distributions.
8. If target workload is not represented, label evidence BENCHMARK_SECURITY rather than OPERATIONAL_METAVERSE_SECURITY.
9. Require external/cross-dataset or native-testbed evidence before stronger transfer claims.
10. Preserve accuracy/F1 only with dataset and evaluation protocol attached.

Output: transfer class and permitted manuscript wording.
