import pandas as pd

# Notes:
# 1. DataFrame object does not have length method, use shape to get number along an axis accordingly
# 2. Boolean or is represented by | not ||. Similarly, and is represented by &, not &&.
# 3. Put brackets around the booleans before applying the operators
# 4. You have to use complicated chaining to get values sometimes
# 5. Round off the result using the in buolt round function in Python or Series/Data Frame's own round function
def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts().round(1)
    
    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean().round(1)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df.loc[df['education'] == "Bachelors"].shape[0]) * 100 / (df['education'].shape[0]), 1)
    
    # # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # # What percentage of people without advanced education make more than 50K?
    
    # # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_condition = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    higher_education = df.loc[higher_education_condition]
    lower_education = df.loc[~higher_education_condition]
    
    # # percentage with salary >50K
    higher_education_rich = round(((higher_education.loc[higher_education['salary'] == '>50K'].shape[0]) * 100/(higher_education.shape[0])), 1)
    lower_education_rich = round(((lower_education.loc[lower_education['salary'] == '>50K'].shape[0]) * 100/(lower_education.shape[0])), 1)
    
    # # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    # # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df.loc[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_workers.shape[0]
    rich_percentage = round((min_workers.loc[min_workers['salary'] == '>50K'].shape[0] * 100 / (num_min_workers)), 1)
    
    # # What country has the highest percentage of people that earn >50K?
    earning_more_than_50K_by_country = df.loc[df['salary'] == '>50K', 'native-country'].value_counts() * 100 / df['native-country'].value_counts()
    highest_earning_country_record = earning_more_than_50K_by_country.loc[earning_more_than_50K_by_country == earning_more_than_50K_by_country.max()]
    highest_earning_country = highest_earning_country_record.index.values[0]
    highest_earning_country_percentage = round(highest_earning_country_record.iloc[0], 1)
    
    # # Identify the most popular occupation for those who earn >50K in India.
    IN_occupations = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India'), 'occupation']
    IN_occupation_counts = IN_occupations.value_counts()
    top_IN_occupation_count = IN_occupation_counts.max()
    top_IN_occupation = IN_occupation_counts.loc[IN_occupation_counts == top_IN_occupation_count].index.values[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
