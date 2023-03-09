import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 465)

server.ehlo()

with open ("password.txt", "r") as f:
    password = f.read()

sender = "Testeduserdomain"
receiver = "sag82852@omeie.com"

server.login(sender, password)

msg = MIMEMultipart()
msg["from"] = "CodeRad"
msg["to"] =  "sag82852@omeie.com"
msg["object"] = "Just a text"

with open("message.txt", "r") as f:
    message = f.read()

# add an attachment
filename = "picture.jpeg"
attachment = open(filename, "rb")

# set the payload
p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename={filename}")

# send email message
msg.attach(MIMEText(message, "plain"))

text = msg.as_string()
server.sendmail(sender, receiver, message)