# AEYA
tunes do travel AI preproduction

## Workflows

`content_orchestration_core.json` orchestrates the creation and review of
scripts and videos. It calls the `ensemble-review-subflow` to obtain quality
checks from multiple language models.

### Ensemble Review Subflow

The ensemble subflow queries three Hugging Face hosted models and aggregates
their responses. The aggregation logic normalizes confidence scores, ignores
results from failed requests, and lowers the risk threshold to `0.6`.
