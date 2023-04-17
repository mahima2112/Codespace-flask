from flask import Flask, render_template
import sampleDashboard
import pandas as pd
import dash_html_components as html
import plotly.express as px
app = Flask(__name__)

@app.route("/")
def hello_world():
    # return render_template("index.html", title="Hello")
    # return sampleDashboard.getLayout()
    import plotly.graph_objects as go
    fig = go.Figure(
        data=[go.Bar(y=[2, 1, 3])],
        layout_title_text="A Figure Displayed with the bar chart"
    )
    fig.show()
    
