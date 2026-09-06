# W02 Seeded Defect #3 — Checkout Health Command Failure

## Symptom

Running `./run_checkout_health.sh` failed with:

`python-three: command not found`

## Expected result

The health script should print:

`checkout-health: OK`

and return exit code `0`.

## Actual result before fix

The script returned exit code `127`.

The automated test failed with:

`AssertionError: 127 != 0`

## Reproduction

Commands used:

- `./run_checkout_health.sh`
- `python3 -m unittest test_checkout_health.py -v`

## Diagnosis

`command -v python-three` returned no result.

`command -v python3` returned:

`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`

The PATH contained the Python 3.13 executable directory.

## Root cause

The script requested the nonexistent executable `python-three` instead of the valid executable `python3`.

Python itself was installed correctly and PATH was functioning correctly.

## Fix

Changed:

`python-three -c 'print("checkout-health: OK")'`

to:

`python3 -c 'print("checkout-health: OK")'`

## Verification

Manual run:

- Output: `checkout-health: OK`
- Exit code: `0`

Targeted test:

`python3 -m unittest test_checkout_health.py -v`

Result: `OK`

Full regression suite:

`python3 -m unittest discover -v`

Result:

`Ran 7 tests`

`OK`

## Git evidence

Failing-test commit:

`feada5e — Add failing checkout health command test`

Fix commit:

`ca3f5d9 — Fix checkout health Python command`

## Shell concepts demonstrated

- PATH lookup
- Executable discovery with `command -v`
- Exit codes
- Exit code `127`
- Shell scripts
- Executable permission with `chmod +x`
- Program versus process
- Automated subprocess testing

## Debugging lesson

Do not assume the runtime is broken when a command fails.

Check these separately:

1. Does the executable exist?
2. Can the shell find it through PATH?
3. Is the script requesting the correct command name?

The confirmed root cause should be fixed instead of changing a working environment.
