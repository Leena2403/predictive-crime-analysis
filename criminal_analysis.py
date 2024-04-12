import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

accused = pd.read_csv('Datasets/AccusedData (1).csv')
fir = pd.read_csv('Datasets/FIR_Details_Data.csv')

def get_criminal(district, Unit_Name, Crime_No, month, year=2024, gender='MALE'):
    print("Filtering by:", district, "Crime No.", Crime_No, "Month:", month, year, gender)
    data = accused[(accused['District_Name'] == district) &
                   (accused['UnitName'] == Unit_Name) &
                   (accused['Month'] == month) &
                   (accused['Year'] == year) &
                   (accused['Sex'] == gender)]

    data = data[data['crime_no'] == Crime_No]
    group = data.groupby("Person_Name").size()
    return data

def get_freq_table(data):
    group = data.groupby("Person_Name").size()
    return group


def get_probability(data):
    crime_list = data['crime_no'].tolist()
    prob = accused[accused['crime_no'].isin(crime_list)]

    person_list = data['Person_Name'].tolist()
    prob = prob[prob['Person_Name'].isin(person_list)]

    group = prob.groupby('Person_Name').size()
    return group


def compute_confidence_matrix(district, Unit_name, Crime_No, month, year=2024, gender='MALE', top_n=5):
    global app
    data = get_criminal(district, Unit_name, Crime_No, month, year, gender)
    if data.empty:
        return "No data found for the given criteria."

    freq = get_freq_table(data)
    if freq.empty:
        return "No frequency data found for the given criteria."

    past_data = get_probability(data)
    if past_data.empty:
        return "No past data found for the given criteria."

    confidence_values = (past_data / freq).sort_values(ascending=False).head(top_n)

    if confidence_values.empty:
        return "No confidence values computed."

    # Normalize confidence values
    normalized_confidence_values = confidence_values / confidence_values.sum()

    top_criminals = normalized_confidence_values.index.tolist()
    top_confidences = normalized_confidence_values.values.tolist()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=normalized_confidence_values.index, y=normalized_confidence_values.values, ax=ax, color='Coral')
    ax.set_title('Confidence Matrix for Top Criminals')
    ax.set_xlabel('Criminals')
    ax.set_ylabel('Confidence Value')
    ax.tick_params(axis='x', rotation=45)

    plot_filename = 'static/confidence_matrix_plot.png' 
    plt.savefig(plot_filename)

    return plot_filename

def pie_chart(data, category):
    group = data.groupby(category).size().nlargest(15)
    fig, ax = plt.subplots(figsize=(8, 8))
    group.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_title('Top 15 Crimes Committed under Selected Arrest ID')
    ax.set_ylabel('')
    plt.show()

def bg_details(data):
    crime_list = data['crime_no'].tolist()
    age_list = data['age'].tolist()
    prob = accused[accused['crime_no'].isin(crime_list)]
    prob = accused[accused['age'].isin(crime_list)]

    grouped_data = prob.groupby(['age', 'crime_no']).size().reset_index(name='count')

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(data=grouped_data, x='age', y='count', hue='crime_no', ax=ax)
    ax.set_title("People of Different Ages Committing Crimes")
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title='Crime No', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()


def get_injury(data, fir):
    arr_list = data['Arr_ID'].tolist()
    injury = fir[fir['FIR_ID'].isin(arr_list)]

    injury = injury.drop(columns=['District_Name', 'RI', 'Accused Count', 'Unit_ID'])
    if injury.empty:
        return "Unavailable Arrest ID in FIR ID"
    else:
        pie_chart(injury, 'CrimeGroup_Name')
    return injury


def criminal(Arr_ID, name=None, age=None, crime_no=None):
    filters = {'Arr_ID': Arr_ID}
    if name is not None:
        filters['Person_Name'] = name
    if age is not None:
        filters['age'] = age
    if crime_no is not None:
        filters['crime_no'] = crime_no

    data = accused[(accused['Arr_ID'] == Arr_ID) &
                   ((name is None) or (accused['Person_Name'] == name)) &
                   ((age is None) or (accused['age'] == age)) &
                   ((crime_no is None) or (accused['crime_no'] == crime_no))
                   ]
    if data.empty:
        return "No data found"
    else:
        if name is not None and age is not None or crime_no is not None:
            bg_details(data)
            if get_injury(data, fir) is None:
                pass
            else:
                return data

        else:
            pie_chart(fir, 'CrimeGroup_Name')
            # get_injury(data, fir)
            return data