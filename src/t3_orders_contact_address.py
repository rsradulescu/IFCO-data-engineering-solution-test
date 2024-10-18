#Conditional Imports
try:
    # Relative import
    from src.t1_orders_per_type import load_orders
except ImportError:
    # Direct execution
    from t1_orders_per_type import load_orders
import json 

'''
Test 3: DataFrame of Orders with Contact Address
Provide a DataFrame (df_2) containing the following columns:order_id, contact_address
'''


# Contact_adress = concat (city + cp)
def get_contact_address(contact_data):
    try:
        # Replace double double-quotes with single double-quotes
        contact_data = contact_data.replace('""', '"')
        # Parse the JSON string
        contact_list = json.loads(contact_data)
        # Consider if content_data exist and have values
        if contact_list and len(contact_list) > 0:
            # Complete values for city and cp
            contact = contact_list[0] if contact_list else {}
            city = contact.get('city', 'Unknown')
            cp = contact.get('cp', 'UNK00')
    except Exception as e:
        city = 'Unknown'
        cp = 'UNK00'
    return f'city name: {city}, postal_code: {cp}'


if __name__ == '__main__':
    # Use load from t1
    df = load_orders()
    
    # Apply function 
    df['contact_address'] = df['contact_data'].apply(get_contact_address)

    # Only return required columns
    df_2 = df[['order_id', 'contact_address']]

    # Display the result
    print(df_2)