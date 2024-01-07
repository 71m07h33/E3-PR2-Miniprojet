from dash import dcc, html
from Helper.data_processing import (
    year_mapping,
    age_categories,
)
from Dashboard.heatmap import update_heatmap


def set_layout(app):
    # Define the layout of the app
    app.layout = html.Div(
        [
            html.H1("Qui fait du sport aujourd'hui en France ?"),
            html.Div(
                [
                    html.P(
                        "Ceci est mon premier paragraphe introductif : Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et congue elit. Vestibulum in risus lacinia tortor pharetra aliquam non vel ex. Proin at diam justo. Nulla odio purus, rutrum nec dolor sed, iaculis interdum leo. Nulla massa sem, sagittis eget lorem a, gravida luctus orci"
                    ),
                    html.P(
                        "Ceci est mon decuième paragraphe introductif : Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et congue elit. Vestibulum in risus lacinia tortor pharetra aliquam non vel ex. Proin at diam justo. Nulla odio purus, rutrum nec dolor sed, iaculis interdum leo. Nulla massa sem, sagittis eget lorem a, gravida luctus orci"
                    ),
                ]
            ),
            # Dropdown for selecting a sport
            dcc.Dropdown(
                id="sport-dropdown",
                options=[
                    {"label": sport, "value": sport}
                    for sport in year_mapping.get(2019)["Fédération"].unique()
                ],
                # Default selection
                value="FF de Ski",
                multi=False,
                style={"width": "50%"},
            ),
            dcc.Dropdown(
                id="commune-dropdown",  # Location become commune
                options=year_mapping.get(2019)["Commune"].unique(),
                # Default selection
                value="Chamonix-Mont-Blanc",
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
            # Dropdown for selecting a location
            dcc.Dropdown(
                id="departement-dropdown",
                options=year_mapping.get(2019)["Département"].unique(),
                # Default selection
                value="74",
                multi=False,
                style={"width": "50%"},
            ),
            html.H1("Carte Folium"),
            html.Iframe(
                id="heatmap",
                srcDoc=update_heatmap("FF de Ski", 2019, "10 à 14 ans", "H", "74"),
                width="50%",
                height="400",
            ),
        ]
    )
