# Importation
import dash
from Components.layouts import set_layout
from Components.callbacks import set_callbacks

# Création d'une application Dash
app = dash.Dash(__name__)

# Création du layout
set_layout(app)

# Création des callbacks
set_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
