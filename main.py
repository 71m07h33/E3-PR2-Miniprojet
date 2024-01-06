import dash
from Components.layouts import set_layout
from Components.callbacks import set_callbacks

# Create Dash app
app = dash.Dash(__name__)

set_layout(app)

set_callbacks(app)


if __name__ == "__main__":
    app.run_server(debug=True)
    