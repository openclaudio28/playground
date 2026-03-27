# House Price ML Research — Autonomous Agent Loop

An autonomous ML research system where AI agents iteratively improve a house price prediction model. No human writes code — agents pick tasks, implement them, open PRs, review each other's work, and continuously enrich the backlog with new ideas.

This project is the first chapter of a broader autoresearch platform (inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch)), grounded in a concrete, measurable problem: predicting house prices.

---

## How It Works

Four agent roles run on schedule, fully automated:

```
┌─────────────────────────────────────────────────────────┐
│                    Every 30 minutes                      │
│  PM Agent                                                │
│  - Reads BACKLOG.json                                    │
│  - Counts active tasks (in-progress + review)            │
│  - If < 3 active: assigns next todo tasks, spawns devs   │
└────────────────────┬────────────────────────────────────┘
                     │ spawns
        ┌────────────▼────────────┐
        │   Developer Agent(s)    │
        │   - One agent per task  │
        │   - Creates branch      │
        │   - Implements task     │
        │   - Opens PR            │
        │   - Adds backlog ideas  │
        └────────────┬────────────┘
                     │ opens PR
┌────────────────────▼────────────────────────────────────┐
│                    Every 20 minutes                      │
│  PR Reviewer Agent                                       │
│  - Lists open PRs                                        │
│  - Verifies each acceptance criterion independently      │
│  - Approves & merges OR requests changes                 │
│  - Updates BACKLOG.json                                  │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                    Every 2 hours                         │
│  Repo Reviewer Agent                                     │
│  - Reads repo state, git log, experiments               │
│  - Adds new valuable backlog items (≤5 per pass)        │
│  - Removes stale/duplicate/vague items                   │
└─────────────────────────────────────────────────────────┘
```

---

## Task Lifecycle

```
todo → in-progress → review → done
              ↑_____________↓
         (PR changes requested → back to in-progress)
```

The PM only assigns tasks when `active < 3`, where `active = in-progress + review`.

---

## Backlog Structure

All tasks live in `BACKLOG.json`. Each task has:

```json
{
  "id": "task-001",
  "title": "Data acquisition",
  "description": "What to do and why",
  "acceptanceCriteria": [
    "Specific, verifiable criterion",
    "Another criterion"
  ],
  "priority": "high | medium | low",
  "status": "todo | in-progress | review | done",
  "branch": "task-001-data-acquisition",
  "prNumber": 3,
  "addedBy": "human | pm | developer | reviewer",
  "assignedTo": "developer-agent",
  "createdAt": "2026-03-26T12:00:00Z",
  "startedAt": "2026-03-26T14:30:00Z",
  "completedAt": null
}
```

**Acceptance criteria are mandatory.** A task without verifiable criteria will not be worked on. The PR Reviewer checks each criterion independently before approving.

---

## Git & PR Workflow

All agents follow the rules in `WORKFLOW.md`. Summary:

```
main  (protected — no direct commits)
 └── task-{id}-{slug}     ← developer branch
      └── PR opened        ← title: "[task-001] Data acquisition"
           └── reviewed    ← PR Reviewer approves or requests changes
                └── squash merge → main
```

**Branch naming:** `task-{id}-{short-slug}` (e.g. `task-001-data-acquisition`)

**PR title format:** `[task-{id}] {title}`

**PR body must include:**
- Task description
- Acceptance criteria as a checkbox list
- What was added to the backlog

---

## File Structure

```
playground/
├── IDEA.md              ← Project north star & goals
├── BACKLOG.json         ← All tasks, their status, and history
├── EXPERIMENTS.md       ← Model results table (updated by agents)
│
├── WORKFLOW.md          ← Git/PR rules all agents follow
├── PM.md                ← PM agent instructions
├── DEVELOPER.md         ← Developer agent instructions
├── PR_REVIEWER.md       ← PR Reviewer instructions
├── REPO_REVIEWER.md     ← Repo Reviewer instructions
│
├── src/
│   ├── data/
│   │   └── download.py  ← Dataset download script
│   ├── features.py      ← Shared preprocessing pipeline
│   ├── model_baseline.py
│   ├── model_gbm.py
│   └── compare.py       ← Ranks all experiments by RMSE
│
├── notebooks/
│   └── 01_eda.ipynb     ← Exploratory data analysis
│
├── data/
│   ├── README.md        ← Column documentation
│   └── raw/             ← Downloaded CSVs (gitignored)
│
├── results/
│   ├── baseline.json    ← RMSE, MAE, hyperparams, timestamp
│   └── gbm.json
│
└── tests/
    └── test_features.py
```

---

## Experiments

Results are tracked in `EXPERIMENTS.md` and as individual JSON files in `results/`.

**Metric:** Validation RMSE on log-transformed `SalePrice` (lower is better).

Each `results/*.json` follows this schema:
```json
{
  "experiment": "gbm-v1",
  "model": "LightGBM",
  "val_rmse": 0.1201,
  "val_mae": 0.0843,
  "train_rmse": 0.0921,
  "hyperparams": {"n_estimators": 500, "learning_rate": 0.05},
  "features_used": 220,
  "notes": "one-hot encoded, no feature engineering yet",
  "timestamp": "2026-03-26T15:30:00Z",
  "branch": "task-005-gbm-model"
}
```

---

## Agent Roles — Quick Reference

| Agent | File | Cron | Key Constraint |
|-------|------|------|----------------|
| PM | `PM.md` | Every 30 min | Max 3 active tasks total |
| Developer | `DEVELOPER.md` | Spawned by PM | One task, one branch, one PR |
| PR Reviewer | `PR_REVIEWER.md` | Every 20 min | Never approve without verifying |
| Repo Reviewer | `REPO_REVIEWER.md` | Every 2h | Max 5 additions per pass |

---

## Initial Seed Tasks

The backlog starts with 6 tasks in dependency order:

| ID | Title | Priority |
|----|-------|----------|
| task-001 | Data acquisition | high |
| task-002 | EDA notebook | high |
| task-003 | Preprocessing pipeline | high |
| task-004 | Baseline linear regression | medium |
| task-005 | Gradient boosting model | medium |
| task-006 | Experiment comparison script | low |

From task-004 onwards, agents will extend the backlog autonomously.

---

## Technical Setup

**Git identity (inside sandbox):**
- User: `openclaudio28`
- Email: `openclaudio28@github.com`
- SSH key: `/workspace/openclaw-agent-key-final`
- Remote: `git@github.com:openclaudio28/playground.git` (SSH only, never HTTPS)

**Python tooling:**
- Package manager: `uv`
- Formatter: `black`
- Linter: `ruff`
- Tests: `pytest`
- Python: 3.11+

**Model:** All agents run on `lmstudio/mlx-community/Qwen3.5-4B-MLX-4bit` (local, via LM Studio).

---

## Future Direction

Once house prices is well-characterized (multiple models, hyperparameter tuning, ensembles), the same agent loop applies to:
- Other tabular ML problems
- LLM training experiments (autoresearch-style)
- Any domain with a clear metric to optimize

The infrastructure — backlog, PR loop, four agent roles — is reusable across projects.

---

*This repo is autonomously maintained. Humans seed the backlog and define the north star. Agents do the rest.*
