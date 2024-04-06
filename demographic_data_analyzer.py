import pandas as pd

def calculate_baseball_owners_data(print_data=True):
    # Read data from file
    df = pd.read_csv('baseball_owners_data.csv')

    # How many of each race are represented in this dataset of baseball owners?
    race_count = df['race'].value_counts()

    # What is the average age of baseball owners?
    average_age_owners = round(df['age'].mean(), 1)

    # What about median age?
    median_age_owners = round(df['age'].median(), 1)

    # What percentage of baseball owners have at least a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education'] == 'bachelors', 'education'].count() / df.shape[0] * 100,1)
    
    # What is the most popular industry among baseball owners?
    top_industry = df['industry'].value_counts().idxmax()
    
    # What is the median net worth of baseball owners?
    median_net_worth = df['net_worth'].median()
    
    # What is the average value of the teams owned?
    average_team_value = df['franchise_value'].mean()

    max_value_index = df['franchise_value'].idxmax()

    # What is the most valuable franchise?
    most_valuable_franchise_row = df.loc[df['franchise_value'].idxmax()]

    # Extract the team name and franchise value from the row
    most_valuable_team = most_valuable_franchise_row['team']
    most_valuable_value = most_valuable_franchise_row['franchise_value']

    # Data output is below this line

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Current Average Age of Owners:", average_age_owners)
        print("Current Median Age of Owners:", median_age_owners)
        print(f"Current Percentage with at least Bachelors degrees: {percentage_bachelors}%")
        print("Current Most popular industry among owners:", top_industry)
        print("Current Median net worth of owners: ${:,.2f}".format(median_net_worth))
        print("Current Average value of teams: ${:,.2f}".format(average_team_value))
        print("Most Valuable Franchise: {most_valuable_team} with a value of ${most_valuable_value:} ")

    return {
        'race_count': race_count,
        'average_age_owners': average_age_owners,
        'median_age_owners': median_age_owners,
        'percentage_bachelors': percentage_bachelors,
        'top_industry': top_industry,
        'median_net_worth': median_net_worth,
        'average_team_value': average_team_value,
        'most_valuable_franchise': most_valuable_team
    }
    return calculate_baseball_owners_data()
