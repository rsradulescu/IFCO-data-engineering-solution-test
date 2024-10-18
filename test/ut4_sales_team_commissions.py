import unittest
from src.t4_sales_team_commissions import get_commissions
from decimal import Decimal, ROUND_HALF_UP
import pandas as pd
'''
UNITTEST for t4_sales_team_commissions
Calculation of Sales Team Commissions
UNIT TEST
- Calculate the commissions
'''

class TestCommission(unittest.TestCase):
    def setUp(self):
        # Create test data to start
        self.orders_df = pd.DataFrame({
            'order_id': ['order1', 'order2', 'order3'],
            'salesowners': ['Alice,Bob,Charlie', 'Bob,Charlie', 'Alice']
        })
        self.invoices_df = pd.DataFrame({
            'order_id': ['order1', 'order2', 'order3'],
            'gross_value': ['120000', '240000', '360000'],
            'vat_rate': ['20', '10', '0'],
            'net_value': [Decimal('100000'), Decimal('218181.82'), Decimal('360000')]
        })

    def test_calculate_commissions(self):
        # +(net_value * order_id) 
        expected_commissions = pd.DataFrame({
            'salesowners': ['Alice', 'Bob', 'Charlie'],
            'commission_cents':[
                    ((Decimal('100000') * Decimal('0.06')).quantize(Decimal('.01'), rounding=ROUND_HALF_UP) +
                      (Decimal('360000') * Decimal('0.06')).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)),
                    ((Decimal('100000') * Decimal('0.025')).quantize(Decimal('.01'), rounding=ROUND_HALF_UP) +
                    (Decimal('218181.82') * Decimal('0.06')).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)),
                    ((Decimal('100000') * Decimal('0.0095')).quantize(Decimal('.01'), rounding=ROUND_HALF_UP) +
                        (Decimal('218181.82') * Decimal('0.025')).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
            ],
            'commission_euro': [Decimal('276.00'), Decimal('155.91'), Decimal('64.05')]
        })
        result_commissions = get_commissions(self.orders_df, self.invoices_df)
        pd.testing.assert_frame_equal(result_commissions, expected_commissions)

if __name__ == '__main__':
    unittest.main()