import plotly.express as px
from Helper.data_processing import year_mapping, generate_histogram_data


def update_histogram(selected_sport, selected_location, selected_year):
    # Load data for the selected year
    df = year_mapping.get(selected_year)

    wide_df = generate_histogram_data(
        df, selected_sport, selected_location, selected_year
    )

    # Use color_discrete_map to specify colors for Female and Male
    color_discrete_map = {"Female": "pink", "Male": "blue"}

    fig = px.bar(
        wide_df,
        x="Age",
        y=["Female", "Male"],
        color_discrete_map=color_discrete_map,
        labels={"value": "Licenciés"},
        animation_frame="Year",  # Specify the animation frame, A FAIRE : ANIMATION
    )

    # Customize layout to make it more visually appealing
    fig.update_layout(
        xaxis_title="Catégorie",
        yaxis_title="Licenciés",
        barmode="stack",  # Stack bars on top of each other
    )

    return fig
