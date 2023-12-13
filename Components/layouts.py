from dash import dcc, html
from Helper.data_processing import year_mapping, age_categories


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
                    for sport in year_mapping.get(2019)["Fédération"].unique()
                ],
                value=year_mapping.get(2019)["Fédération"].unique()[
                    0
                ],  # Default selection
                multi=False,
                style={"width": "50%"},
            ),
            # Dropdown for selecting a location
            dcc.Dropdown(
                id="location-dropdown",
                options=year_mapping.get(2019)["Commune"].unique(),
                # Default selection
                value=year_mapping.get(2019)["Commune"].unique()[0],
                multi=False,
                style={"width": "50%"},
            ),
            # Slider for selecting a year
            dcc.Slider(
                id="year-slider",
                min=2019,
                max=2021,
                value=2019,
                marks={
                    str(year): str(year) for year in range(2019, 2022)
                },  # ETENDRE A 2017 PUIS 2014 SI FONCTIONNELLE ET TEMPS
                step=1,
            ),
            # Histogram with Plotly Express
            dcc.Graph(id="histogram"),
            # Dropdown for an age group to study
            dcc.Dropdown(
                id="age-dropdown",
                options=age_categories,
                # Default selection
                value="10 à 14 ans",
                multi=False,
                style={"width": "50%"},
            ),
            # Drop for a gender
            dcc.Dropdown(
                id="gender-dropdown",
                options=["H", "F"],
                value="H",
                multi=False,
                style={"width": "50%"},
            ),
            # Line chart for sport's evolution thourghout the years
            dcc.Graph(id="graph"),
        ]
    )
