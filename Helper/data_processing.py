# Importation
import pandas as pd
import requests

# Lecture des base des données
df_2021 = pd.read_csv("./Data/lic-data-2021.csv", delimiter=";", encoding="utf-8")
df_2020 = pd.read_csv("./Data/lic-data-2020.csv", delimiter=";", encoding="utf-8")
df_2019 = pd.read_csv("./Data/lic-data-2019.csv", delimiter=";", encoding="utf-8")

# Création d'un dictionnaire pour facilement acceder aux bases de données
year_mapping = {
    2021: df_2021,
    2020: df_2020,
    2019: df_2019,
}

# Catégories d'âge
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

##################
### PARAMETRES ###
##################


def update_departement_dropdown(selected_year):
    """
    Update the departement dropodown

    Parameters:
        - selected_year (int): The year selected
    """
    # Récuperation des departments disponibles en fonction de l'année
    departement_options = year_mapping.get(selected_year)["Département"].unique()

    # Créer une liste d'option pour notre dropdown
    options = [{"label": commune, "value": commune} for commune in departement_options]

    return options


def update_commune_dropdown(selected_department):
    """
    Update the commune dropodown

    Parameters:
        - selected_department (str): The departement selected
    """
    # Récuperation des communes disponible dans le département demandé
    commune_options = year_mapping.get(2019)[
        year_mapping.get(2019)["Département"] == int(selected_department)
    ]["Commune"].unique()

    # Créer une liste d'option pour notre dropdown
    options = [{"label": commune, "value": commune} for commune in commune_options]

    return options


def update_sport_dropdown(selected_commune):
    """
    Update the sport dropodown

    Parameters:
        - selected_commune (str): The sport selected
    """
    # Récuperation des sports disponible dans la commune demandée
    sport_options = year_mapping.get(2019)[
        year_mapping.get(2019)["Commune"] == selected_commune
    ]["Fédération"].unique()

    # Créer une liste d'option pour notre dropdown
    options = [{"label": commune, "value": commune} for commune in sport_options]

    return options


#################
### RESULTATS ###
#################


def generate_camembert_data(commune_name, selected_year):
    """
    Generate the data necessary to create a camembert

    Parameters:
        - commune_name (str): The commune selected
        - selected_year (int): The year selected
    """
    # Création d'un dictionnaire pour stocker les statistiques
    pop_data = {}

    # Choix de la bonne base de données
    df = year_mapping[selected_year]

    # Filtrer les données pour la commune sélectionnées
    filtered_data = df[df["Commune"] == commune_name]

    # Grouper par fédération et calculer la population totale pour chaque fédération
    grouped = filtered_data.groupby("Fédération")["Total"].sum()

    # Stocker les totaux pour chaque fédération dans le dictionnaire
    for fed, total in grouped.items():
        if fed not in pop_data:
            pop_data[fed] = []
        pop_data[fed].append(total)

    # Calculer les pourcentages pour chaque fédération et l'ajoute au dictionnaire
    percentages = {fed: sum(values) for fed, values in pop_data.items()}
    total_population = sum(percentages.values())

    percentages = {
        fed: (total / total_population) * 100 for fed, total in percentages.items()
    }

    # Simplification du camembert par le regroupement des sports minoritaires
    total_population = sum(percentages.values())

    # Filtre des fédération représentant moins de 3% des licensiées
    other_federations = sum(
        value for value in percentages.values() if (value / total_population) * 100 < 3
    )

    # Création d'un nouveau dictionnaire avec "Other fédération"
    modified_percentages = {
        fed: (value / total_population) * 100
        for fed, value in percentages.items()
        if (value / total_population) * 100 >= 3
    }
    modified_percentages["Other Federation"] = other_federations

    return modified_percentages


def generate_histogram_data(federation_name, commune_name, selected_year):
    """
    Generate the data necessary to create a histogram

    Parameters:
        - federation_name (str): The sport selected
        - commune_name (str): The commune selected
        - selected_year (int): The year selected
    """
    # Choix de la base de données
    df = year_mapping[selected_year]

    # Filtre les données disponible en fonction du sport et de la commune
    filtered_data = df[
        (df["Fédération"] == federation_name) & (df["Commune"] == commune_name)
    ]

    # Initialisation des listes vides
    female_data = []
    male_data = []
    year_values = []

    # Iteration à travers les catégories d'âge
    for age_category in age_categories:
        female_col = f"F - {age_category}"
        male_col = f"H - {age_category}"

        # Extrait les données en fonction du genre
        female_count = filtered_data[female_col].values[0]
        male_count = filtered_data[male_col].values[0]

        # Rajouter les données extraites aux listes
        female_data.append(female_count)
        male_data.append(male_count)
        year_values.append(selected_year)

    # Créer une nouvelles dataframe à partir des listes
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
    """
    Generate the data necessary to create a line chart

    Parameters:
        - federation_name (str): The sport selected
        - commune_name (str): The commune selected
        - age (int): The age selected
        - gender (str): The gender selected
    """
    # Données recherchées
    data_wanted = f"{gender} - {age}"

    # Initialisation d'une liste vides
    licensees_data = []

    # Itération à travers les différentes bases de données
    for year in year_mapping:
        # Choisis la base de données
        df = year_mapping.get(year)

        # Filtre les données en fonction du sport et de la commune
        filtered_data = df[
            (df["Fédération"] == federation_name) & (df["Commune"] == commune_name)
        ]

        # Rajoute les données filtrées à la liste
        licensees_data.append(filtered_data[data_wanted].values[0])

    # Créer une nouvelle dataframe à partir de la liste
    wide_format_data = pd.DataFrame(
        {"Years": year_mapping.keys(), "Licensees": licensees_data, "Gender": gender}
    )

    return wide_format_data


def generate_heatmap_data(
    federation_name, selected_year, wanted_data, selected_department
):
    """
    Generate the data necessary to create a heatmap

    Parameters:
        - federation_name (str): The sport selected
        - selected_year (int): The year selected
        - wanted_data (str): The data wanted
        - selected_department (str): The departement selected
    """
    # Choix de l'année
    df = year_mapping.get(selected_year)

    # Création d'une dataframe vide
    heatmap_df = pd.DataFrame(columns=["Commune", "Licensees", "Coordinates"])

    # Filtrer en fonction de la fédération et du départmement
    filtered_by_federation = df[df["Fédération"] == federation_name]

    clear_df = filtered_by_federation[
        filtered_by_federation["Département"] == int(selected_department)
    ]

    # Appelle d'une API pour récuperer les position des communes
    response = requests.get(
        f"https://geo.api.gouv.fr/departements/{selected_department}/communes?format=geojson"
    )
    data = response.json()

    # Pour chaque commune du départmeent
    for commune in data["features"]:
        # Récupération des données nécessaires
        commune_code = commune["properties"]["code"]
        coordinates = commune["geometry"]["coordinates"]

        # On traverse chaque ligne de la dataframe (pourrait être optimisé)
        for index, row in clear_df.iterrows():
            # Si on est sur la bonne commune
            if row["Code Commune"] == int(commune_code):
                # Récupère le nombre de licensiées
                licensees = row[wanted_data]

                # On rajoute la commune avec ses données à la dataframe finale
                row_to_append = {
                    "Commune": commune_code,
                    "Licensees": licensees,
                    "Coordinates": coordinates,
                }
                heatmap_df = pd.concat(
                    [heatmap_df, pd.DataFrame([row_to_append])], ignore_index=True
                )

    return heatmap_df
