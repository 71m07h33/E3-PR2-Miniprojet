# #valentin's page :)
import plotly.express as px
from Helper.data_processing import generate_camembert_data, year_mapping


def update_camembert(location_dropdown_2, selected_year):
    

    wide_df = generate_camembert_data(
         location_dropdown_2, selected_year
    )
    labels = list(wide_df.keys())
    values = list(wide_df.values())

    fig = px.pie(
        values=values,
        names=labels,
        title=f"Part de chaque sport pratiqué à {location_dropdown_2}",
    )

    return fig
