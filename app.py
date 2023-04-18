from flask import Flask, render_template
import pandas as pd
import dash_html_components as html
import plotly.express as px
import flask
import dash
server = Flask('budashboard')

app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True, url_base_pathname='/bu/',
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
    
