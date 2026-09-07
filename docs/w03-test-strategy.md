# W03 Test Strategy

## Target project

The current target repository is `checks`.

It is a small Python and shell practice repository containing:

- inclusive range-sum behavior
- inventory fulfillment rules
- checkout-health shell-script behavior
- Python script compilation checks

Typed CLI issue tracker: not found in the existing repository.

Full CI implementation is blocked until the target project is identified.

## Existing tests

### 1. test_checkout_health_script_succeeds

Assertions:

- process return code must equal `0`
- stdout must equal `checkout-health: OK`

Protected behavior:

The checkout-health shell script must execute successfully and return the expected output.

Classification:

Integration / smoke test because the Python test launches an external shell script.

### 2. test_order_above_stock_is_rejected

Assertion:

`can_fulfill_order(5, 6)` must be false.

Protected behavior:

An order larger than available stock must be rejected.

Classification:

Unit test with boundary coverage.

### 3. test_exact_stock_order_is_allowed

Assertion:

`can_fulfill_order(5, 5)` must be true.

Protected behavior:

An order equal to the available stock must be accepted.

Classification:

Unit test with edge/boundary coverage.

### 4. test_sum_of_zero

Assertion:

`inclusive_sum(0)` must equal `0`.

Protected behavior:

Zero input must produce zero.

Classification:

Unit test with edge-case coverage.

### 5. test_sum_includes_upper_bound

Assertion:

`inclusive_sum(3)` must equal `6`.

Protected behavior:

The requested upper bound must be included in the sum.

Classification:

Unit regression test with boundary coverage.

### 6. test_disk_usage_compiles

Assertion:

`disk_usage.py` must compile without raising a Python compilation exception.

Protected behavior:

The script must remain syntactically valid Python.

Classification:

Compile / smoke check.

### 7. test_free_memory_compiles

Assertion:

`free_memory.py` must compile without raising a Python compilation exception.

Protected behavior:

The script must remain syntactically valid Python.

Classification:

Compile / smoke check.

## Baseline result

Command:

`python3 -m unittest discover -v`

Result:

PASTE THE EXACT RESULT HERE.

Command:

`git diff --check`

Result:

PASTE THE EXACT RESULT HERE. If there was no output, record: no whitespace errors reported.

## Five failure cases

1. Checkout-health command cannot execute — expected exit code `0` and output `checkout-health: OK`.
2. Order quantity exceeds stock — expected behavior is rejection.
3. Order quantity exactly equals stock — expected behavior is acceptance.
4. Inclusive sum accidentally excludes the upper bound — `inclusive_sum(3)` must remain `6`.
5. Zero-input range sum produces a non-zero value — `inclusive_sum(0)` must remain `0`.

## Dependency decision

The typed CLI issue tracker was not found in the existing `checks` repository.

This is an unresolved dependency for the planned full CI implementation.

## Next decision

Do not begin full CI implementation until the target project is confirmed.
