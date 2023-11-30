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
def update_histogram(selected_sport, selected_location):  # , selected_year):
    filtered_df = df[
        (df["nom_fed"] == selected_sport)
        & (df["libelle"] == selected_location)
        # & (df["Year"] == selected_year)
    ]

    # Define age-related columns based on your CSV fields
    age_columns = [
        "l_0_4_2019",
        "l_5_9_2019",
        "l_10_14_2019",
        "l_15_19_2019",
        "l_20_29_2019",
        "l_30_44_2019",
        "l_45_59_2019",
        "l_60_74_2019",
        "l_75_2019",
    ]

    male_columns = [
        "l_0_4_h_2019",
        "l_5_9_h_2019",
        "l_10_14_h_2019",
        "l_15_19_h_2019",
        "l_20_29_h_2019",
        "l_30_44_h_2019",
        "l_45_59_h_2019",
        "l_60_74_h_2019",
        "l_75_h_2019",
    ]

    female_columns = [
        "l_0_4_f_2019",
        "l_5_9_f_2019",
        "l_10_14_f_2019",
        "l_15_19_f_2019",
        "l_20_29_f_2019",
        "l_30_44_f_2019",
        "l_45_59_f_2019",
        "l_60_74_f_2019",
        "l_75_f_2019",
    ]

    # Create color map to change the color of Male and Female bars
    color_map = {
        "l_0_4_h_2019": "blue",
        "l_5_9_h_2019": "blue",
        "l_10_14_h_2019": "blue",
        "l_15_19_h_2019": "blue",
        "l_20_29_h_2019": "blue",
        "l_30_44_h_2019": "blue",
        "l_45_59_h_2019": "blue",
        "l_60_74_h_2019": "blue",
        "l_75_h_2019": "blue",
        "l_0_4_f_2019": "pink",
        "l_5_9_f_2019": "pink",
        "l_10_14_f_2019": "pink",
        "l_15_19_f_2019": "pink",
        "l_20_29_f_2019": "pink",
        "l_30_44_f_2019": "pink",
        "l_45_59_f_2019": "pink",
        "l_60_74_f_2019": "pink",
        "l_75_f_2019": "pink",
    }

    # Create a new column "Gender" based on the available male and female columns
    filtered_df["Gender"] = filtered_df[male_columns].sum(axis=1) - filtered_df[
        female_columns
    ].sum(axis=1)

    # Reshape the DataFrame for stacked histograms
    stacked_df = pd.melt(
        filtered_df,
        id_vars=["Gender"],
        value_vars=male_columns + female_columns,
        var_name="Age",
        value_name="Licensees",
    )

    # Create histogram using Plotly Express
    fig = px.bar(
        stacked_df,
        x="Age",
        y="Licensees",
        color="Gender",
        color_discrete_map=color_map,
        labels={"Licensees": "Number of Licensees", "Age": "Age Group"},
        title=f"Licensees Distribution for {selected_sport} in {selected_location}",  # ({selected_year})",
        barmode="stack",
        category_orders={"Age": age_columns},
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
