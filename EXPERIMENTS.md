# EXPERIMENTS.md — Results Tracker

All model experiments logged here. Updated by developer agents after each task that produces a model result.

## How to Add a Row

After training a model:
1. Log full results to `results/{experiment_name}.json`
2. Add a row to the table below (newest at top)
3. Commit with: `results: {model} RMSE={value}`

## Results Table

| # | Model | Branch | Val RMSE | Val MAE | Notes | Date |
|---|-------|--------|----------|---------|-------|------|
| — | — | — | — | — | No experiments yet | — |

## Best Known RMSE

**Current best:** N/A — no experiments run yet

Update this line whenever a new best is achieved.

---

## Result File Format

Each `results/{name}.json` should contain at minimum:

```json
{
  "experiment": "name",
  "model": "LinearRegression",
  "val_rmse": 0.1423,
  "val_mae": 0.0981,
  "train_rmse": 0.1387,
  "hyperparams": {},
  "features_used": 80,
  "notes": "baseline, no feature engineering",
  "timestamp": "2026-03-26T12:00:00Z",
  "branch": "task-004-baseline-model"
}
```
