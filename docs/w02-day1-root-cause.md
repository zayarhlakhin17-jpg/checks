# W02 Day 1 — Inclusive Range Sum Root Cause

## Symptom

The `inclusive_sum()` function returned the wrong result because it did not include the upper bound.

Example:

```python
inclusive_sum(3)
```

Expected:

```text
6
```

Actual:

```text
3
```

The function calculated:

```text
0 + 1 + 2 = 3
```

instead of:

```text
0 + 1 + 2 + 3 = 6
```

---

## How to reproduce

The original implementation was:

```python
def inclusive_sum(number):
    return sum(range(number))
```

The bug was reproduced manually with:

```bash
python3 -c "from range_sum import inclusive_sum; print(inclusive_sum(3))"
```

Output:

```text
3
```

A unit test was then created:

```python
def test_sum_includes_upper_bound(self):
    self.assertEqual(inclusive_sum(3), 6)
```

Running:

```bash
python3 -m unittest test_range_sum.py -v
```

produced:

```text
AssertionError: 3 != 6
FAILED (failures=1)
```

This confirmed the bug before the implementation was changed.

---

## Expected result

For:

```python
inclusive_sum(3)
```

the function should include the upper bound `3`.

Therefore:

```text
0 + 1 + 2 + 3 = 6
```

Expected result:

```text
6
```

---

## Actual result

The original function returned:

```text
3
```

because `range(3)` generated:

```text
0, 1, 2
```

and excluded `3`.

---

## Root cause

The root cause was an off-by-one error.

Python's `range(stop)` excludes the stop value.

Therefore:

```python
range(3)
```

produces:

```text
0, 1, 2
```

instead of:

```text
0, 1, 2, 3
```

The original implementation used:

```python
sum(range(number))
```

so the requested upper bound was never included.

---

## Fix

The implementation was changed from:

```python
return sum(range(number))
```

to:

```python
return sum(range(number + 1))
```

Using `number + 1` makes the original number part of the generated range.

For example:

```python
range(3 + 1)
```

becomes:

```python
range(4)
```

which generates:

```text
0, 1, 2, 3
```

and therefore:

```text
0 + 1 + 2 + 3 = 6
```

After the fix, the targeted test passed:

```text
test_sum_includes_upper_bound ... ok
```

---

## Regression tests

A boundary regression test was added:

```python
def test_sum_of_zero(self):
    self.assertEqual(inclusive_sum(0), 0)
```

This checks that the function also behaves correctly at the zero boundary.

The final range tests were:

```text
test_sum_includes_upper_bound ... ok
test_sum_of_zero ... ok
```

The complete repository test suite was then run with:

```bash
python3 -m unittest discover -v
```

Final result:

```text
test_sum_includes_upper_bound ... ok
test_sum_of_zero ... ok
test_disk_usage_compiles ... ok
test_free_memory_compiles ... ok

Ran 4 tests

OK
```

---

## Remote/Git concepts learned

I used a separate feature branch for the bug fix:

```text
fix/inclusive-range-sum
```

This kept the bug-fix work separate from `main`.

I also learned the value of keeping different stages of a bug fix in separate commits.

The bug reproduction was committed first:

```text
0daa8a4 Add failing test for inclusive range sum
```

The actual fix was committed separately:

```text
e1c0e1c Fix inclusive range sum off-by-one error
```

The regression protection was then committed separately:

```text
6361ca9 Add boundary coverage for inclusive range sum
```

This creates a clear Git history:

```text
Prove bug
→ Fix bug
→ Add regression protection
```

I also verified that the local `main` branch tracks:

```text
origin/main
```

and used:

```bash
git branch -vv
git ls-remote origin
git status --short
git log --graph --oneline --decorate --all
```

to inspect local branches, remote references, repository cleanliness, and history.

---

## Shell/process observations

A failing test is useful evidence and does not automatically mean the development process failed.

The correct process was:

```text
Reproduce
→ Test
→ Fail
→ Diagnose
→ Fix
→ Test again
→ Add regression protection
```

I also learned to inspect repository state before deleting or committing files.

Useful commands included:

```bash
git status --short
git diff
git log --oneline
```

I accidentally typed a Python assertion directly into the zsh shell once instead of entering it inside Nano.

I also accidentally edited `test_scripts.py` instead of creating `test_range_sum.py`.

I inspected the accidental modification using:

```bash
git diff -- test_scripts.py
```

and safely restored the original tracked file using:

```bash
git restore test_scripts.py
```

I also accidentally created an extra file called:

```text
test_range_sum.py9
```

I inspected its contents before removing it instead of deleting it blindly.

---

## Largest mistake + why it happened

My largest process mistake was editing `test_scripts.py` instead of creating the new `test_range_sum.py` file.

This temporarily replaced existing repository tests with the new test skeleton.

The mistake happened because I entered the wrong filename when opening Nano and continued editing without first confirming which file I had opened.

I detected the problem using:

```bash
git diff -- test_scripts.py
```

and restored the file with:

```bash
git restore test_scripts.py
```

The lesson is to verify the filename and repository status before editing or committing.

For future work I should use:

```bash
pwd
git branch --show-current
git status --short
```

and confirm the filename before making changes.

This reduces the risk of accidentally modifying an existing tracked file.

