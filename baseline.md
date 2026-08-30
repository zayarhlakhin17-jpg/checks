# W01 Baseline Assessment

## Sprint

**W01 — Baseline & Environment**

Purpose: establish my current development-environment and Git baseline before progressing to more advanced software-engineering work.

## Baseline Summary

| Area | Current Level | Decision |
|---|---|---|
| Terminal navigation | Working knowledge | KEEP practicing |
| File operations | Working knowledge | KEEP practicing |
| Python environment | Operational | KEEP |
| Git repository basics | Operational | KEEP |
| Git staging workflow | Operational | KEEP |
| Git recovery commands | Developing | KEEP practicing |
| Branching | Operational | KEEP |
| Merge conflicts | Demonstrated practically | KEEP practicing |
| Git history inspection | Operational | KEEP |
| Remote Git workflows | Not yet sufficiently practiced | DEFER to Module 3 |

## Git Command Comparison

| Command | Main Purpose | Changes Working File? | Changes Stage? | Creates Commit? |
|---|---|---:|---:|---:|
| `git status` | Inspect repository state | No | No | No |
| `git diff` | Inspect unstaged changes | No | No | No |
| `git add` | Stage changes | No | Yes | No |
| `git restore FILE` | Discard unstaged changes | Yes | No | No |
| `git restore --staged FILE` | Unstage changes | No | Yes | No |
| `git rm FILE` | Remove tracked file and stage deletion | Yes | Yes | No |
| `git mv OLD NEW` | Rename/move tracked file and stage it | Yes | Yes | No |
| `git commit` | Save staged snapshot | No | Uses stage | Yes |
| `git commit --amend` | Replace latest local commit | Possibly | Uses stage | Yes |
| `git revert COMMIT` | Create inverse commit | Yes | Yes | Yes |
| `git reset` | Move HEAD and optionally stage/working state | Possibly | Possibly | No |
| `git switch BRANCH` | Change branches | Usually | No | No |
| `git merge BRANCH` | Combine branch histories | Possibly | Possibly | Usually |

## Recovery Mental Model

```text
WORKING DIRECTORY
      |
      | git add
      v
STAGING AREA
      |
      | git commit
      v
REPOSITORY HISTORY

## Practical Evidence Completed

- Renamed a tracked disposable file with `git mv`.
- Deleted a tracked disposable file with `git rm`.
- Discarded an unstaged modification with `git restore`.
- Unstaged a deletion with `git restore --staged`.
- Replaced a local practice commit using `git commit --amend`.
- Created a feature branch.
- Changed the same line differently on two branches.
- Produced an intentional merge conflict.
- Inspected `<<<<<<<`, `=======`, and `>>>>>>>` conflict markers.
- Manually resolved the conflict.
- Completed a merge commit.
- Inspected the resulting Git graph.

## Relevant Evidence

Integrated recovery/conflict merge commit:

`03b6edc` — Complete Git Module 2 recovery and conflict lab

Previous accepted recovery evidence:

- `cffb321` — Revert "Rename"
- `a5e78ed` — Reapply "Rename"

## Three Strengths

1. I now inspect repository state before making important Git changes.
2. I can use Git recovery tools instead of immediately deleting or recreating work.
3. I can understand and resolve a basic same-line merge conflict.

## Three Current Gaps

1. I still need faster recognition of staged versus unstaged states.
2. I need more repetition choosing the correct recovery command under pressure.
3. Remote repositories and collaboration workflows remain the next learning gap.

## W01 Decision

**KEEP:** practical Git workflow, recovery, branching and inspection.

**SKIP:** repeating completed introductory Module 2 material.

**DEFER:** Module 3 and remote collaboration until W01 closeout is accepted.

## Baseline Conclusion

The local Git baseline is sufficient to close W01 after documentation, testing and final repository verification are complete.
