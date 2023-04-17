import pandas as pd
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import Dash

app = Dash(__name__)

class sampleDashboard:
    dashData = {}

    def load_data_frame(self):
        data = [{'nation':'South Korea', 'medal': 'gold', 'count': 24}]
        return pd.DataFrame(data)


sample_dashboard = sampleDashboard()


def getLayout():
    # df = sample_dashboard.load_data_frame()

    return [
                    html.Div(children=[
                            dcc.Graph(id='graph')
                    ])
    ]

@app.callback(Output('graph', 'figure'),
              Input('url', 'search'),
              State('url', 'pathname'))
def update_figure(search, pathname):
    df = sample_dashboard.load_data_frame()
    fig = {}
    if not df.empty:
        fig = px.bar(df, x="nation", y="count", title="graph")
    return fig
