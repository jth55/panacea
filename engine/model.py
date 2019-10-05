import logging, datetime, random, copy, json, ast, subprocess, yaml
import collections, sys, json
from threading import Thread, Timer
from hashlib import sha256
from enum import IntEnum
from time import sleep
#from engine import db

class MetaModel(object):
    """
    Data for all components of this project.

    """

    def __init__(self):

        print("Loading config...")
        self.patient = Patient("Debra")

        # DEMO VERSION -- NO DATABASE
        """
        with open('config.yaml', 'r') as f:
            config = yaml.load(f, Loader=yaml.SafeLoader)

        self.settings = config['settings']
        print("Hashing password...")
        self.settings['password'] = sha256(
            self.settings['password'].encode('utf-8')).hexdigest()

        self.config_teams = config['teams']
        self.config_systems = config['systems']

        print("Emptying existing database...")
        db.reset_all_tables()

        logging.info(
            "------------------------ APP LAUNCHED ------------------------")
        logging.info("Loading data into the in-memory model.")

        # Initialize modules into the database
        for module in modules.module_info.list_modules():
            getattr(modules, module).create()

        # Set MSFRPC current setting to off
        self.msfrpc_loaded = 0
        self.autostart = 0

        # todo run through jobs
        self.jobs = []

        # Load global settings
        self.run = 0
        self.dest = 0
        self.thread_lock = 0
        self.msf_pw = "9wFZ8T7KWyydh2z4"

        # Load teams and systems
        self.teams = []
        sorted_teams = sorted(self.config_teams.items(), key=lambda kv: kv[0])
        for team in sorted_teams:
            team_info = (team[1]['team_name'], team[1]['prefix'],
                         team[1]['difficulty'])
            self.write_team(team_info)
        """


class Patient(object):
    def __init__(self, name):
        self.name = name
        self.visits = [("Appointment at Sanford Health Center", "3PM Sunday", "ical", "maps"), \
        ("Chemotherapy at the Sanford Cancer Center", "1PM Monday", "ical", "maps")]
        self.prescriptions = [("Zofran", "Take 8:00 AM Daily"), ("Promethegan", "Take Tuesday, Saturday")]
        self.bills = [("Radiology visit at Sanford Health", "October 21", "12,798", "Unpaid")]
        self.paid = [("Radiology visit at Sanford Health", "October 12", "300", "paid")]


    def __str__(self):
        return ("Patient %s", self.name)

    def save(self):
        # save in db
        pass
