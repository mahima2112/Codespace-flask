from .app import app
import dash_core_components as dcc
import dash_html_components as html
from dash import dcc, html
from dash.dependencies import Input, Output, State
from .dashboard import Dashboard
dashboard = Dashboard()
content = html.Div(id='bu-page-content', children=[])
app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        content
    ])


@app.callback(
    Output("bu-page-content", "children"),
    [Input("url", "pathname"), Input("url", "search"), Input("url", "href")],
    State("bu-page-content", "children")
)
def display_page(pathname, search, fullPath, stateContent):
    pageContent = None
    if pathname:
        
        if pathname == '/bu/dashApp':
            pageContent = dashboard.dashApp()
        return pageContent
    else:
        return stateContent