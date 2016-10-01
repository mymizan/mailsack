#!/usr/bin/env python
"""Dummy SMTP Server"""

import asyncore
import smtpd
import sys

class Mailsack_Server(smtpd.SMTPServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save_message(*args, **kwargs):
        pass

    def print_message(*args, **kwargs):
        print("From: ", args[2], "\n"
               "To: ", args[3], "\n"
               "Body: ", args[4], "\n"
            )
        print("----------END--------------\n")

    def process_message(self, *args, **kwargs):
        self.print_message(*args, **kwargs)

    def notify_client():
        pass


if __name__ == '__main__':
    try:
        mailsack = Mailsack_Server(('localhost', 25), None)
        print("Server listening on port 25")
    except(PermissionError):
        print("Can not bind to port 25. Please, run as root")
        sys.exit()

    try:
        asyncore.loop()
    except KeyboardInterrupt:
        mailsack.close()

