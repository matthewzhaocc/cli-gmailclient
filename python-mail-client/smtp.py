import smtplib
from email.message import EmailMessage
TO = input('who do u want to send it to: ')
SUBJECT = input('what is the subject of the email: ')
TEXT = input('what do u want to send: ')
rounds = input('how many times do u want to send it: ')
msg = EmailMessage()
gmailusername = input('what is ur email: ')
gmailpassword = input('what is ur password: ')
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmailusername,gmailpassword)
BODY = '\r\n'.join(['To: %s' % TO,'From: %s' % gmailusername,'Subject: %s'% SUBJECT, '', TEXT])
for i in range(int(rounds)):
    try:
        server.sendmail(gmailusername, [TO],BODY)
        print('Success')
    except:
        print('failure')
server.close()
