# package for email services 
import smtplib
import string
TO = "you@your_email.com"
FROM = "webmaster@your_domain.com"
SUBJECT = "Ello from python"
text = "Hi im an email"

BODY = string.join(("From: %s" %FROM,"To: %s" %TO,"Subject: %s" %SUBJECT, "",text), "\r\n")
server = smtplib.SMTP('127.0.0.1', 1025)
server.sendmail(FROM, [TO], BODY)
server.quit()