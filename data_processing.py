# data_processing.py
import pandas as pd


# Load the CSV data
df_2019 = pd.read_csv("./Data/lic-data-2019.csv", delimiter=";", encoding="latin1")
df_2018 = pd.read_csv("./Data/lic-data-2018.csv", delimiter=";", encoding="latin1")
df_2017 = pd.read_csv("./Data/lic-data-2017.csv", delimiter=";", encoding="latin1")

# create nd csv files but they are empty for now
for year in range(2017, 2020, 1):
    nd = open(f"./Data/nd-{year}.csv")
    nd.close()


year_mapping = {
    2019: df_2019,
    2018: df_2018,
    2017: df_2017,
}


def generate_plotly_data(df, federation_name, commune_name, selected_year):
    # Filter the data based on the provided federation and commune
    filtered_data = df[
        (df["nom_fed"] == federation_name) & (df["libelle"] == commune_name)
    ]

    # Define age categories
    age_categories = [
        "0_4",
        "5_9",
        "10_14",
        "15_19",
        "20_29",
        "30_44",
        "45_59",
        "60_74",
        "75",
    ]

    # Initialize empty lists for female and male data
    female_data = []
    male_data = []
    year_values = []

    # Iterate through age categories
    for age_category in age_categories:
        female_col = f"l_{age_category}_f_{selected_year}"
        male_col = f"l_{age_category}_h_{selected_year}"

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


def data_treatement():
    # Data normalization
    df_2017["nom_fed"] = df_2017["nom_fed"].str.replace(
        "Fédération Française", "FF", regex=False, case=False
    )

    # Suppression sport incompatible
    federation_list_path = "./Data/liste-federation.xlsx"
    federation_list_excel = pd.ExcelFile(federation_list_path)

    # Iterate through each sheet and convert to CSV
    for sheet_name in federation_list_excel.sheet_names:
        # Read the sheet
        nd = pd.read_excel(federation_list_path, sheet_name)

        # Specify the path for the CSV file (adjust the path and file name as needed)

        csv_file_path = f"./Data/nd-{sheet_name}.csv"

        # Write the sheet to CSV
        nd.to_csv(csv_file_path, index=False)

        # On vient de créer les fichiers csv qui nous interessent
        # Reste à les parse pour faire une liste de sport problématique et les supprimer de nos datas

    federations_with_nd = []

    federations_with_nd += get_federations_with_nd("./Data/nd-2019.csv")
    federations_with_nd += get_federations_with_nd("./Data/nd-2018.csv")
    federations_with_nd += get_federations_with_nd("./Data/nd-2017.csv")
    # Supprimer doublon
    # Si temps, rajouter 2016

    remove_rows_by_federation("./Data/lic-data-2019.csv", federations_with_nd)
    # Si on supprime de 2019, on ne le propose plus a l'utilisateur donc plus de problème
    # Parse la collone des nd, si nd, retourner 2 cases en arrières et get FF
    # Faire une liste de FF à supprimer, puis supp FF de fédé 2019


def get_federations_with_nd(filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Filter rows where "lic-data-2019" column has the value "n.d."
    filtered_df = df[df["lic-data-2019"] == "n.d."]

    # Extract the "Libellé fédération" values from the filtered rows
    federations_with_nd = filtered_df["Code fédération"].tolist()

    return federations_with_nd


def remove_rows_by_federation(csv_filename, federations_to_remove):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_filename)

    # Filter rows where "fed_2019" is not in the provided list
    filtered_df = df[~df["fed_2019"].isin(federations_to_remove)]

    # Write the filtered DataFrame back to the CSV file
    filtered_df.to_csv(csv_filename, index=False)


# supprimer sport problématique pre app
