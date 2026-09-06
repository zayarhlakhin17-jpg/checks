import subprocess
import unittest


class CheckoutHealthTest(unittest.TestCase):

    def test_checkout_health_script_succeeds(self):
        result = subprocess.run(
            ["./run_checkout_health.sh"],
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "checkout-health: OK")


if __name__ == "__main__":
    unittest.main()
