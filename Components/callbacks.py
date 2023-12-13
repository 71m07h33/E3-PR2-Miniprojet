from dash import Dash, Input, Output
from Dashboard.histogram import update_histogram
from Dashboard.heatmap import update_heatmap


def set_callbacks(app: Dash):
    # Define callback to update histogram based on user inputs
    @app.callback(
        Output("histogram", "figure"),
        [
            Input("sport-dropdown", "value"),
            Input("location-dropdown", "value"),
            Input("year-slider", "value"),
        ],
    )
    def callback_histogram(selected_sport, selected_location, selected_year):
        return update_histogram(selected_sport, selected_location, selected_year)

    # Define callback to update heatmap based on user inputs
    # @app.callback(
    #    Output("heatmap", "figure"),
    #    [
    #        Input("sport-dropdown", "value"),
    #        Input("year-slider", "value"),
    #    ],
    # )
    # def callback_heatmap(selected_sport, selected_year):
    #    return update_heatmap(selected_sport, selected_year)
