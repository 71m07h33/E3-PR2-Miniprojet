from dash import Dash, Input, Output
from Dashboard.histogram import update_histogram
from Dashboard.linechart import update_linechart
from Dashboard.heatmap import update_heatmap


def set_callbacks(app: Dash):
    # Define callback to update histogram based on user inputs
    @app.callback(
        Output("histogram", "figure"),
        [
            Input("sport-dropdown", "value"),
            Input("commune-dropdown", "value"),
            Input("year-slider", "value"),
        ],
    )
    def callback_histogram(selected_sport, selected_commune, selected_year):
        return update_histogram(selected_sport, selected_commune, selected_year)

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

    # Define callback to update heatmap based on user inputs
    @app.callback(
        Output("heatmap", "srcDoc"),
        [
            Input("sport-dropdown", "value"),
            Input("year-slider", "value"),
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
