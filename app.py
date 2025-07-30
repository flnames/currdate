from flask import Flask, jsonify
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

BASE_DATE = datetime(2020, 5, 1)
SERVICE_START_TIME = datetime.utcnow()
INTERVAL = timedelta(minutes=5)

@app.route('/currdate', methods=['GET'])
def currdate():
    now = datetime.utcnow()
    elapsed_time = now - SERVICE_START_TIME

    intervals_passed = int(elapsed_time.total_seconds() // INTERVAL.total_seconds())
    current_date = BASE_DATE + relativedelta(months=intervals_passed)

    # Calculate time left for next interval
    remaining = INTERVAL - (elapsed_time % INTERVAL)
    remaining_seconds = int(remaining.total_seconds())

    return jsonify({
        'currentDate': current_date.strftime('%Y-%m-%d'),
        'time_until_next_update_seconds': remaining_seconds
    })


