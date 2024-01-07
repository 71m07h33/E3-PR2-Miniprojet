# Importation
import folium
from Helper.data_processing import generate_heatmap_data


def update_heatmap(
    selected_sport, selected_year, selected_age, selected_gender, selected_department
):
    """
    Create and update the heatmap

    Parameters:
        - selected_sport (str): The sport selected
        - selected_year (int): The year selected
        - selected_age (int): The age selected
        - selected_gender (str): The gender selected
        - selected_department (str): The departement selected
    """
    # Coordonnées du centre de la France
    coords = (46.539758, 2.430331)
    # Creation de la carte
    map = folium.Map(location=coords, tiles="OpenStreetMap", zoom_start=5)

    # Définition de la donnée recherché
    wanted_data = f"{selected_gender} - {selected_age}"

    # Création de la data frame
    df = generate_heatmap_data(
        selected_sport, selected_year, wanted_data, selected_department
    )

    # Creation de la couche de marker
    marker_layer = folium.FeatureGroup(name="Marker Layer")

    # Pour chaque communes
    for index, row in df.iterrows():
        coords = row["Coordinates"]
        licensees = row["Licensees"]

        # Ajouter un marker sur la couche
        folium.CircleMarker(
            location=[coords[1], coords[0]],
            radius=licensees,
            fill=True,
            fill_color="crimson",
            fill_opacity=0.7,
            popup=f"Fédération: {selected_sport}\nCatégorie: {wanted_data}\nCommune: {row['Commune']}\nLicensees: {licensees}",
        ).add_to(marker_layer)

    # Ajouter la couche à la carte
    marker_layer.add_to(map)
    folium.LayerControl().add_to(map)

    return map._repr_html_()
