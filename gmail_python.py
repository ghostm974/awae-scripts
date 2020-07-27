#!/usr/bin/python3

import smtplib
import getpass
import email.utils
import ssl

print("Enter Login Details\n")
gmail_user = str(input('Enter your Gmail Email: '))
gmail_password = getpass.getpass()

to_gmail = str(input("Enter Receipients Email: "))

sent_from = gmail_user
to = [to_gmail]
subject = "Test Email"
body = 'hey, What\'s up.?'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail('ghostm974@gmail.com', to, email_text)
    server.close()
    
    print ("Email Sent")
