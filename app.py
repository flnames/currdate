from flask import Flask, jsonify, request
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

# Starting values
BASE_DATE = datetime(2020, 5, 1)
current_fake_date = BASE_DATE

@app.route('/currdate', methods=['GET'])
def currdate():
    return jsonify({
        'currentDate': current_fake_date.strftime('%Y-%m-%d')
    })

@app.route('/next', methods=['POST'])
def next_date():
    global current_fake_date
    current_fake_date += relativedelta(months=1)
    return jsonify({
        'message': 'Date advanced by 1 month',
        'newDate': current_fake_date.strftime('%Y-%m-%d')
    })

@app.route('/prev', methods=['POST'])
def prev_date():
    global current_fake_date
    current_fake_date -= relativedelta(months=1)
    return jsonify({
        'message': 'Date moved back by 1 month',
        'newDate': current_fake_date.strftime('%Y-%m-%d')
    })

@app.route('/date', methods=['POST'])
def set_date():
    global current_fake_date
    date_str = request.args.get('date')
    if not date_str:
        return jsonify({'error': 'Missing "date" query parameter'}), 400
    try:
        current_fake_date = datetime.strptime(date_str, '%Y-%m-%d')
        return jsonify({
            'message': f'Date set to {date_str}',
            'newDate': current_fake_date.strftime('%Y-%m-%d')
        })
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

@app.route('/')
def health():
    return "Fake Date Service Running"
