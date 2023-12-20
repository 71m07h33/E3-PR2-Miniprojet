# data_processing.py
import pandas as pd


# Load the CSV data
geolocalisation_df = pd.read_csv(
    "./Data/geolocalisation.csv", delimiter=",", encoding="utf-8"
)
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


def generate_heatmap_data(federation_name, selected_year, wanted_data):
    # Choose the correct csv file
    licensees_df = year_mapping.get(selected_year)

    merged_df = pd.merge(
        licensees_df,
        geolocalisation_df,
        left_on="Code Commune",
        right_on="code_commune_INSEE",
        how="inner",  # left
    )

    print(merged_df.head(10))

    # Wanted columns
    wanted_columns = [wanted_data, "latitude", "longitude", "Code Commune"]

    filtered_data = merged_df[(merged_df["Fédération"] == federation_name)]
    filtered_data = filtered_data[wanted_columns]

    print(filtered_data.head(10))

    return filtered_data
