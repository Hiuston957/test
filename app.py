from flask import Flask, render_template
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Pobranie stref czasowych
    timezones = pytz.all_timezones
    current_times = []

    for tz in timezones:
        now = datetime.now(pytz.timezone(tz))
        current_times.append((tz, now.strftime("%Y-%m-%d %H:%M:%S")))

    return render_template("index.html", current_times=current_times)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
