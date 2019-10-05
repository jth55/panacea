import logging, datetime, random, copy, json, ast, subprocess
import collections, sys, json
from threading import Thread, Timer
from hashlib import sha256
from enum import IntEnum
from time import sleep


def get_json(json_file):
    """Returns json data for specified patient UUID, demo uses test json data """
    with open("data/patientData0.json", "r") as json_file:
        return json.load(json_file)


class MetaModel(object):
    """
    Data for all components of this project.
    """

    def __init__(self):

        print("Loading config...")
        self.patient = Patient("Debra")

class Patient(object):
    def __init__(self, name):# pass in later

        entered_patient_json = "data/patientData0.json"

        pj = get_json(entered_patient_json)

        #self.name = pj
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
