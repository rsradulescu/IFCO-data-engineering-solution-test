import unittest
import pandas as pd
from src.t5_company_salesowners import load_orders, get_company_salesowners_df

'''
UNITTEST for t5_company_salesowners
Provide a DataFrame (df_3) containing the following columns:company_id,company_name,list_salesowners.
UNIT TEST
- test_create_company_salesowners_df: sales owners from all orders with similar company names are combined.
- test_duplicate_companies_handling: duplicate companies are correctly identified and merged.
'''

class TestCompanySalesOwners(unittest.TestCase):
    def setUp(self):
        # Create a sample df 
        self.orders_df = pd.DataFrame({
            'order_id': ['order1', 'order2', 'order3', 'order4'],
            'company_id': ['id1', 'id2', 'id3', 'id4'],
            'company_name': ['Acme Corp', 'acme corp.', 'Beta LLC', 'beta llc'],
            'salesowners': ['Ammy Winehouse, Bob Jones', 'Charlie Brown', 'Luke Skywalker', 'Ammy Winehouse'],
        })
        # Split and clean the salesowners
        self.orders_df['salesowners_list'] = self.orders_df['salesowners'].apply(
            lambda x: [s.strip() for s in x.split(',')] if pd.notnull(x) else []
        )

    def test_create_company_salesowners_df(self):
        df_3 = get_company_salesowners_df(self.orders_df)
        # Expected results
        expected_data = {
            'company_id': ['id1', 'id3'],
            'company_name': ['Acme Corp', 'Beta LLC'],
            'list_salesowners': ['Ammy Winehouse, Bob Jones, Charlie Brown', 'Ammy Winehouse, Luke Skywalker']
        }
        expected_df = pd.DataFrame(expected_data)
        # Check if the DataFrame matches the expected results
        pd.testing.assert_frame_equal(df_3.reset_index(drop=True), expected_df)


    def test_duplicate_companies_handling(self):
        df_3 = get_company_salesowners_df(self.orders_df)
        # Check that duplicate companies are merged
        self.assertEqual(len(df_3), 2)
        self.assertTrue('Acme Corp' in df_3['company_name'].values)
        self.assertTrue('Beta LLC' in df_3['company_name'].values)

if __name__ == '__main__':
    unittest.main()
