from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.express as px
import dash
from .app import app
    




data = [{'nation':'South Korea', 'medal': 'gold', 'count': 24}]
df = pd.DataFrame(data)

def getLayout():
    return [html.Div(children=[dcc.Graph(id='graph')])]


@app.callback(Output('graph', 'figure'),
              Input('url', 'search'),
              State('url', 'pathname'))
def update_figure(search, pathname):
    
    fig = {}
    if not df.empty:
        fig = px.bar(df, x="nation", y="count", title="graph")
    return fig



# app = DispatcherMiddleware(server, {
#     '/dash': dash_app1.server
# })

# run_simple('0.0.0.0', 8080, app, use_reloader=True, use_debugger=True)
