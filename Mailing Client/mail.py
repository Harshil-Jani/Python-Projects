import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

with open('password.txt','r') as pwd:
    password = pwd.read()

msg = MIMEMultipart()
msg['From'] = 'Mr. Harshil Jani'
msg['To'] = 'annoyingfriend@gmail.com'
msg['Subject'] = 'Learning SMTP'

with open('message.txt','r') as message:
    content = message.read()

msg.attach(MIMEText(content,'plain'))
text = msg.as_string()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login('yourmail@gmail.com', password)
server.sendmail('yourmail.com', 'annoyingfriend@gmail.com', text)
server.close()
