# Coder B validation status — 2026-10-06

## Repository inspection
The folder contains an uploaded binary workbook named `Coder_B_50_Papers_Anand_Approved.xlsx` and a README describing the intended 50-record (25%) stratified independent-coder sample.

## Binary integrity check
The workbook bytes currently stored in GitHub are not a valid complete XLSX package. ZIP integrity inspection reports a missing-byte condition and overlapping components, and the spreadsheet parser rejects the file as corrupted data.

Because the uploaded workbook cannot be reliably parsed, **no coder judgments, human-verification flags, initials, dates, agreement values, Cohen kappa, or weighted kappa are accepted from this file yet.**

The existing README is also stale: it still says the folder is intentionally unfilled, despite the presence of the uploaded workbook.

## Required repair
Re-upload/export the approved Coder B workbook as a clean XLSX file. Preserve the 50 sampled record IDs and the genuine human Coder B labels. Do not overwrite the raw pre-adjudication labels with consensus values.

After a readable workbook is available, the next validation step is:
1. confirm exactly 50 unique sampled records and the declared stratified allocation;
2. verify coder initials/date/human-verification fields;
3. freeze Coder B labels;
4. align against the independently frozen Coder A labels;
5. compute raw agreement, Cohen's kappa for categorical fields, and weighted kappa for ordinal fields;
6. preserve a separate disagreement/adjudication file.

## Current P2 status
**DATA PRESENT BUT NOT VALIDATED — uploaded XLSX is corrupted/unreadable.**

No kappa value is reported.
