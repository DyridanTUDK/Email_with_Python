import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from' ] = 'Sender Name'
email['to'] = 'Reciever Email'
email['subject'] = 'Subject Here'


email.set_content(html.substitute({'name' : ' homie'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender email here', 'sender password here')
    smtp.send_message(email)
    print('all good homie')


