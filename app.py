from flask import Flask, jsonify
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

# Hardcoded start date (UTC)
START_DATE = datetime(2023, 1, 1, 0, 0, 0)
INTERVAL_MINUTES = 5
MAX_MONTHS = 1200  # Cap at 100 years

@app.route('/currdate', methods=['GET'])
def get_currdate():
    now = datetime.utcnow()
    elapsed_minutes = (now - START_DATE).total_seconds() // 60
    intervals_passed = int(elapsed_minutes // INTERVAL_MINUTES)

    # Cap the month increment
    if intervals_passed > MAX_MONTHS:
        intervals_passed = MAX_MONTHS

    current_date = START_DATE + relativedelta(months=intervals_passed)
    return jsonify({'currentDate': current_date.strftime('%Y-%m-%d')})
