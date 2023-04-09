import altair as alt
import datapane as dp
from flask import Flask, render_template
from vega_datasets import data

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("homepage.html")

@app.route("/iris")
def loadIris():
    return "<p>data.iris<p>"

if __name__ == "__main__":
    app.run(debug=True)
    