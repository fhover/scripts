
#!/usr/bin/python
import smtplib, string
import os, time

os.system("/etc/init.d/sendmail start")
time.sleep(4)

HOST = "localhost"
SUBJECT = "Email from spoofed sender"
TO = "frederik@hover.dk"
FROM = "titttts@asssss.com"
TEXT = "Message Bodyyyyyyyyyyyyy masses"
BODY = string.join((
	"From: %s" % FROM,
	"To: %s" % TO,
	"Subject: %s" % SUBJECT ,
	"",
	TEXT
	), "\r\n")
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()

time.sleep(4)
os.system("/etc/init.d/sendmail stop")
