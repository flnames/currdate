from flask import Flask, jsonify
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

# Hardcoded reference date
BASE_DATE = datetime(2023, 1, 1)

# Track when the service was started
SERVICE_START_TIME = datetime.utcnow()

INTERVAL = timedelta(minutes=5)

@app.route('/currdate', methods=['GET'])
def currdate():
    now = datetime.utcnow()
    elapsed_time = now - SERVICE_START_TIME

    # Number of 5-minute intervals since service started
    intervals_passed = int(elapsed_time.total_seconds() // INTERVAL.total_seconds())

    # Add one month per interval to the BASE_DATE
    current_date = BASE_DATE + relativedelta(months=intervals_passed)

    return jsonify({'currentDate': current_date.strftime('%Y-%m-%d'),'time':elapsed_time % INTERVAL})

