from dash import Dash, Input, Output
from Dashboard.histogram import update_histogram
from Dashboard.linechart import update_linechart
from Dashboard.camembert import update_camembert
# from Dashboard.histogram_pop import update_histogrampop
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

    @app.callback(
        Output("graph", "figure"),
        [
            Input("sport-dropdown", "value"),
            Input("location-dropdown", "value"),
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
    
    #callback for camembert
    @app.callback(
        Output(component_id='camembert_graph', component_property='figure'),
        [Input(component_id='location_dropdown_2', component_property='value'),
        ],
    )
    def callback_camembert(selected_location):
        return update_camembert(selected_location)
        


    # @app.callback(
    #     Output('histogram_pop', 'figure'),
    #     [
    #         Input('year-slider', 'value'),
    #         Input('location-dropdown', 'value')
    #     ]
    # )
    # def callback_histogrampop( selected_location, selected_year):
    #     return update_histogrampop( selected_location, selected_year)
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
