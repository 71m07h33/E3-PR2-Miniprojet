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
            html.H1("Le sport en France"),
            html.Div(
                className="quizz",
                children=[
                    html.H2("A propos de vous ?"),
                    html.H5("Votre âge"),
                    # Dropdown for an age group to study
                    dcc.Dropdown(
                        id="age-dropdown",
                        options=age_categories,
                        # Default selection
                        value="10 à 14 ans",
                        multi=False,
                        style={"width": "50%"},
                    ),
                    html.H5("Votre genre"),
                    # Drop for a gender
                    dcc.Dropdown(
                        id="gender-dropdown",
                        options=["H", "F"],
                        value="H",
                        multi=False,
                        style={"width": "50%"},
                    ),
                    html.H5("Votre département"),
                    # Dropdown for selecting a departement
                    dcc.Dropdown(
                        id="departement-dropdown",
                        options=year_mapping.get(2019)["Département"].unique(),
                        # Default selection
                        value="74",
                        multi=False,
                        style={"width": "50%"},
                    ),
                    html.H5("Votre commune"),
                    # Dropdown for selecting a commune
                    dcc.Dropdown(
                        id="commune-dropdown",  # Location become commune
                        options=year_mapping.get(2019)["Commune"].unique(),
                        # Default selection
                        value="Chamonix-Mont-Blanc",
                        multi=False,
                        style={"width": "50%"},
                    ),
                    html.H5("Votre sport"),
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
                    html.H5("L'année d'étude"),
                    # Slider for selecting a year
                    dcc.Dropdown(
                        id="year-slider",
                        options=[{"label": i, "value": i} for i in range(2019, 2022)],
                        value=2019,
                        multi=False,
                        style={"width": "50%"},
                    ),
                ],
            ),
            html.Div(
                className="result",
                children=[
                    html.H2("Les Résultats"),
                    html.Div(
                        [
                            html.H5("Les sports les plus pratiqué dans votre commune"),
                            # Camembert des sports les plus pratiqué dans la région
                            dcc.Graph(
                                id="camembert_graph",
                                style={"width": "100%"},
                            ),
                        ]
                    ),
                    html.Div(
                        [
                            html.H5("Qui pratique votre sport dans votre commune ?"),
                            # Histogram with Plotly Express
                            dcc.Graph(id="histogram"),
                            html.H5(
                                "Comment evolue la pratique de votre sport dans votre catégorie ?"
                            ),
                            # Line chart for sport's evolution thourghout the years
                            dcc.Graph(id="graph"),
                        ]
                    ),
                    html.Div(
                        [
                            html.H5(
                                "Où se situent les plus grand pratiquants dans votre déparetments ?"
                            ),
                            html.Iframe(
                                id="heatmap",
                                srcDoc=update_heatmap(
                                    "FF de Ski", 2019, "10 à 14 ans", "H", "74"
                                ),
                                width="100%",
                                height="500",
                            ),
                        ]
                    ),
                ],
            ),
            html.P("Fait avec ❤️ par Valentin L. et Timothée D."),
        ]
    )
