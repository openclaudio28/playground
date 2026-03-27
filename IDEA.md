# IDEA.md — Project North Star

## What We're Building

An **autonomous ML research loop** for house price prediction, serving as the first chapter of a broader autoresearch platform.

The system runs without human intervention: agents pick tasks, implement them, open PRs, review each other's work, and continuously enrich the backlog with new ideas.

## The Goal

Build and iteratively improve a house price prediction system where:
- AI agents propose experiments, implement them, and review results
- Each iteration tries to reduce validation RMSE
- Findings are tracked in `EXPERIMENTS.md` for reproducibility
- The backlog captures the next set of ideas to try

## Dataset

**Kaggle House Prices: Advanced Regression Techniques**
- Source: https://www.kaggle.com/c/house-prices-advanced-regression-techniques
- Target: `SalePrice` (log-transformed for modeling)
- Metric: **RMSE on log-transformed SalePrice** (lower is better)
- Split: 80/20 stratified train/validation

## Research Progression

```
Data → EDA → Preprocessing → Baseline → Better Models → Ensembles → AutoML → ?
```

Each step lives as a task in the backlog. Agents move the project forward one PR at a time.

## Success Criteria Per Experiment

An experiment is considered successful if it:
1. Runs end-to-end without errors
2. Logs results to `results/{name}.json`
3. Updates `EXPERIMENTS.md` with the row
4. Either beats or meaningfully informs the best known RMSE

## Future Direction

Once house prices is well-characterized, this same loop applies to:
- Other tabular ML problems (classification, time series)
- LLM training experiments (autoresearch-style, à la Karpathy)
- Any domain where iterative improvement + metric tracking matter

The infrastructure (backlog, PR loop, agent roles) is reusable across projects.
