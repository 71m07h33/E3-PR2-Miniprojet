import plotly.express as px
from Helper.data_processing import generate_linechart_data


def update_linechart(selected_sport, selected_location, selected_age, selected_gender):
    """
    Create and update the linechart

    Parameters:
        - selected_sport (str): The sport selected
        - selected_location (str): The commune selected
        - selected_age (int): The age selected
        - selected_gender (str): The gender selected
    """
    # Creation de la dataframe
    wide_df = generate_linechart_data(
        selected_sport, selected_location, selected_age, selected_gender
    )

    # Creation du graphique
    fig = px.line(wide_df, x="Years", y="Licensees")

    # Personnalisation du graphique
    fig.update_layout(
        xaxis_title="Années",
        yaxis_title="Licenciés",
    )

    return fig
