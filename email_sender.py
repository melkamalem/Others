from email.message import EmailMessage
from app2 import email_password 
import ssl
import smtplib


email_sender = 'malemay20@gmail.com'
email_password = email_password

email_receiver = 'miboto1498@dogemn.com'

subject = 'this is the email sender'
body = """and this is the main message"""

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

