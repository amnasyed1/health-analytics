import pandas as pd
import numpy as np 

#variables
patient_age = 22
patient_firstName = "Taylor"
patient_healthconditions = ["migranes", "asthma", "allergies"]
patient_information = {
    "patient_age": 22,
    "firstName": "Taylor",
    "patient_pastInformation": {
        "current health conditions": ["migranes", "asthma", "allergies"],
        "current medications": {
            "migranes": "triptan",
            "asthma": "singulair",
            "allergies": "cetirizine"
        }
    }
}

