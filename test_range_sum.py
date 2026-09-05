import unittest
from range_sum import inclusive_sum


class TestInclusiveSum(unittest.TestCase):
    def test_sum_of_zero(self):
        self.assertEqual(inclusive_sum(0),0)
    def test_sum_includes_upper_bound(self):
        self.assertEqual(inclusive_sum(3), 6)

if __name__ == "__main__":
    unittest.main()
