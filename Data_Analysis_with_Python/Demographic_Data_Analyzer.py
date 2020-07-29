import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('file.csv') #'./adult.data.csv' no repl

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round(df.age.groupby(df.sex).mean()['Male'],1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(100*df.education.value_counts()[2]/df.education.value_counts().sum(),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.education.value_counts().loc[['Bachelors','Masters','Doctorate']].sum()
    lower_education = df.education.value_counts().loc[['HS-grad', 'Some-college', 'Assoc-voc', '11th',
       'Assoc-acdm', '10th', '7th-8th', 'Prof-school', '9th', '12th',
        '5th-6th', '1st-4th', 'Preschool']].sum()

    # percentage with salary >50K
    higher_education_rich_total = df.education.groupby(df.salary).value_counts()[[('>50K','Bachelors'),('>50K','Masters'),('>50K','Doctorate')]].sum()
    higher_education_rich = round(100* higher_education_rich_total / higher_education,1)
    lower_education_rich_total = df.education.groupby(df.salary).value_counts()['>50K'].sum() - higher_education_rich_total # total rich minus higher education rich
    lower_education_rich = round(100 * lower_education_rich_total / lower_education,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.iloc[:,-3].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.iloc[:,-3].value_counts().loc[min_work_hours]

    rich_percentage = 100 * df.iloc[:,-3].groupby(df.salary).value_counts().loc[('>50K',min_work_hours)] / num_min_workers

    # What country has the highest percentage of people that earn >50K?
    people_per_country = df.loc[:,'native-country'].value_counts()
    rich_people_per_country = df.loc[:,'native-country'].groupby(df.salary).value_counts()['>50K']
    country = []
    percentage = []
    percent_per_country = {'country':country,'percentage':percentage}

    for element in people_per_country.index:
      for elem in rich_people_per_country.index:
        if (element==elem):
          country.append(element)
          perc = 100 * rich_people_per_country.loc[elem]/ people_per_country.loc[element]
          percentage.append(perc)

    
    highest_earning_country = country[percentage.index(max(percentage))]
    highest_earning_country_percentage = round(max(percentage),1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indians = df.loc[(df.loc[:,'salary'] == '>50K') & (df.loc[:,'native-country'] == 'India')]
    rich_indians_professions = rich_indians.occupation.value_counts()
    top_IN_occupation = rich_indians_professions.index[0] #rich_indians_professions in sorted decreasing

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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data(print_data=True)
