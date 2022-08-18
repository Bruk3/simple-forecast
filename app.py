import os

from flask import jsonify

from flask import Flask, render_template

app = Flask(__name__)


WEATHER = [
    {
        "Temperature": "40",
        "Precipitation": "20%",
        "Wind": "18 mph",
        "Comment": "Layer Up!",
    },
    {
        "Temperature": "108",
        "Precipitation": "2%",
        "Wind": "8 mph",
        "Comment": "Sunny day, Beach day!",
    },
]


@app.route("/api/today")
def get_today_forecast():
    return jsonify(WEATHER[0])


@app.route("/api/tomorrow")
def get_tmw_forecast():
    return jsonify(WEATHER[1])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)
