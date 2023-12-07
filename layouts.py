from dash import dcc, html
from data_processing import year_mapping


def set_layout(app):
    # Define the layout of the app
    app.layout = html.Div(
        [
            html.H1("Licensees Dashboard"),
            # Dropdown for selecting a sport
            dcc.Dropdown(
                id="sport-dropdown",
                options=[
                    {"label": sport, "value": sport}
                    for sport in year_mapping.get(2019)["nom_fed"].unique()
                ],
                value=year_mapping.get(2019)["nom_fed"].unique()[
                    0
                ],  # Default selection
                multi=False,
                style={"width": "50%"},
            ),
            # Dropdown for selecting a location
            dcc.Dropdown(
                id="location-dropdown",
                options=[
                    {"label": location, "value": location}
                    for location in year_mapping.get(2019)["libelle"].unique()
                ],
                value=year_mapping.get(2019)["libelle"].unique()[
                    0
                ],  # Default selection
                multi=False,
                style={"width": "50%"},
            ),
            # Slider for selecting a year
            dcc.Slider(
                id="year-slider",
                min=2016,
                max=2019,
                value=2019,
                marks={str(year): str(year) for year in range(2016, 2020)},
                step=1,
            ),
            # Histogram with Plotly Express
            dcc.Graph(id="histogram"),
        ]
    )
