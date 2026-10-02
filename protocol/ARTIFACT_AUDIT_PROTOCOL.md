# Artifact Audit Protocol

## Purpose
Determine whether published Metaverse algorithms can be independently reused, reproduced, and compared without inferring artifact availability from manuscript prose alone.

## Search order
1. Publisher article page and supplementary material.
2. DOI landing page.
3. Author/project links explicitly cited by the paper.
4. Public code hosts searched by exact title, DOI, algorithm name, and author/title combination.
5. Dataset/testbed links named by the paper.
6. Archived versions/releases when a repository is found.
7. Independent reproduction repositories or benchmark suites.

## Artifact dimensions
Official code; experiment configuration; dependency environment; seeds; datasets/traces/workload generator; preprocessing; baseline implementations; metric implementation; result scripts; container; CI/workflow; versioned release; persistent archive; license; independent reproduction.

## Audit values
confirmed; partial; not_found_in_audit; inaccessible; not_applicable; unresolved.

not_found_in_audit means only that the defined search did not locate the artifact. It must never be rewritten as a claim that the authors did not release it.

## Reproduction classes
R0 paper-only description; R1 partial implementation information; R2 public code but incomplete experiment reconstruction; R3 code plus configuration/data sufficient for substantial rerun; R4 automated environment/workflow reproducing artifacts; R5 independently reproduced/extended under documented protocol.

These classes describe artifact support, not scientific quality.
