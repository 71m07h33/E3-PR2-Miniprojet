# Importation
import plotly.express as px
from Helper.data_processing import generate_camembert_data


def update_camembert(selected_location, selected_year):
    """
    Create and update the camembert

    Parameters:
        - selected_location (str): The location selected
        - selected_year (int): The year selected
    """
    # Crétion de la dataframe
    wide_df = generate_camembert_data(selected_location, selected_year)

    # Création du camembert
    fig = px.pie(
        values=list(wide_df.values()),
        names=list(wide_df.keys()),
    )

    # Mise à jours du camembert
    fig.update_traces()

    return fig
