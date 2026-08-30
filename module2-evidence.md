# Git Module 2 Evidence

## Module Results

| Assessment 			| Result 	|
|-------------------------------|---------------|
| Git/GitHub Module 2 		| Complete 	|
| Practice Assignment 		| 100% 		|
| Google Skills Git Merge Lab 	| 20/20 	|
| Module 2 Graded Challenge 	| 95% 		|
| Undoing Things Practice 	| 100% 		|


## Git Recovery Practice

The integrated Git lab demonstrated:

- `git mv` — rename a tracked file
- `git rm` — remove a tracked file
- `git restore` — discard an unstaged working-tree change
- `git restore --staged` — remove a change from the staging area
- `git commit --amend` — replace the most recent local commit
- feature branch creation
- intentional same-line merge conflict
- manual conflict resolution
- merge commit creation

## Merge Conflict

Both `main` and `module2-lab/conflict-practice` changed the same line in:

`git-module2-lab/conflict-demo.txt`

The conflict contained Git markers:
- `<<<<<<< HEAD`
- `status = MAIN version`
- `=======`
- `status = FEATURE version`
- `>>>>>>> module2-lab/conflict-practice`o
## Three Gaps

1. I need faster recognition of staged versus unstaged status indicators.
2. I need more practice choosing between restore, reset, revert and amend.
3. I need more experience with remote Git workflows.

## Skip / Keep Decisions

### KEEP

- Git status and diff inspection before commits
- Small meaningful commits
- Branch-based development
- Merge conflict practice
- Recovery commands
- Git history inspection

### SKIP FOR W01

- Additional Module 2 videos
- Repeating completed assessments
- Additional introductory Git exercises

### DEFER

- Module 3 — Working with Remotes
- Advanced remote collaboration
- Pull requests and remote branch workflows

These are deferred until W01 is formally closed.

## Tomorrow's First Action

Run:

```bash
git status --short
