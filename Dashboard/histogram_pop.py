# #valentin's page :)
# import plotly.express as px
# from Helper.data_processing import generate_histogram_pop_data, year_mapping, generate_histogram_data


# def update_histogrampop( selected_location, selected_year):
#     # Load data for the selected year
#     df = year_mapping.get(selected_year)

#     wide_df = generate_histogram_pop_data(
#         df, selected_location,selected_year
#     )
    
#     # Use color_discrete_map to specify colors for Female and Male
#     color_discrete_map = {"Female": "pink", "Male": "blue"}

#     fig = px.histogram(wide_df, x='Federation', y='Population', title='Population by Federation')
#     return fig

#     return fig
