from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)
response = None

@app.route("/", methods=["GET", "POST"])
def mainPage():
    if request.method == "GET":
        return render_template("weather.html")

@app.route("/weather_result", methods=["POST"])
def results(): 
     location = request.form["city"]
     url = f"http://api.weatherapi.com/v1/current.json?key={API}&q={location}"
     content = requests.get(url)
     response = content.json()
     if "error" in response:
        return redirect(url_for("mainPage"))
     return render_template("weather_result.html", weatherUpdate = response)

app.run(debug = True)

