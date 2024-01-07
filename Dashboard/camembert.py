# #valentin's page :)
import plotly.express as px
from Helper.data_processing import generate_camembert_data, year_mapping


def update_camembert(selected_location, selected_year):
    wide_df = generate_camembert_data(selected_location, selected_year)

    labels = list(wide_df.keys())
    values = list(wide_df.values())

    fig = px.pie(
        values=values,
        names=labels,
        title=f"Part de chaque sport pratiqué à {selected_location}",
    )

    fig.update_traces(hole=0)

    return fig
