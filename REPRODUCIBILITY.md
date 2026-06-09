# Reproducibility Notes

## Scope

This folder contains a sanitized public summary pack for the Remaining Five-System Multi-Axis Seal Model.

It is intended for GitHub / external review as a public evidence-index pack.

## Final framing

Strong multi-axis structure, not proof of tampering or attribution.

## Public verification level

This public pack allows reviewers to inspect:

- Stage-level summary outputs
- Claim boundaries
- Sanitized CSV / JSON / TXT / MD files
- SHA-256 inventory for the included public files
- Skipped-file log
- Copy-error log
- Public-pack verification script

## What can be verified publicly

Reviewers can verify:

1. The included public files are stable by checking PACK_INVENTORY.csv.
2. The included file hashes match the public files.
3. Raw iOS logs and backup payload bodies are not included.
4. The public claim boundary avoids unsupported conclusions.
5. The staged outputs are presented as structural review summaries, not attribution proof.

## What cannot be fully reproduced from this public pack

This public pack does not include:

- Raw iOS logs
- Raw Manifest.db bodies
- Snapshot bodies
- 00-ff backup payload bodies
- Large context part files
- Private account / OTP / financial / message / screenshot material

Therefore, this pack is not a raw full-reproduction forensic archive.

## Verification script

The file verify_remaining_five_public_pack.py can be used after cloning or downloading this repository folder.

It checks:

- SHA-256 consistency against PACK_INVENTORY.csv
- Dangerous raw file extensions
- Raw / payload / context filename patterns
- Files larger than 2 MB

Run:

    run_verify_remaining_five_public_pack.bat

or:

    python verify_remaining_five_public_pack.py

The script outputs:

    VERIFY_REPORT.json
    VERIFY_REPORT.csv

## Claim boundary

Supported:

- Strong multi-axis structure
- Remaining five-system review completed
- 12G as core device, if present in stage summaries
- 15G / mini1 as supporting axes, if present in stage summaries
- Backup / Manifest structural axis, not tampering proof
- Evidence pressure candidates, not suppression proof
- Normal explanations are stressed

Not supported:

- Attack proven
- Apple involvement proven
- hidden MDM proven
- server-side control proven
- tampering proven
- attacker intent proven