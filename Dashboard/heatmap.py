import folium
from Helper.data_processing import generate_heatmap_data


def update_heatmap(selected_sport, selected_year, selected_age, selected_gender):
    # Creation de la carte
    coords = (46.539758, 2.430331)
    map = folium.Map(location=coords, tiles="OpenStreetMap", zoom_start=5)

    # Donnée rcherché
    wanted_data = f"{selected_gender} - {selected_age}"

    # Creation de la dataframe
    df = generate_heatmap_data(selected_sport, selected_year, wanted_data)
    print(df)

    for row in df.iterrows():
        commune = row[1][0]
        latitude = row[1][2]
        longitude = row[1][3]
        radius = row[1][1]

        print(f"commune : {commune}")
        print(f"latitude : {latitude}")
        print(f"Longitude : {longitude}")
        print(f"Licensiées : {radius}\n\n")

        folium.CircleMarker(
            location=(latitude, longitude),
            radius=radius,
            color="crimson",
            fill=True,
            fill_color="crimson",
        ).add_to(map)

    # Retour de la cart
    return map._repr_html_()
