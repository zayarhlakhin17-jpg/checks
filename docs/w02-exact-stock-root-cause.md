# W02 — Exact-Stock Order Root Cause

## Symptom

An order was incorrectly rejected when the requested quantity was exactly equal to the available stock.

Example:

Stock: 5  
Order quantity: 5

Expected: order allowed  
Actual: order rejected

## How to reproduce

The original implementation was:

```python
def can_fulfill_order(stock, quantity):
    return quantity < stock

The problem can be reproduced with:

can_fulfill_order(5, 5)

The function returned:

False

A failing unit test was added:

def test_exact_stock_order_is_allowed(self):
    self.assertEqual(can_fulfill_order(5, 5), True)

Before the fix, the test failed with:

AssertionError: False != True
Expected result

When stock is 5 and the customer orders exactly 5 units, the order should be allowed.

Expected:

True
Actual result

The function returned:

False
Root cause

The implementation used the strict less-than operator:

quantity < stock

For an exact-stock order:

5 < 5

evaluates to:

False

The business rule requires an order to be accepted when quantity is less than or equal to available stock.

Fix

The comparison was changed from:

quantity < stock

to:

quantity <= stock

Now:

5 <= 5

returns:

True
Regression tests

Two inventory boundary cases are covered:

stock 5, order 5 → allowed
stock 5, order 6 → rejected

Tests:

def test_exact_stock_order_is_allowed(self):
    self.assertEqual(can_fulfill_order(5, 5), True)

def test_order_above_stock_is_rejected(self):
    self.assertFalse(can_fulfill_order(5, 6))

The full repository suite passed:

Ran 6 tests
OK
Git workflow

The work was completed on:

fix/exact-stock-order

Commit sequence:

4db2d56 Add failing test for exact-stock order
a496633 Fix exact-stock order rejection
b9fb80a Add insufficient-stock regression coverage

This preserves the development sequence:

reproduce → fix → regression protection
Process observations

A test must contain an assertion.

Simply calling:

can_fulfill_order(5, 6)

does not verify whether the returned value is correct.

A proper regression test must assert the expected behavior, for example:

self.assertFalse(can_fulfill_order(5, 6))
Largest mistake + why it happened

The largest mistake was creating a regression test that called the function without asserting its result.

The test appeared to pass even though it did not verify any behavior.

Another mistake was temporarily changing the exact-stock test from (5, 5) to (5, 6).

The lesson is to verify that every test has:

an input,
an expected result,
an assertion comparing actual behavior with that expectation.

Save it, then run:

```bash
git status --short
