import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Create Dash app
app = dash.Dash(__name__)

# Load the CSV data
df_2019 = pd.read_csv("./Data/lic-data-2019.csv", delimiter=";", encoding="latin1")
df_2018 = pd.read_csv("./Data/lic-data-2018.csv", delimiter=";", encoding="latin1")
df_2017 = pd.read_csv("./Data/lic-data-2017.csv", delimiter=";", encoding="latin1")
df_2016 = pd.read_csv("./Data/lic-data-2016.csv", delimiter=";", encoding="latin1")

# Data normalization
df_2016["nom_fed"] = df_2016["nom_fed"].str.replace(
    "Fédération Française", "FF", regex=False, case=False
)
df_2017["nom_fed"] = df_2017["nom_fed"].str.replace(
    "Fédération Française", "FF", regex=False, case=False
)

year_mapping = {
    2019: df_2019,
    2018: df_2018,
    2017: df_2017,
    2016: df_2016,
}

# Define the layout of the app
app.layout = html.Div(
    [
        html.H1("Licensees Dashboard"),
        # Dropdown for selecting a sport
        dcc.Dropdown(
            id="sport-dropdown",
            options=[
                {"label": sport, "value": sport}
                for sport in df_2019["nom_fed"].unique()
            ],
            value=df_2019["nom_fed"].unique()[0],  # Default selection
            multi=False,
            style={"width": "50%"},
        ),
        # Dropdown for selecting a location
        dcc.Dropdown(
            id="location-dropdown",
            options=[
                {"label": location, "value": location}
                for location in df_2019["libelle"].unique()
            ],
            value=df_2019["libelle"].unique()[0],  # Default selection
            multi=False,
            style={"width": "50%"},
        ),
        # Slider for selecting a year
        dcc.Slider(
            id="year-slider",
            min=2016,
            max=2019,
            value=2019,
            marks={str(year): str(year) for year in range(2016, 2020)},
            step=1,
        ),
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
        Input("year-slider", "value"),
    ],
)
def update_histogram(selected_sport, selected_location, selected_year):
    # Load data for the selected year
    df = year_mapping.get(selected_year)

    wide_df = generate_plotly_data(df, selected_sport, selected_location, selected_year)

    # Use color_discrete_map to specify colors for Female and Male
    color_discrete_map = {"Female": "pink", "Male": "blue"}

    fig = px.bar(
        wide_df,
        x="Age",
        y=["Female", "Male"],
        color_discrete_map=color_discrete_map,
        labels={"value": "Count"},
    )

    # Customize layout to make it more visually appealing
    fig.update_layout(
        title=f"Sport Participation in {selected_location} for {selected_sport} ({selected_year})",
        xaxis_title="Age Category",
        yaxis_title="Count",
        barmode="stack",  # Stack bars on top of each other
    )

    return fig


def generate_plotly_data(df, federation_name, commune_name, selected_year):
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
    i = 0
    for age_category in age_categories:
        female_col = f"l_{age_category}_f_{selected_year}"
        male_col = f"l_{age_category}_h_{selected_year}"

        print(female_data)
        print(male_data)

        # Extract female and male data for the specific age category
        female_count = filtered_data[female_col].values[0]
        male_count = filtered_data[male_col].values[0]

        # Append data to respective lists
        female_data.append(female_count)
        male_data.append(male_count)
        print(i)
        i += 1

    # Create a new DataFrame in wide-format
    wide_format_data = pd.DataFrame(
        {"Age": age_categories, "Female": female_data, "Male": male_data}
    )

    return wide_format_data


if __name__ == "__main__":
    app.run_server(debug=True)
