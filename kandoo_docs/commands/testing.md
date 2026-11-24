---
name: testing
description: Define, implement and rehearse the testing procedures for this Kandoo.
---

# /testing

Write the accepted test procedure to template/docs/constitution/testing.md and record its review in the current dossier. For each stage specify representative inputs, expected observable result, responsible checker, commands or human inspection, failure record, retry path and acceptance evidence. Identify which checks run on every take, at stage close, and before sealing. Distinguish human judgment from machine verification.

Implement fixtures and executable checks for shared code where applicable. Preserve previous prompts or output references in docs/versions/VERSION/takes/ with a take number, defect, change and result. Accept defects via chat or file while the stage is open. Retest the affected output and record evidence before advancing. If the defect, new asset or correction changes future projects, write a method note immediately. Exercise one failed and corrected example and verify which commands unlock. Hand off to /apply with test commands and evidence.

At every automated test record the result. For every failure and at closure of each /issue record expected and observed behavior, revision, evidence, origin (project, reusable method, or undetermined), repair and retest. Compare the installed procedure or template to the failing artifact before classifying. Write one sanitized method note for a repeatable defect, linking the local record; for undetermined origin record the missing check. Human testers may report in the current step or invoke /method-note at any time. Reuse the same note on retry.
