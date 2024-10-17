from t1_orders_per_type import load_orders
import json

# Contact_full_name = concat (name + surname)
def get_contact_full_name(contact_data):
    try:
        # Replace double double-quotes with single double-quotes
        contact_data = contact_data.replace('""', '"')
        # Parse the JSON string
        contact_list = json.loads(contact_data)
        # If not empty
        if contact_list and len(contact_list) > 0:
            contact = contact_list[0]  
            contact_name = contact.get('contact_name', '').strip()
            contact_surname = contact.get('contact_surname', '').strip()
            if contact_name and contact_surname:
                return f"{contact_name} {contact_surname}"
    except Exception as e:
        pass
    # Information not available = return placeholder
    return "John Doe"

if __name__ == '__main__':
    # Use load from t1
    df = load_orders()
    
    # Apply function contact_full_name
    df['contact_full_name'] = df['contact_data'].apply(get_contact_full_name)

    # Only return required columns
    df_1 = df[['order_id', 'contact_full_name']]

    # Display the result
    print(df_1)
