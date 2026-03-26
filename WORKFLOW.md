# Git Workflow - Feature Branch Pattern

This document describes the standard workflow for developing features in this repository.

## ⚠️ IMPORTANT: NEVER COMMIT TO MAIN

**NEVER commit directly to the main branch.** Always work on feature branches.

- **Always create a feature branch first**
- **Always merge into main, not the other way around**
- **Never force-push to main** (use `git pull` first if needed)
- **Main is production-ready** - protect it at all costs

### The Golden Rule
```bash
# ❌ DON'T do this:
git checkout main
git add .
git commit -m "Quick fix"

# ✅ DO this instead:
git checkout -b feature/<feature-name>
# ... make changes ...
git push origin feature/<feature-name>
# Create PR on GitHub
# Merge via PR, not direct commit
```

### Branch Protection Rules
- **Main branch**: Protected, requires PR review, no force pushes
- **Feature branches**: Can be force-pushed, but always merge into main
- **Production**: Never push directly to production - always through main

### Safe Commands
```bash
# Create feature branch (safe)
git checkout -b feature/<feature-name>

# Work on feature
git add .
git commit -m "Describe change"

# Push feature branch (safe)
git push origin feature/<feature-name>

# Merge into main (safe)
git merge main
```

### Unsafe Commands
```bash
# ❌ NEVER do this:
git checkout main
git add .
git commit -m "Quick fix"
git push origin main
```

## 📝 Learnings & Instructions

### Git Push/Pull Issues
- **Always pull before pushing** - branches may have diverged
- **Use `git pull origin main` or `git merge origin/main`**
- **If branches have unrelated histories:**
  - Use `git config advice.mergeUnrelatedHistories always` to allow merges
  - Or reset local branch: `git reset --hard origin/main`
- **Pass `--no-rebase` flag if needed**: `git pull --no-rebase origin main`

### Authentication Methods
- **HTTPS URL format**: `https://github.com/openclaudio28/repo.git`
- **SSH format**: `git@github.com:openclaudio28/repo.git`
- **Credential helpers**: Configure `git config --global credential.helper osxkeychain`
- **HTTPS URL substitution**: `git config --global url."https://github.com/".insteadOf ssh://`

### SSH Key Management
- **Generate with passphrase**: `ssh-keygen -t ed25519 -f keyfile -C "email"`
- **Enter passphrase when prompted** (GitHub will ask for it)
- **Keep private key secure** - never commit the `.pub` file
- **Use HTTPS instead of SSH** if SSH authentication fails

### Workflow Iteration
- **When you see an error, keep iterating** - try different approaches
- **Save all learnings** - document what worked and what didn't
- **Test connections** - use `git remote -v` to verify remote URL
- **Check status** - always check `git status` before committing

### Memory & Documentation
- **Include workflow in memory files** - always loaded with you
- **Update WORKFLOW.md** with new learnings
- **Document authentication methods** - what works and what doesn't
- **Track git branch synchronization** - maintain local/remote branches

### Core Principles
- **Be genuinely helpful, not performatively helpful**
- **Actions speak louder than filler words**
- **Have opinions** - be direct, no-nonsense
- **Remember you're a guest** - treat the workspace with respect

---

*This workflow embodies the philosophy: Be genuinely helpful, not performatively helpful. Actions speak louder than filler words. When you see an error, always keep iterating until fixing it.*
