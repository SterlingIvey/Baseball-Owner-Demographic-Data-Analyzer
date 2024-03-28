import pandas as pd


def calculate_baseball_owners_data(print_data=True):
    # Read data from file
    df = pd.read_csv('baseball_owners_data.csv')
    
    # Data cleaning and preprocessing
    df['net_worth'] = df['net_worth'].replace('[\$,']', '', regex=True).astype(float)
    df['franchise_value'] = df['franchise_value'].replace('[\$,']', '', regex=True).astype(float)

    # How many of each race are represented in this dataset of baseball owners?
    race_count = df['race'].value_counts()

    # What is the average age of baseball owners?
    average_age_owner = round(df['age'].mean(), 1)

    # What percentage of baseball owners have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education'] == 'Bachelors', 'education'].count() / df.shape[0] * 100,1)
    
    # What is the most popular industry among baseball owners?
    top_industry = df['industry'].value_counts().idxmax()
    
    # What is the average net worth of baseball owners?
    average_net_worth = df['net worth'].mean()
    
    # What is the average value of the teams owned?
    df['franchise_value'] = df['franchise_value'].replace('[\$,]', '', regex=True.astype(float)
    average_team_value = df['franchise_value'].mean()


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of owner:", average_age_owner)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print("Most popular industry among owners:", top_industry)
        print("Average net worth of owners: ${:,.2f}".format(average_net_worth))
        print("Average value of teams: ${:,.2f}".format(average_team_value))

    return {
        'race_count': race_count,
        'average_age_owner': average_age_owner,
        'percentage_bachelors': percentage_bachelors,
        'top_industry': top_industry,
        'average_net_worth': average_net_worth,
        'average_team_value': average_team_value
    }