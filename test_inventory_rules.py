import unittest
from inventory_rules import can_fulfill_order

class TestInventoryRules(unittest.TestCase):
    def test_order_above_stock_is_rejected(self):
        self.assertFalse(can_fulfill_order(5,6))

    def test_exact_stock_order_is_allowed(self):
        self.assertEqual(can_fulfill_order(5,5),True)

    def test_order_below_stock_is_allowed(self):
        self.assertTrue(can_fulfill_order(5,4))

    def test_positive_order_with_zero_stock_is_rejected(self):
        self.assertFalse(can_fulfill_order(0,1))
if __name__ == "__main__":
    unittest.main()
