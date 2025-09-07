import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    df.head()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    qtd_bachelors = (df['education'] == 'Bachelors').sum()
    percentage_bachelors = (qtd_bachelors / total_people) * 100
    percentage_bachelors = round(percentage_bachelors, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_edu_list = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df['education'].isin(higher_edu_list)
    total_higher_edu = df[higher_education].shape[0]
    higher_edu_rich = df[higher_education & (df['salary'] == '>50K')].shape[0]
    higher_education_rich = round((higher_edu_rich / total_higher_edu) * 100, 1)

    # Teste de mensagem
    lower_education = ~df['education'].isin(higher_edu_list)
    total_lower_edu = df[lower_education].shape[0]
    lower_edu_rich_count = df[lower_education & (df['salary'] == '>50K')].shape[0]
    lower_education_rich = round((lower_edu_rich_count / total_lower_edu) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_work_hours = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_work_hours[num_min_work_hours['salary'] == '>50K']
    rich_percentage = round(len(rich_min_workers) / len(num_min_work_hours) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    rich_people = df[df['salary'] == '>50K']
    country_earning = (rich_people['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country = country_earning.idxmax()
    highest_earning_country_percentage = round(country_earning.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax())

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