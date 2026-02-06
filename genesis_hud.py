import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import psutil

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
app.layout = dbc.Container([
    html.H1("GENESIS HUD v6.0", className="text-center text-success"),
    dbc.Row([
        dbc.Col(dbc.Card([dbc.CardHeader("CPU %"), dbc.CardBody(html.H2(id="cpu"))])),
        dbc.Col(dbc.Card([dbc.CardHeader("RAM %"), dbc.CardBody(html.H2(id="ram"))])),
    ]),
    dcc.Interval(id='ref', interval=1000)
], fluid=True)

@app.callback([Output("cpu", "children"), Output("ram", "children")], [Input("ref", "n_intervals")])
def up(n):
    return f"{psutil.cpu_percent()}%", f"{psutil.virtual_memory().percent}%"

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050)
