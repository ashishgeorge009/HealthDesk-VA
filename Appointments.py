import pandas as pd
from utils import DETAILS
from display_data import get_date

## Create a custom function to create appointments
def create_appointment():
    doc_info = pd.read_excel('Doctor_database.xlsx')
    # Getting the Branch information
    branch = doc_info[(doc_info['Name'] == DETAILS['doctor']) & (doc_info['Specialization']==DETAILS['appointment'])]['Branch'].item() 
    appointment = pd.read_excel('Appointment_database.xlsx')
    app = {'Patient Name': DETAILS['name'],
        'Doctor Name': DETAILS['doctor'],
        'Specialist Type': DETAILS['appointment'],
        'Branch': branch,
        'Date':get_date(DETAILS['date']),
        'Time':DETAILS['time']}
    appointment = appointment.append(app,ignore_index=True)   
    appointment.to_excel('Appointment_database.xlsx',index=False)

## Create a custom function to show appointment
def show_appointments():
    appointment = pd.read_excel('Appointment_database.xlsx')
    print("\n")
    print(appointment.head())
    print("\n")

## A custom function to count the number of appointments
def no_of_appointments():
    appointment = pd.read_excel('Appointment_database.xlsx')
    return len(appointment)

## A custom function to cancel the appointments
def cancel_appointment(id):
    appointment = pd.read_excel('Appointment_database.xlsx')
    appointment.drop(index=id,inplace=True)
    appointment.to_excel('Appointment_database.xlsx',index=False)
