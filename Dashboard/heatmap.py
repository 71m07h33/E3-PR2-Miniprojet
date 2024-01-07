import folium
import branca
from Helper.data_processing import generate_heatmap_data


# Dû au limitation de l'API (50 appels par seconde et par IP, il faudrait 10 minutes pour charger toute les communes. On fait alors par région)
def update_heatmap(
    selected_sport, selected_year, selected_age, selected_gender, selected_department
):
    # Default coordinates
    coords = (46.539758, 2.430331)
    # Create the map
    map = folium.Map(location=coords, tiles="OpenStreetMap", zoom_start=5)

    # Define the wanted data
    wanted_data = f"{selected_gender} - {selected_age}"

    # Generate the heatmap data
    df = generate_heatmap_data(
        selected_sport, selected_year, wanted_data, selected_department
    )

    # Create a FeatureGroup
    marker_layer = folium.FeatureGroup(name="Marker Layer")

    print(df.head(50))

    for index, row in df.iterrows():
        coords = row["Coordinates"]
        licensees = row["Licensees"]

        folium.CircleMarker(
            location=[coords[1], coords[0]],
            radius=licensees,  # Simplement changer couleur
            # color=cm(color),
            fill=True,
            # fill_color=cm(color),
            fill_color="crimson",
            fill_opacity=0.7,
            popup=f"Fédération: {selected_sport}\nCatégorie: {wanted_data}\nCommune: {row['Commune']}\nLicensees: {licensees}",
        ).add_to(marker_layer)

    marker_layer.add_to(map)
    folium.LayerControl().add_to(map)

    return map._repr_html_()
