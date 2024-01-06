# #valentin's page :)
import plotly.express as px
from Helper.data_processing import generate_camembert_data, year_mapping


def update_camembert(location_dropdown_2    ):
    

    wide_df = generate_camembert_data(
         location_dropdown_2
    )
    labels = list(wide_df.keys())
    values = list(wide_df.values())

    fig = px.pie(
        values=values,
        names=labels,
        title='Part of each Sport',
        hole=.10,
    )

    return fig
