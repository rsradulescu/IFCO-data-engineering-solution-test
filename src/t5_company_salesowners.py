#Conditional Imports
try:
    # Relative import
    from src.t1_orders_per_type import load_orders
except ImportError:
    # Direct execution
    from t1_orders_per_type import load_orders
import pandas as pd

'''
Test 5: DataFrame of Companies with Sales Owners
Provide a DataFrame (df_3) containing the following columns:company_id, company_name, list_salesowners
- Consider the possibility of duplicate companies stored under multiple IDs in the database.
'''

def get_company_salesowners_df(orders_df):
    # Add new column: normalize company names. Consider all lowercase and rwmove non-alphanumeric characters.  
    orders_df['normalized_company_name'] = orders_df['company_name'].str.lower().str.replace(r'\W', '', regex=True)

    # Mapping from normalized_company_name to a unique company_id
    company_id_mapping = orders_df.drop_duplicates('normalized_company_name').set_index('normalized_company_name')['company_id']
    
    # Group orders by normalized company name
    grouped = orders_df.groupby('normalized_company_name')
    
    # Initialize lists to build df_3
    company_ids = []
    company_names = []
    list_salesowners = []

    for normalized_name, group in grouped:
        # Get the company_id from the mapping
        company_id = company_id_mapping[normalized_name]
        company_ids.append(company_id)
        # Use the first company_name
        company_name = group['company_name'].mode()[0]
        company_names.append(company_name)
        
        # Collect all salesowners for this company. Consider multiple owners in one value, clean and split
        salesowners_lists = group['salesowners'].apply(
            lambda x: [s.strip() for s in x.split(',')] if pd.notnull(x) else []
        ).tolist()

        # Flatten the list of lists
        salesowners = set([owner for sublist in salesowners_lists for owner in sublist])
        #print('salesowners: ',salesowners)
        # Ensure uniqueness and sort in ascending alphabetical order of the first name
        salesowners_sorted = sorted(salesowners, key=lambda x: x.split()[0])
        # Join into a comma-separated list
        list_salesowners.append(', '.join(salesowners_sorted))

    # Create the result df_3
    df_3 = pd.DataFrame({
        'company_id': company_ids,
        'company_name': company_names,
        'list_salesowners': list_salesowners
    })

    return df_3
    
if __name__ == '__main__':
    df_orders = load_orders()
    df_3 = get_company_salesowners_df(df_orders)
    print(df_3)