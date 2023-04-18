from flask import Flask, render_template
import sampleDashboard
import pandas as pd
import dash_html_components as html
import plotly.express as px
import flask
app_flask = flask.Flask(__name__)

@app_flask.route('/abc') 
def hello_world():
    return flask.redirect('/pathname')
    # return render_template("index.html", title="Hello")
    # return sampleDashboard.getLayout()
    # return 'Hello'
    
