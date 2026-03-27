# WORKFLOW.md — Agent Git & PR Rules

Ground truth for how all agents interact with this repository. Read this before touching anything.

---

## Branch Naming

```
task-{task-id}-{short-slug}
```

The `task-id` is the short ID from `BACKLOG.json` (e.g. `task-001`).
The slug is the first 3–4 words of the task title in kebab-case.

**Examples:**
- `task-001-data-acquisition`
- `task-003-preprocessing-pipeline`
- `task-005-gbm-model`

---

## Developer Flow (step by step)

```bash
# 1. Always start from a clean main
git checkout main
git pull origin main

# 2. Create your task branch
git checkout -b task-{id}-{slug}

# 3. Implement (commit often, clear messages)
git add <files>
git commit -m "feat: ..."

# 4. When done, push
git push -u origin task-{id}-{slug}

# 5. Open PR
gh pr create \
  --base main \
  --head task-{id}-{slug} \
  --title "[task-{id}] {title}" \
  --body "$(cat <<'EOF'
## Task
{description}

## Acceptance Criteria
- [ ] criterion 1
- [ ] criterion 2
- [ ] criterion 3

## Backlog Additions
- {new item added to backlog}

## Notes
{anything the reviewer should know}
EOF
)"
```

---

## After Opening the PR

Update `BACKLOG.json` on your branch:
- `status` → `"review"`
- `branch` → `"task-{id}-{slug}"`
- `prNumber` → the PR number returned by `gh pr create`

Then commit and push:
```bash
git add BACKLOG.json
git commit -m "backlog: task-{id} → review, PR #{prNumber}"
git push
```

---

## Backlog Contributions (Developer Duty)

When you finish a task, you **must** add 1–3 future improvement ideas to `BACKLOG.json`:
- `status: "todo"`
- `addedBy: "developer"`
- `priority: "low"` (unless clearly important)
- Include specific `acceptanceCriteria`

These go on your branch alongside the code, committed together.

---

## PR Reviewer Flow

```bash
# List open PRs
gh pr list --base main --state open

# Check out to verify
gh pr checkout {pr_number}

# Run the code, verify each acceptance criterion

# Approve & merge (if all criteria met)
gh pr review {pr_number} --approve
gh pr merge {pr_number} --squash --delete-branch

# OR: Request changes (if criteria not met)
gh pr review {pr_number} --request-changes --body "Specific issue: ..."
```

After merging → update `BACKLOG.json` on main: `status: "done"`, `completedAt: now`.
After requesting changes → update `BACKLOG.json` on main: `status: "in-progress"`.

---

## Commit Message Format

```
{type}: {what}
```

Types:
- `feat` — new functionality
- `fix` — bug fix
- `data` — data files or scripts
- `results` — experiment output
- `backlog` — backlog-only changes
- `docs` — documentation
- `chore` — tooling, config

**Examples:**
```
feat: add preprocessing pipeline with median imputation
results: baseline linear regression RMSE=0.1423
backlog: add polynomial features idea from developer
fix: handle NaN in LotFrontage before scaling
```

---

## Golden Rules

1. **NEVER commit directly to main**
2. **One task = one branch = one PR**
3. **Verify every acceptance criterion before opening a PR**
4. **SSH remote only**: `git@github.com:openclaudio28/playground.git`
5. **Do not modify `.gitconfig`** — git is pre-configured, leave it
6. If git push fails, report the error. Do not reconfigure git.
