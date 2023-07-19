import smtplib , ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
#import socket
#socket.getaddrinfo('127.0.0.1',8080)
#context = ssl.create_default_context()
server = smtplib.SMTP("sandbox.smtp.mailtrap.io",465)
server.ehlo()
with open('password.txt' , 'r') as f:
    password=f.read()
server.login('ee8fac92ca90c6',password)

msg=MIMEMultipart()
msg['From'] = 'Shreyyyk'
msg['To'] = 'alsoshreyyyk@protonmail.com'
msg['Subject']= 'Testing'

with open('message.txt','r') as f:
    message=f.read()

msg.attach(MIMEText(message,'plain'))

filename='image.jpg'
attachment = open(filename , 'rb')

p = MIMEBase('application' ,'octet=-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment ; filename={filename}')

text=msg.as_string()

server.sendmail('ee8fac92ca90c6', 'alsoshreyyyk@protonmail.com' , text)