# import pandas as pd
# import dash_html_components as html
# import plotly.express as px
# import dash_core_components as dcc
# from dash.dependencies import Input, Output, State
# import dash
# import flask

# app_flask = flask.Flask(__name__)

# app_dash = dash.Dash(__name__, server=app_flask, url_base_pathname='/pathname')

# class sampleDashboard:
#     dashData = {}

#     def load_data_frame(self):
#         data = [{'nation':'South Korea', 'medal': 'gold', 'count': 24}]
#         return pd.DataFrame(data)


# sample_dashboard = sampleDashboard()


# def getLayout():
#     # df = sample_dashboard.load_data_frame()

#     return [
#                     html.Div(children=[
#                             dcc.Graph(id='graph')
#                     ])
#     ]

# @app_flask.callback(Output('graph', 'figure'),
#               Input('url', 'search'),
#               State('url', 'pathname'))
# def update_figure(search, pathname):
#     df = sample_dashboard.load_data_frame()
#     fig = {}
#     if not df.empty:
#         fig = px.bar(df, x="nation", y="count", title="graph")
#     return fig


from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import flask
from werkzeug.serving import run_simple
import dash_html_components as html

server = flask.Flask(__name__)
dash_app1 = Dash(__name__, server = server, url_base_pathname='/dashboard/' )
dash_app2 = Dash(__name__, server = server, url_base_pathname='/reports/')
dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])
dash_app2.layout = html.Div([html.H1('Hi there, I am app2 for reports')])
@server.route('/')
@server.route('/hello')
def hello():
    return 'hello world!'

@server.route('/dashboard/')
def render_dashboard():
    return flask.redirect('/dash1')


@server.route('/reports/')
def render_reports():
    return flask.redirect('/dash2')

app = DispatcherMiddleware(server, {
    '/dash1': dash_app1.server,
    '/dash2': dash_app2.server
})

run_simple('0.0.0.0', 8080, app, use_reloader=True, use_debugger=True)
