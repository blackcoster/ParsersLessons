import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Hello')
msg['Subject'] = 'Tema'
msg['From'] = 'polina@mail.ru'
msg['To'] = 'mama@gmail.com'

s = smtplib.SMTP('localhost')
s.send_message(msg)

s.quit()
