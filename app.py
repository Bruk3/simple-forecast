import os
from flask import jsonify

from flask import Flask

app = Flask(__name__, template_folder='templates')

QUOTE_SERVICE_URL = os.environ.get("QUOTE_SERVICE_URL")


WEATHER = [
    {"Temperature": "40", "Precipitation": "20%", "Wind": "18 mph", "Comment": "Layer Up!"}, 
    {"Temperature": "108", "Precipitation": "2%", "Wind": "8 mph", "Comment": "Sunny day, Beach day!" }
]

def fetch_quote():
    contents = urllib.request.urlopen(
            "http://{QUOTE_SERVICE_URL}/api/quote".format(
                QUOTE_SERVICE_URL=QUOTE_SERVICE_URL
            )
        ).read()
    return json.loads(contents)


@app.route('/api/today')
def get_today_forecast():
    return jsonify(WEATHER[0])

@app.route('/api/tomorrow')
def get_tmw_forecast():
    return jsonify(WEATHER[1])



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
