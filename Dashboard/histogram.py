# Importation
import plotly.express as px
from Helper.data_processing import generate_histogram_data


def update_histogram(selected_sport, selected_location, selected_year):
    """
    Create and update the histogram

    Parameters:
        - selected_sport (str): The sport selected
        - selected_location (str): The commune selected
        - selected_year (int): The year selected
    """
    # Création d'une dataframe
    wide_df = generate_histogram_data(selected_sport, selected_location, selected_year)

    # Dictionnaire de couleur
    color_discrete_map = {"Female": "pink", "Male": "blue"}

    # Création de l'histogramme
    fig = px.bar(
        wide_df,
        x="Age",
        y=["Female", "Male"],
        color_discrete_map=color_discrete_map,
        labels={"value": "Licenciés"},
    )

    # Personnalisation de l'histogramme
    fig.update_layout(
        xaxis_title="Catégorie",
        yaxis_title="Licenciés",
        barmode="stack",
    )

    return fig
