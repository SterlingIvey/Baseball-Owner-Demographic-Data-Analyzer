import pandas as pd

def calculate_baseball_owners_data(print_data=True):
    # ... (existing code)

def rank_owners_by_net_worth(df):
    """
    Ranks baseball team owners by their net worth.

    Parameters:
    df (DataFrame): The DataFrame containing the owners' data.

    Returns:
    DataFrame: DataFrame sorted by owners' net worth in descending order.
    """
    # Sort the DataFrame based on the 'net_worth' column in descending order
    sorted_df = df.sort_values(by='net_worth', ascending=False)
    return sorted_df
    
def rank_by_franchise_value(df):
    """
    Ranks baseball teams by their franchise value.

    Parameters:
    df (DataFrame): DataFrame containing the team and franchise value data.

    Returns:
    DataFrame: Sorted by franchise value in descending order.
    """
    return df.sort_values(by='franchise_value', ascending=False)[['team', 'franchise_value']]

# Usage Example
df = pd.read_csv('baseball_owners_data.csv')
# Assuming the 'net_worth' column exists and is correctly formatted
df['net_worth'] = df['net_worth'].replace('[\$,]', '', regex=True).astype(float)

sorted_owners = rank_owners_by_net_worth(df)
print(sorted_owners[['name', 'net_worth']])