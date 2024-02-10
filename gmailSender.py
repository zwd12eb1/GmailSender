# https://www.youtube.com/watch?v=g_j6ILT-X0k
import os
from email.message inport EmailMessage
import ssl
import smtplib

email_sender = '@gmail.com'
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = 'abc@rece.com'

subject = 'Check out my new video'
body = """
I've just published a new video on YouTube: https://youtu.be/2cZzP9DL1kg
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Attach the image file
with open('Image.png', 'rb') as attachment_file:
    file_data = attachment_file.read()
    file_name = attlachment_file.name.split("/")[-1]

attachment = MINEBase('application', 'octet-strean')
attachment.set_payload(file_data)
encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', f'attachment; filename="{File_name}"')
em.attach(attachment)

# ADD SSL security
context = ssl.create_default_context()    

with smtplib.SMTP_SSL('smtp.gmail.com', 465, cantextscontext) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
