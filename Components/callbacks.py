# Importation
from dash import Dash, Input, Output
from Dashboard.histogram import update_histogram
from Dashboard.linechart import update_linechart
from Dashboard.heatmap import update_heatmap
from Dashboard.camembert import update_camembert
from Helper.data_processing import (
    update_commune_dropdown,
    update_sport_dropdown,
    update_departement_dropdown,
)


def set_callbacks(app: Dash):
    """
    Set the callbacks of the application

    Parameters:
        - app (Dash application): The Dash application
    """
    ##################
    ### PARAMETRES ###
    ##################

    # Dropdown des communes dans un département
    @app.callback(
        Output("departement-dropdown", "options"),
        [
            Input("year-dropdown", "value"),
        ],
    )
    def callback_departement_dropdown(selected_department):
        return update_departement_dropdown(selected_department)

    # Dropdown des communes dans un département
    @app.callback(
        Output("commune-dropdown", "options"),
        [
            Input("departement-dropdown", "value"),
        ],
    )
    def callback_commune_dropdown(selected_department):
        return update_commune_dropdown(selected_department)

    # Dropdown des sports dans une communes
    @app.callback(
        Output("sport-dropdown", "options"),
        [
            Input("commune-dropdown", "value"),
        ],
    )
    def callback_sport_dopdown(selected_department):
        return update_sport_dropdown(selected_department)

    #################
    ### RESULTATS ###
    #################

    # Camembert intéractif, évoluant en fonction des paramètres du dashboard
    @app.callback(
        Output(component_id="camembert_graph", component_property="figure"),
        [
            Input("commune-dropdown", "value"),
            Input("year-dropdown", "value"),
        ],
    )
    def callback_camembert(selected_location, selected_year):
        return update_camembert(selected_location, selected_year)

    # Histogramme intéractif, évoluant en fonction des paramètres du dashboard
    @app.callback(
        Output("histogram", "figure"),
        [
            Input("sport-dropdown", "value"),
            Input("commune-dropdown", "value"),
            Input("year-dropdown", "value"),
        ],
    )
    def callback_histogram(selected_sport, selected_commune, selected_year):
        return update_histogram(selected_sport, selected_commune, selected_year)

    # Graphique intéractif, évoluant en fonction des paramètres du dashboard
    @app.callback(
        Output("graph", "figure"),
        [
            Input("sport-dropdown", "value"),
            Input("commune-dropdown", "value"),
            Input("age-dropdown", "value"),
            Input("gender-dropdown", "value"),
        ],
    )
    def callback_linechart(
        selected_sport, selected_location, selected_age, selected_gender
    ):
        return update_linechart(
            selected_sport, selected_location, selected_age, selected_gender
        )

    # Carte intéractive, évoluant en fonction des paramètres du dashboard
    @app.callback(
        Output("heatmap", "srcDoc"),
        [
            Input("sport-dropdown", "value"),
            Input("year-dropdown", "value"),
            Input("age-dropdown", "value"),
            Input("gender-dropdown", "value"),
            Input("departement-dropdown", "value"),
        ],
    )
    def callback_heatmap(
        selected_sport,
        selected_year,
        selected_age,
        selected_gender,
        selected_department,
    ):
        return update_heatmap(
            selected_sport,
            selected_year,
            selected_age,
            selected_gender,
            selected_department,
        )
