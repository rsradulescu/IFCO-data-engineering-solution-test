import unittest
import pandas as pd
from src.t2_orders_full_name import get_contact_full_name

'''
UNITTEST for t2_orders_full_name
DataFrame of Orders with Full Name of the Contact
Provide a DataFrame (df_1) containing the following columns: order_id, contact_full_name
UNIT TEST - Possibilities
- Have both name and surname
- Have only name or only surname: show John Doe if some of these are not abailable
- Have empty data: show placeholder
- Have extra double quotes
'''
class TestGetContactFullName(unittest.TestCase):
    def test_valid_contact(self):
        contact_data = '[{ "contact_name":"Curtis", "contact_surname":"Jackson" }]'
        expected_result = 'Curtis Jackson'
        result = get_contact_full_name(contact_data)
        self.assertEqual(result, expected_result)

    def test_missing_contact_name(self):
        contact_data = '[{ "contact_surname":"Jackson" }]'
        expected_result = 'John Doe'
        result = get_contact_full_name(contact_data)
        self.assertEqual(result, expected_result)

    def test_missing_contact_surname(self):
        contact_data = '[{ "contact_name":"Curtis" }]'
        expected_result = 'John Doe'
        result = get_contact_full_name(contact_data)
        self.assertEqual(result, expected_result)

    def test_empty_string(self):
        contact_data = ''
        expected_result = 'John Doe'
        result = get_contact_full_name(contact_data)
        self.assertEqual(result, expected_result)

    def test_extra_double_quotes(self):
        contact_data = '[{ ""contact_name"":""Curtis"", ""contact_surname"":""Jackson"" }]'
        expected_result = 'Curtis Jackson'
        result = get_contact_full_name(contact_data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()    