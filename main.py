import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the CSV data
df = pd.read_csv("./Data/lic-data-2019.csv", delimiter=";", encoding="latin1")

# Create Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    [
        html.H1("Licensees Dashboard"),
        # Dropdown for selecting a sport
        dcc.Dropdown(
            id="sport-dropdown",
            options=[
                {"label": sport, "value": sport} for sport in df["nom_fed"].unique()
            ],
            value=df["nom_fed"].unique()[0],  # Default selection
            multi=False,
            style={"width": "50%"},
        ),
        # Dropdown for selecting a location
        dcc.Dropdown(
            id="location-dropdown",
            options=[
                {"label": location, "value": location}
                for location in df["libelle"].unique()
            ],
            value=df["libelle"].unique()[0],  # Default selection
            multi=False,
            style={"width": "50%"},
        ),
        # Slider for selecting a year
        # dcc.Slider(
        #     id="year-slider",
        #     min=2016,
        #     max=2019,
        #     value=2016,
        #     marks={str(year): str(year) for year in range(2016, 2020)},
        #     step=1,
        # ),
        # Histogram with Plotly Express
        dcc.Graph(id="histogram"),
    ]
)


# Define callback to update histogram based on user inputs
@app.callback(
    Output("histogram", "figure"),
    [
        Input("sport-dropdown", "value"),
        Input("location-dropdown", "value"),
        # Input("year-slider", "value"),
    ],
)
def update_histogram(selected_sport, selected_location):
    wide_df = generate_plotly_data(selected_sport, selected_location)

    # Use color_discrete_map to specify colors for Female and Male
    color_discrete_map = {"Female": "pink", "Male": "blue"}

    fig = px.bar(
        wide_df,
        x="Age",
        y=["Female", "Male"],
        color_discrete_map=color_discrete_map,
    )

    return fig


def generate_plotly_data(federation_name, commune_name):
    # Filter the data based on the provided federation and commune
    filtered_data = df[
        (df["nom_fed"] == federation_name) & (df["libelle"] == commune_name)
    ]

    # Define age categories
    age_categories = [
        "0_4",
        "5_9",
        "10_14",
        "15_19",
        "20_29",
        "30_44",
        "45_59",
        "60_74",
        "75",
    ]

    # Initialize empty lists for female and male data
    female_data = []
    male_data = []

    # Iterate through age categories
    for age_category in age_categories:
        female_col = f"l_{age_category}_f_2019"
        male_col = f"l_{age_category}_h_2019"

        # Extract female and male data for the specific age category
        female_count = filtered_data[female_col].values[0]
        male_count = filtered_data[male_col].values[0]

        # Append data to respective lists
        female_data.append(female_count)
        male_data.append(male_count)

    # Create a new DataFrame in wide-format
    wide_format_data = pd.DataFrame(
        {"Age": age_categories, "Female": female_data, "Male": male_data}
    )

    return wide_format_data


if __name__ == "__main__":
    app.run_server(debug=True)
