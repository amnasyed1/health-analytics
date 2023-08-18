import pandas as pd
import numpy as np 

#variables
patient_firstName = "Taylor"
patient_age = 22 
patient_healthconditions = ["migranes", "asthma", "allergies"]
patinet_o2sat = 98
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

# function
def measure_o2sat (asthma, health_conditions, o2sat):
    if o2sat <94 and "asthma" in health_conditions:
        return "put on oxygen respirator"
    elif o2sat == 95 and "asthma" in health_conditions:
        return "keep obeservation on o2sat"
    else:
        return "no need for oxygen respirator"

#print fucntions

print ("Patient First Name:", patient_firstName)
print ("Patient Age:", patient_age)
print ("Patient Health Conditions:", patient_healthconditions)
print ("Patient Oxygen Saturation Level:", patinet_o2sat)
print ("Patient Medical Informaiton Recorded:", patient_information)

