import unittest
from src.t3_orders_contact_address import get_contact_address

'''
UNITTEST for t3_orders_contact_address
DataFrame of Orders with Contact Address
Provide a DataFrame (df_2) containing the following columns:order_id, contact_address
UNIT TEST - Possibilities
- Have both city and cp
- Have only city or only cp
- Have empty city and cp: show placeholder for city and cp
- Have None in contact_data
'''

class TestGetContactAddress(unittest.TestCase):
    def test_complete_address(self):
        contact_data = '[{ ""contact_name"":""Curtis"", ""contact_surname"":""Jackson"", ""city"":""Chicago"", ""cp"": ""12345""}]'
        expected_output = 'city name: Chicago, postal_code: 12345'
        result = get_contact_address(contact_data)
        self.assertEqual(result, expected_output)

    def test_missing_city(self):
        contact_data = '[{ ""contact_name"":""Para"", ""contact_surname"":""Cetamol"", ""cp"": "3934"}]'
        expected_output = 'city name: Unknown, postal_code: 3934'
        result = get_contact_address(contact_data)
        self.assertEqual(result, expected_output)

    def test_missing_cp(self):
        contact_data = '[{ ""contact_name"":""Maria"", ""contact_surname"":""Theresa"", ""city"":""Calcutta""}]'
        expected_output = 'city name: Calcutta, postal_code: UNK00'
        result = get_contact_address(contact_data)
        self.assertEqual(result, expected_output)

    def test_missing_city_and_cp(self):
        contact_data = '[{ ""contact_name"":""John"", ""contact_surname"":""Doe""}]'
        expected_output = 'city name: Unknown, postal_code: UNK00'
        result = get_contact_address(contact_data)
        self.assertEqual(result, expected_output)

    def test_empty_contact_data(self):
        contact_data = None
        expected_output = 'city name: Unknown, postal_code: UNK00'
        result = get_contact_address(contact_data)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()