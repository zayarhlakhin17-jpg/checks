import unittest
from inventory_rules import can_fulfill_order

class TestInventoryRules(unittest.TestCase):
    def test_exact_stock_order_is_allowed(self):
        self.assertEqual(can_fulfill_order(5,5),True)

if __name__ == "__main__":
    unittest.main()
