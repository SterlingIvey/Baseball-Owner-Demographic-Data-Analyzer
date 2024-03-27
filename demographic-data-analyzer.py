import pandas as pd


def calculate_baseball_owners_data(print_data=True):
    # Read data from file
    df = pd.read_csv('baseball_owners_data.csv')

    # How many of each race are represented in this dataset of baseball owners?
    race_count = df['race'].value_counts()

    # What is the average age of baseball owners?
    average_age_owner = round(df['age'].mean() * 100, 1)

    # What percentage of baseball owners have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education'] == 'Bachelors', 'education'].count() / df.shape[0] * 100,1)
    
    # What is the most popular industry among baseball owners?
    top_industry = df['industry'].value_counts().idxmax()
    
    # What is the average net worth of baseball owners?
    df['net worth'] = df['net worth'].replace('[\$,]', '', regex=True).astype(float)
    average_net_worth = df['net worth'].mean()

    # Identify the most popular industry that MLB owners come from.
    top_IN_industry = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'),'occupation'].value_counts().idxmax()
    
    # What is the average value of the teams owned?
    df['franchise value'] = df['franchise value'].replace('[\$,]', '', regex=True.astype(float)
    average_team_value = df['franchise value'].mean()


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of owner:", average_age_owner)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Most popular industry among owners:", top_industry")
        print(f"Average net worth of owners: $ {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        'highest_earning_country_percentage,
         top_IN_occupation': top_IN_occupation
    }
