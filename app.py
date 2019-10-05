from flask import Flask, render_template, request, redirect, url_for
from functools import wraps
from engine import model
from threading import Thread
from hashlib import sha256
import logging, os, subprocess, sys, random

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
    success = error = team = 0  # Set false/none
    if 'view' in request.args:
        try:
            team_id = int(request.args['view'])
        except:
            error = "Invalid team ID."
        try:
            team = mm.teams[int(team_id) - 1]
        except:
            error = "Team ID doesn't exist."
        if error:
            return render_template('teams.html',r=mm.run,
                           d=mm.dest, teams=mm.teams, error=error)
        if request.method == 'GET':
            return render_template('team_details.html', r=mm.run, d=mm.dest, team=team)

    if request.method == 'POST':

        if 'action' in request.form:
            if request.form['action'] == 'edit' or request.form['action'] == 'add':
                return render_template('team_edit.html', r=mm.run, d=mm.dest, team=team)

            if request.form['action'] == 'cancel':
                if team:
                    return render_template('team_details.html', r=mm.run, d=mm.dest, team=team)
                else:
                    return render_template('teams.html', r=mm.run, d=mm.dest)


            if request.form['action'] == 'save':
                    try:
                        if request.form['name'] != "":
                            name = request.form['name']
                        # character whitelist here
                    except:
                        error = "Invalid characters in team name."
                    try:
                        if request.form['ip'] != "":
                            ip = request.form['ip']
                        # regex matching here
                    except:
                        error = "Invalid IP address format."
                    try:
                        difficulty = request.form['difficulty']
                        # diffiulty integer within range test here
                    except:
                        error = "Invalid difficulty."
                    if not error:
                        success = 1
                        if team == 0:
                            team_info = (name, ip, difficulty)
                            mm.write_team(team_info)
                            return render_template('teams.html', r=mm.run, d=mm.dest, teams=mm.teams, success=success)
                        else:
                            team.save()
                            return render_template('team_details.html', r=mm.run, d=mm.dest, team=team, success=success)

    return render_template('teams.html', r=mm.run, d=mm.dest, teams=mm.teams, error=error)


@app.route('/pricing', methods=['GET', 'POST'])
@login_required
def pricing():
    return render_template('pricing.html', patient=mm.patient)

@app.route('/options', methods=['GET', 'POST'])
@login_required
def options():
    return render_template('options.html')

# Launch web server
logging.info("Running web server.")
app.run(debug=True, use_reloader=False, host= '0.0.0.0', port=5682)
