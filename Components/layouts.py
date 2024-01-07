# Importation
from dash import dcc, html
from Helper.data_processing import (
    year_mapping,
    age_categories,
)
from Dashboard.heatmap import update_heatmap


def set_layout(app):
    """
    Set the layout of the application

    Parameters:
        - app (Dash application): The Dash application
    """
    # Page Web
    app.layout = html.Div(
        [
            # Titre
            html.H1("Le sport en France"),
            # Paramètres
            html.Div(
                className="quizz",
                children=[
                    html.H2("Paramètres"),
                    # Age
                    html.H5("Âge"),
                    dcc.Dropdown(
                        id="age-dropdown",
                        options=age_categories,
                        multi=False,
                        style={"width": "50%"},
                    ),
                    # Genre
                    html.H5("Genre"),
                    dcc.Dropdown(
                        id="gender-dropdown",
                        options=["H", "F"],
                        multi=False,
                        style={"width": "50%"},
                    ),
                    # Departement
                    html.H5("Département"),
                    dcc.Dropdown(
                        id="departement-dropdown",
                        options=year_mapping.get(2019)["Département"].unique(),
                        multi=False,
                        style={"width": "50%"},
                    ),
                    # Commune
                    html.H5("Commune"),
                    dcc.Dropdown(
                        id="commune-dropdown",
                        options=[],
                        multi=False,
                        style={"width": "50%"},
                    ),
                    # Sport
                    html.H5("Fédération Francaise de sport"),
                    dcc.Dropdown(
                        id="sport-dropdown",
                        options=[],
                        multi=False,
                        style={"width": "50%"},
                    ),
                    # Année
                    html.H5("Année de la récolte de donnée"),
                    dcc.Dropdown(
                        id="year-slider",
                        options=[{"label": i, "value": i} for i in range(2019, 2022)],
                        multi=False,
                        style={"width": "50%"},
                    ),
                ],
            ),
            # Résultats
            html.Div(
                className="result",
                children=[
                    html.H2("Résultats"),
                    html.Div(
                        [
                            # Camembert
                            html.H5("Sports les plus pratiqué dans votre commune"),
                            dcc.Graph(
                                id="camembert_graph",
                                style={"width": "100%"},
                            ),
                        ]
                    ),
                    html.Div(
                        [
                            # Histogramme
                            html.H5(
                                "Histogramme des pratiquants de votre sport dans votre commune ?"
                            ),
                            dcc.Graph(id="histogram"),
                            # Graphique
                            html.H5(
                                "Comment evolue la pratique de votre sport dans votre catégorie ?"
                            ),
                            dcc.Graph(id="graph"),
                        ]
                    ),
                    html.Div(
                        [
                            # Carte
                            html.H5(
                                "Carte des pratiquants de votre sport dans votre départements"
                            ),
                            html.Iframe(
                                id="heatmap",
                                width="100%",
                                height="500",
                            ),
                        ]
                    ),
                ],
            ),
            # Footer
            html.P("Valentin L. & Timothée D.   •   ESIEE Paris   •   2024"),
        ]
    )
