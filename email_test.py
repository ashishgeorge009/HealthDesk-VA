import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from permissions import set_api_key
from utils import DETAILS
from display_data import get_date

def send_email():
    set_api_key() # This line just adds the SENDGRID_API_KEY environment variable
    target = DETAILS['email']
    message = Mail(
        from_email='myemailid109@gmail.com',
        to_emails=target,
        subject='Appointment Booked',
        html_content="""\
        <html>
        <head></head>
        <body>
            <h2>Your Appointment has been booked successfully!</h2>
            <p><h4>Hi, {name} your appointment with Dr {doctor} has been booked.</h4>
            <h4>Here are all your appointment details:</h4>
            <b>Specialist Type: </b>{type}<br>
            <b>Doctor: </b>{doctor}<br>
            <b>Patient Name: </b>{name}<br>
            <b>Date :</b>{date}<br>
            <b>Time :</b>{time}<br>
            </p><br>
        </body>
        </html>
        """.format(name=DETAILS['name'],doctor=DETAILS['doctor'],
        type=DETAILS['appointment'],date=get_date(DETAILS['date']),time=DETAILS['time']))

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        # print(e.message)
        pass