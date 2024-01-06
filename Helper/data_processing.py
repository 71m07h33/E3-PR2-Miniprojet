# data_processing.py
import pandas as pd


# Load the CSV data
df_2021 = pd.read_csv("./Data/lic-data-2021.csv", delimiter=";", encoding="utf-8")
df_2020 = pd.read_csv("./Data/lic-data-2020.csv", delimiter=";", encoding="utf-8")
df_2019 = pd.read_csv("./Data/lic-data-2019.csv", delimiter=";", encoding="utf-8")

year_mapping = {
    2021: df_2021,
    2020: df_2020,
    2019: df_2019,
}

age_categories = [
    "1 à 4 ans",
    "5 à 9 ans",
    "10 à 14 ans",
    "15 à 19 ans",
    "20 à 24 ans",
    "25 à 29 ans",
    "30 à 34 ans",
    "35 à 39 ans",
    "40 à 44 ans",
    "45 à 49 ans",
    "50 à 54 ans",
    "55 à 59 ans",
    "60 à 64 ans",
    "65 à 69 ans",
    "70 à 74 ans",
    "75 à 79 ans",
    "80 à 99 ans",
    "NR",
]


def generate_histogram_data(df, federation_name, commune_name, selected_year):
    # Filter the data based on the provided federation and commune
    filtered_data = df[
        (df["Fédération"] == federation_name) & (df["Commune"] == commune_name)
    ]

    # Initialize empty lists for female and male data
    female_data = []
    male_data = []
    year_values = []

    # Iterate through age categories
    for age_category in age_categories:
        female_col = f"F - {age_category}"
        male_col = f"H - {age_category}"

        # Extract female and male data for the specific age category
        female_count = filtered_data[female_col].values[0]
        male_count = filtered_data[male_col].values[0]

        # Append data to respective lists
        female_data.append(female_count)
        male_data.append(male_count)
        year_values.append(selected_year)

    # Create a new DataFrame in wide-format
    wide_format_data = pd.DataFrame(
        {
            "Age": age_categories,
            "Female": female_data,
            "Male": male_data,
            "Year": year_values,
        }
    )

    return wide_format_data

def generate_camembert_data(commune_name):
 
    #Dictionnary to stock stats
    pop_data = {}

    # Iterate through files
    for year,df in year_mapping.items():

        #filter for the data file
        filtered_data = df[df["Commune"] == commune_name]

        # Group by Federation and sum the total population for each federation
        grouped = filtered_data.groupby("Fédération")["Total"].sum()

        # Store the totals for each federation in the dictionary
        for fed, total in grouped.items():
            if fed not in pop_data:
                pop_data[fed] = []
            pop_data[fed].append(total)

    # Calculate percentages for each federation
    percentages = {fed: sum(values) for fed, values in pop_data.items()}
    total_population = sum(percentages.values())
    percentages = {fed: (total / total_population) * 100 for fed, total in percentages.items()}

    return percentages
        




# def generate_histogram_pop_data(df, selected_location, selected_year):
# # Filter the data based on the provided location

#     filtered_data = df[df['Location'] == selected_location]

#     # Initialize empty lists for female and male data
#     female_data = []
#     male_data = []
#     year_values = []
#     #initialise la somme de toutes le femmes
#     count_female = 0

#      # Collect female and male data for the selected location and year
#     #somme des femmes
#     female_count = filtered_data[female_col].values[0]
#     female_data = filtered_data['Female_Column_Name'].tolist()  # Remplacez 'Female_Column_Name' par le nom réel de votre colonne de données féminines
#     male_data = filtered_data['Male_Column_Name'].tolist()  # Remplacez 'Male_Column_Name' par le nom réel de votre colonne de données masculines
#     year_values.append(selected_year);
#     # Create a new DataFrame in wide-format
#     wide_format_data = pd.DataFrame(
#         {
#             "Female": female_data,
#             "Male": male_data,
#             "Year": year_values,
#         }
        
#     )

#     return wide_format_data

# LINE CHART FAIT CRASH LE DASHBOARD
def generate_linechart_data(federation_name, commune_name, age, gender):
    # Data wanted
    data_wanted = f"{gender} - {age}"

    # Initialize empty lists for licencees data
    licensees_data = []

    # Iterate through files
    for year in year_mapping:
        # Parse through the years
        df = year_mapping.get(year)

        # Filter the data based on the provided federation and commune
        filtered_data = df[
            (df["Fédération"] == federation_name) & (df["Commune"] == commune_name)
        ]

        # Append the data to the list
        licensees_data.append(filtered_data[data_wanted].values[0])

    wide_format_data = pd.DataFrame(
        {"Years": year_mapping.keys(), "Licensees": licensees_data, "Gender": gender}
    )

    return wide_format_data
