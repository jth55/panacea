from flask import Flask, render_template, request, redirect, url_for
from functools import wraps
from engine import model
from threading import Thread
from hashlib import sha256
import logging, os, subprocess, sys, random
import json

# Flask information
app = Flask(__name__)
app.secret_key = 'this is a secret :-)wrjiafih'

# Logging config
logging.basicConfig(filename='app.log', format='%(asctime)s - %(levelname)s - %(threadName)s - %(message)s', \
    datefmt='%I:%M:%S %p', level=logging.INFO)

# Logging pretty colors
logging.addLevelName(
    logging.INFO, "\033[1;32m%s\033[1;0m" % logging.getLevelName(logging.INFO))
logging.addLevelName(
    logging.WARNING,
    "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))

# "Parse" command line arguments

# Load data model
mm = model.MetaModel()
mm.login = False

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if mm.login:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

@app.route('/login', methods=['GET', 'POST'])
def login():
    # login function here
    if request.method == 'POST':
        mm.login = True
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html', patient=mm.patient)

@app.route('/scheduling', methods=['GET', 'POST'])
@login_required
def scheduling():
    return render_template('scheduling.html', patient=mm.patient)

@app.route('/pricing', methods=['GET', 'POST'])
@login_required
def pricing():
    return render_template('pricing.html', patient=mm.patient)

@app.route('/analytics', methods=['GET', 'POST'])
@login_required
def analytics():
    return render_template('analytics.html', patient=mm.patient)

@app.route('/options', methods=['GET', 'POST'])
@login_required
def options():
    return render_template('options.html')

@app.route('/estimate_price', methods=['GET', 'POST'])
@login_required
def estimate_price():
    return render_template('estimate_price.html')

@app.route('/static_estimate_price', methods=['GET', 'POST'])
@login_required
def static_estimate_price():
    return render_template('static_price_estimate.html')

@app.route('/pubkey_repo', methods=['GET', 'POST'])
@login_required
def pkrepo():
    return render_template('pubkey_repo.html')

def get_json():
    """Returns json data for specified patient UUID, demo uses test json data """
    with open("data/patientData0.json", "r") as json_file:
        return json.load(json_file)


@app.route('/api', methods=['POST'])
def get_api_data():
    """Read only load view for a patient UUID and a specified key"""
    # We only have one patient for now, so uuid field is ignored
    patient_uuid = request.form.get('UUID')
    key = request.form.get('key')

    json_data = get_json()

    # Auth and scoping are not implemented in the sample
    # Could restrict with auth and key scope to only certain keys

    response = app.response_class(
        response=json.dumps(json_data['patient'][key]),
        status=200,
        mimetype='application/json'
    )
    return response


# Launch web server
logging.info("Running web server.")
app.run(debug=True, use_reloader=False, host= '0.0.0.0', port=5682)
