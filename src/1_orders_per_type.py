
import pandas as pd
import os

'''
TEST1
Calculate the distribution of crate types per company (number of orders per type). 
Ensure to include unit tests to validate the correctness of your calculations.
'''

def load_orders():
    '''
    Load the orders from csv file
    '''
    # Set the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Create the resource path: '../resources/orders.csv'
    csv_path = os.path.join(current_dir, '..', 'resources', 'orders.csv')

    # Create the DF from the csv, consdering the header in the first line, and separator ';'
    df = pd.read_csv(csv_path, header=0, sep=';')
    return df


def get_distribution(df):
    """
    Calculate number of orders per crate type for each company
    """
    distribution = df.groupby(['company_name', 'crate_type']).size().reset_index(name='orders_count')
    return distribution


if __name__ == '__main__':
    df = load_orders()
    #print(df.head())
    distribution = get_distribution(df)
    print(distribution)