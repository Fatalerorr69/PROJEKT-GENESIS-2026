import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import psutil

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

app.layout = dbc.Container([
    html.H1("⚡ GENESIS AETERNA HUD ⚡", className="text-center text-success my-4"),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("CPU STATUS"),
            dbc.CardBody(html.H2(id="cpu-usage", className="text-info"))
        ]), width=6),
        dbc.Col(dbc.Card([
            dbc.CardHeader("RAM STATUS"),
            dbc.CardBody(html.H2(id="ram-usage", className="text-warning"))
        ]), width=6),
    ]),
    dcc.Interval(id='update', interval=2000)
], fluid=True, style={'backgroundColor': '#0a0a0a', 'height': '100vh'})

@app.callback(
    [Output("cpu-usage", "children"), Output("ram-usage", "children")],
    [Input("update", "n_intervals")]
)
def update_stats(n):
    return f"{psutil.cpu_percent()}%", f"{psutil.virtual_memory().percent}%"

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050)
