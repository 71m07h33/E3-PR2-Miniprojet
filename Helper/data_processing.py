# data_processing.py
import pandas as pd
import requests

# Define the API endpoint
# geolocalisation_json = requests.get(
#     "https://geo.api.gouv.fr/communes?fields=code,nom,centre"
# ).json()

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
]

# Create a dictionary with commune codes as keys and coordinates as values
# coordinates_dict = coordinates_dict = {
#     entry["code"]: entry["centre"]["coordinates"] for entry in geolocalisation_json
# }


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


def generate_heatmap_data(
    federation_name, selected_year, wanted_data, selected_department
):
    # Choix de l'année
    df = year_mapping.get(selected_year)

    heatmap_df = pd.DataFrame(columns=["Commune", "Licensees", "Coordinates"])

    # Filtrer en fonction de la fédération
    filtered_by_federation = df[df["Fédération"] == federation_name]

    clear_df = filtered_by_federation[
        filtered_by_federation["Département"] == int(selected_department)
    ]

    response = requests.get(
        f"https://geo.api.gouv.fr/departements/{selected_department}/communes?format=geojson"
    )
    data = response.json()

    for commune in data["features"]:
        commune_code = commune["properties"]["codesPostaux"][0]
        coordinates = commune["geometry"]["coordinates"]

        match = clear_df.loc[clear_df["Code Commune"] == int(commune_code), wanted_data]

        if not match.empty:
            row_to_append = {
                "Commune": commune_code,
                "Licensees": match.iloc[0],
                "Coordinates": coordinates,
            }
            print(f"Commune: {commune_code} -> {match.iloc[0]}")

            heatmap_df = pd.concat(
                [heatmap_df, pd.DataFrame([row_to_append])], ignore_index=True
            )

    return heatmap_df
