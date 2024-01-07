import plotly.express as px
from Helper.data_processing import generate_linechart_data


def update_linechart(selected_sport, selected_location, selected_age, selected_gender):
    # Create a wide data frame
    wide_df = generate_linechart_data(
        selected_sport, selected_location, selected_age, selected_gender
    )

    fig = px.line(wide_df, x="Years", y="Licensees")

    fig.update_layout(
        xaxis_title="Années",
        yaxis_title="Licenciés",
    )

    return fig
