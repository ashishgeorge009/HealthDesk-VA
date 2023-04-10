# Healthcare-Receptionist-Chatbot
A healthcare receptionist Voice Assistant using Google's Dialogflow on a Python Client

## Functionalities
1. Conversational bot that can handle non-linear conversations
2. Provide information on available Doctors based on speciality
3. Assist users book medical appointmets using voice as input
  1. Checks to ensure the doctor is available in the requested time-slot
4. List all the users appointments
5. Cancel an upcomming appointment
6. Provide information on nearby pharmacies, dentists, nursing homes etc   

## Install Requirements
```
pip install -r requirements.txt
```

To Reproduce the program, you will need to setup a Google Dialogflow Project <br>

Google Maps and Calendar API access must also be granted from your respective Google project. See instructions for how below:
1. [Google Calendar](https://developers.google.com/calendar/api/quickstart/python)
2. [Google Maps](https://developers.google.com/maps/documentation/places/web-service/get-api-key)

The DialogFlow Project is exported in a Zip file called [Receptionist.zip](Receptionist.zip)
