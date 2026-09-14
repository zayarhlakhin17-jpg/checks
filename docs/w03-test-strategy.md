# W03 Test Strategy

## Target Project

The current target repository is `checks`.

It is a small Python and shell practice repository containing:

- inclusive range-sum behavior
- inventory fulfillment rules
- checkout-health shell-script behavior
- Python script compilation checks

The typed CLI issue tracker was not found in the existing repository.

The `checks` repository was selected as the bounded W03 testing target.

GitHub Actions CI was implemented to automatically run unittest verification on:

- pushes
- pull requests

---

# Test Strategy

The strategy focuses on protecting important behaviors using:

- unit tests
- boundary tests
- integration/smoke tests
- compilation checks

The main testing principle is:

> Test normal behavior, edge cases, and failure boundaries.

---

# Existing Test Coverage

## 1. Checkout Health Script Test

### Test

`test_checkout_health_script_succeeds`

### Assertion

- Process return code must equal `0`
- stdout must equal:

