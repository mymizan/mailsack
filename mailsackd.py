#!/usr/bin/env python
"""Dummy SMTP Server"""

import asyncore
import sockserver
import threading
import argparse
import smtpd
import sys

class Mailsack_Server(smtpd.SMTPServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mail_list = []

    def save_message(self, mail):
        self.mail_list.append(mail)

    def print_message(self, mail):
        print(mail)
        print("----------END--------------\n")

    def process_message(self, *args, **kwargs):
        mail = "From: " + args[1] + "\n" + "To: " + str(args[2]) + "\n" "Body: " + args[3] + "\n"
        self.save_message(mail)
        self.print_message(mail)

if __name__ == '__main__':
    #get default arguments
    try:
        parser = argparse.ArgumentParser(description='')
        parser.add_argument('--host', default='localhost', help='local IP address to listen to')
        parser.add_argument('--port', default='25', help='port to listen')
        parser.add_argument('--listen', default='None', help='listen for client connections')

        args = parser.parse_args()
        args = vars(args)
    except:
        print("Invalid arguments")
        sys.exit()
    try:
        mailsack = Mailsack_Server((args['host'], int(args['port'])), None)
        print("Server listening on port ", args['port'])
    except(PermissionError):
        print("Can not bind to port " + args['port'] + ". Please, run as root")
        sys.exit()

    # listen for incoming connection from GUI
    if args['listen'] != 'None':
        try:
            sockserver = SockServer(args['host'], int(args['listen']))
            sockserver.listen()
        except:
            print("Can not start socket server. Incoming connections from the UI will be denied.")

    try:
        asyncore.loop()
    except KeyboardInterrupt:
        mailsack.close()

