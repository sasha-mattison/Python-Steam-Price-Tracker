import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

app_password = os.getenv("APP_PASSWORD")
email = os.getenv("EMAIL")

def send_email(subject, content):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "Steam Tracker <" + email +">"
    msg["To"] = email

    msg.set_content(content)

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, app_password)
        smtp.send_message(msg)
