
#!/usr/bin/env python
"""A noddy fake smtp server."""
#sudo python -m smtpd -n -c DebuggingServer localhost:25

import smtpd
import asyncore
import sys

class FakeSMTPServer(smtpd.SMTPServer):
    """A Fake smtp server"""

    def __init__(*args, **kwargs):
        print("Running fake smtp server on port 25")
        try:
            smtpd.SMTPServer.__init__(*args, **kwargs)

        except(PermissionError):


    def process_message(*args, **kwargs):
        pass

if __name__ == "__main__":
    smtp_server = FakeSMTPServer(('localhost', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        smtp_server.close()
