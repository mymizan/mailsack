#!/usr/bin/python

import smtplib

sender = 'test1@example.com'
receivers = ['test2@example.com']

message = """From: Jon Doe <test1@example.com>
To: Jane Doe <test2@example.com>
Subject: SMTP TEST

Test message
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print("Sent")
except SMTPException:
   print("SMTP Exception")
