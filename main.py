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
     url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/?key={API}"
     content = requests.get(url)
     response = content.json()
     if "error" in response:
        return redirect(url_for("mainPage"))
     return render_template("weather_result.html", weatherUpdate = response)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )





