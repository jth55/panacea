import logging, datetime, random, copy, json, ast, subprocess
import collections, sys, json
from threading import Thread, Timer
from hashlib import sha256
from enum import IntEnum
from time import sleep


def get_json(json_file):
    """Returns json data for specified patient UUID, demo uses test json data on disk"""
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

        self.name = pj["patient"][0]["name"]

        self.visits = []
        for appointment in pj["patient"][0]["appointment"]:
            apt_tuple = (appointment["location"], appointment["scheduled_time"], "ical",  "maps")
            self.visits.append( apt_tuple )

        #self.visits = [("Appointment at Sanford Health Center", "3PM Sunday", "ical", "maps"), ("Chemotherapy at the Sanford Cancer Center", "1PM Monday", "ical", "maps")]

        self.prescriptions = []
        for prescription in pj["patient"][0]["medication"]:
            per_tuple = ( prescription["brand"], prescription["dosage_mg"] )
            self.prescriptions.append( per_tuple )
        # self.prescriptions = [("Zofran", "Take 8:00 AM Daily"), ("Promethegan", "Take Tuesday, Saturday")]

        self.bills = []
        for bill in pj["patient"][0]["appointment"]:
            if bill["bill"][0]["payment_date"] == "null":
                bill_tuple = ( bill["location"], bill["bill"][0]["date_posted"] , bill["bill"][0]["co-pay"],  "Unpaid" )
                self.bills.append( bill_tuple )


        # self.bills = [("Radiology visit at Sanford Health", "October 21", "12,798", "unpaid")]


        self.paid = []
        for bill in pj["patient"][0]["appointment"]:
            if bill["bill"][0]["payment_date"] != "null":
                paid_tuple = ( bill["location"], bill["bill"][0]["date_posted"] , bill["bill"][0]["co-pay"],  "Paid" )
                self.paid.append( paid_tuple )



        #self.paid = [("Radiology visit at Sanford Health", "October 12", "300", "paid")]


    def __str__(self):
        return ("Patient %s", self.name)

    def save(self):
        # save in db
        pass
