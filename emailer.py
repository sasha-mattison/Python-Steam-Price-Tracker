import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

app_password = os.getenv("APP_PASSWORD")

def send_email(subject, content):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "Steam Tracker <sashamattison2010@gmail.com>"
    msg["To"] = "sashamattison2010@gmail.com"

    msg.set_content(content)

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login("sashamattison2010@gmail.com", app_password)
        smtp.send_message(msg)
