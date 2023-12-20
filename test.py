import pandas as pd

# Replace 'your_file.csv' with the actual file path
file_path_licensees = "./Data/lic-data-2019.csv"
file_path_geo = "./Data/geolocalisation.csv"

# Read the first 10 lines of the CSV file into a DataFrame
df_licensees = pd.read_csv(file_path_licensees, nrows=10, sep=";", encoding="utf-8")

print(df_licensees)

df_geoloc = pd.read_csv(file_path_geo, nrows=10, sep=",", encoding="utf-8")
print(df_geoloc)

merged_df = pd.merge(
    df_licensees,
    df_geoloc,
    left_on="Code Commune",
    right_on="code_commune_INSEE",
    how="left",  # left
)

print(merged_df)

merged_df = pd.merge(
    df_licensees,
    df_geoloc,
    left_on="Code Commune",
    right_on="code_commune_INSEE",
    how="right",  # left
)

print(merged_df)

merged_df = pd.merge(
    df_licensees,
    df_geoloc,
    left_on="Code Commune",
    right_on="code_commune_INSEE",
    how="outer",  # left
)

print(merged_df)

merged_df = pd.merge(
    df_licensees,
    df_geoloc,
    left_on="Code Commune",
    right_on="code_commune_INSEE",
    how="inner",  # left
)

print(merged_df)
