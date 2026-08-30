# W01 — Baseline & Environment

This repository contains the practical evidence for the W01 Baseline & Environment sprint.

## W01 Status

Git/GitHub Module 2 learning and practical recovery work are complete.

### Assessment Results

| Assessment | Result |
|---|---:|
| Practice Assignment | 100% |
| Google Skills Git Merge Lab | 20/20 |
| Module 2 Graded Challenge | 95% |
| Undoing Things Practice | 100% |

## Repository Evidence

The integrated Git lab demonstrates:

- `git mv`
- `git rm`
- `git restore`
- `git restore --staged`
- `git commit --amend`
- branch creation
- divergent branch changes
- intentional merge conflict
- manual conflict resolution
- merge commit creation
- Git graph inspection

Primary merge commit:

`03b6edc` — Complete Git Module 2 recovery and conflict lab

## Documentation

- [Module 2 Evidence](module2-evidence.md)
- [Baseline Assessment](baseline.md)
- [Environment Report](baseline/environment-report.md)
- [W01 Workflow](docs/w01-workflow.md)

## Repository Structure

```text
checks/
├── git-module2-lab/
├── baseline/
│   └── environment-report.md
├── docs/
│   └── w01-workflow.md
├── module2-evidence.md
├── baseline.md
└── README.md


cd /Users/zayar/checks
python3 -m unittest -v
git diff --check
git log --graph --oneline --all -15
git status --short

Reproduction
From the repository root:
cd /Users/zayar/checks
python3 -m unittest -v
git diff --check
git log --graph --oneline --all -15
git status --short
Acceptance Criteria
W01 is ready for closeout when:
1. Tests pass.
2. No unresolved merge-conflict markers remain.
3. Required documentation is non-empty.
4. Git history shows the completed branch and merge exercise.
5. Remote state is recorded.
6. Working tree is clean after the final commit.
Next Step
After W01 is accepted, begin Git Module 3 — Working with Remotes.
Before starting Module 3, first run:
git status --short
Expected time: under one minute.
