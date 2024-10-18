#Conditional Imports
try:
    # Relative import
    from src.t1_orders_per_type import load_orders
except ImportError:
    # Direct execution
    from t1_orders_per_type import load_orders
import json 
import os
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict

'''
Test 4: Calculation of Sales Team Commissions
The Sales Team requires your assistance in computing the commissions. 
It is possible for multiple salespersons to be associated with a single order, 
as they may have participated in different stages of the order. The salesowners field comprises a ranked list of the salespeople
 who have ownership of the order. The first individual on the list represents the primary owner, while the subsequent individuals,
if any, are considered co-owners who have contributed to the acquisition process. 
'''

def load_invoices():
    '''
    Load the invoices from json file
    '''
    # Set the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Create the resource path: '../resources/invoicing_data.json'
    json_path = os.path.join(current_dir, '..', 'resources', 'invoicing_data.json')

    # Load the json file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract the list of invoices from the json
    invoices_list = data['data']['invoices']

    # Create a DataFrame from the invoices list
    data = pd.DataFrame(invoices_list)
    # Replace orderid column name
    data['order_id'] = data['orderId']
    # Convert 'gross' and 'vat' to Decimal
    data['gross_value'] = data['grossValue'].apply(Decimal)
    data['vat_rate'] = data['vat'].apply(Decimal)

    # Calculate the net value [NET = gross - vat]
    data['net_value'] = data.apply(
        lambda row: (row['gross_value'] / (1 + row['vat_rate'] / 100)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP),
        axis=1
    )
    return data

def get_commissions(df_orders, df_invoices):
    # Define commission rates from main-owner, co-owner1 and co-owner2
    commission_rates = [Decimal('0.06'), Decimal('0.025'), Decimal('0.0095')]
    # Merge orders and invoices on order id
    merged_df = df_orders.merge(df_invoices, left_on='order_id', right_on='order_id')
    #print(len(merged_df))
    # Dictionary to store commissions per sales owner
    commissions = defaultdict(Decimal)

    # Iterate over each order
    for index, row in merged_df.iterrows():
        #print('NEW ROW: ', row)
        net_value = row['net_value']
        # Get salesowner split
        salesowners = row['salesowners'].split(',')

        for id_order, owner in enumerate(salesowners):
            if id_order < 3:
                rate = commission_rates[id_order]
                commission = (net_value * rate).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
                commissions[owner] += commission
            else:
                break  # Only first three owners get commissions

    # Convert commissions to a DataFrame
    commissions_df = pd.DataFrame(list(commissions.items()), columns=['salesowners', 'commission_cents'])
    # Convert commission from cents to euros
    commissions_df['commission_euro'] = (commissions_df['commission_cents'] / 100).apply(
        lambda x: x.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    )

    # Sort by descending commission amount
    commissions_df = commissions_df.sort_values(by='commission_euro', ascending=False)

    return commissions_df


if __name__ == '__main__':
    # Use load_orders to get the orders.csv
    df_orders = load_orders()
    
    # Create new load function to get the json invoices
    df_invoices = load_invoices()

    # Apply function to get commisssions
    commissions_results = get_commissions(df_orders, df_invoices)

    print(commissions_results)
