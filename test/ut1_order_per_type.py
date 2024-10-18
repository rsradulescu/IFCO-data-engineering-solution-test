import unittest
import pandas as pd

from src.t1_orders_per_type import get_distribution

'''
UNITTEST for t1_order_per_type
Calculate the distribution of crate types per company (number of orders per type). 
Ensure to include unit tests to validate the correctness of your calculations.
'''
class TestDistribution(unittest.TestCase):

    def test_distribution(self):
        # Create df for testing
        data = {
            'company_name': ['Fresh Fruits', 'Fresh Fruits', 'Veggies', 'Veggies', 'Meat'],
            'crate_type': ['Type1', 'Type2', 'Type1', 'Type1', 'Type2'],
            'order_id': [1, 2, 3, 4, 5]
        }
        test_df = pd.DataFrame(data)
        
        # Create df for expected result
        expected_data = {
            'company_name': ['Fresh Fruits', 'Fresh Fruits', 'Veggies', 'Meat'],
            'crate_type': ['Type1', 'Type2', 'Type1', 'Type2'],
            'orders_count': [1, 1, 2, 1]
        }
        expected_df = pd.DataFrame(expected_data)
        
        # Get distribution from test_df
        result_df = get_distribution(test_df)
        
        # Sort dataframes for better comparison
        result_df = result_df.sort_values(by=['company_name', 'crate_type']).reset_index(drop=True)
        expected_df = expected_df.sort_values(by=['company_name', 'crate_type']).reset_index(drop=True)
        
        # Assert equal
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()
