# Roadmap

This roadmap tracks the project as a decision-intelligence platform rather than a single-purpose analysis script.

## Phase 1: Data Ingestion

- Harvest public provider feeds.
- Detect accepted source contexts before fetching event pages.
- Extract only relevant structured tables.
- Store raw and normalized records separately.

## Phase 2: Incremental Synchronization

- Add local cache manifests.
- Avoid redundant network calls.
- Track source timestamps and content hashes.
- Recover gracefully from partial fetch failures.

## Phase 3: Normalization

- Convert provider-specific fields into stable internal schemas.
- Standardize entity names, event identifiers, and metric labels.
- Validate required fields before evaluation.

## Phase 4: Entity Resolution

- Align duplicate entities across providers.
- Build confidence scores for entity matches.
- Preserve aliases and source-specific names.

## Phase 5: Evidence Graph

- Represent entities, events, metrics, providers, and outcomes as connected evidence.
- Track why a result was retained, rejected, or downgraded.
- Support explainable diagnostics from the graph.

## Phase 6: Evaluation Engine

- Move thresholds into configurable rule files.
- Add rule groups, warnings, and severity levels.
- Keep evaluation offline and reproducible.

## Phase 7: Feedback Learning

- Add verified outcome ingestion.
- Compare prior evaluations with observed results.
- Identify rule drift, weak signals, and recurring failure modes.

## Phase 8: Reporting

- Generate compact tables for operators.
- Export JSON and CSV outputs.
- Add audit reports for rejected records and failed rules.
