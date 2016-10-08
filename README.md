# mailsack
Dummy SMTP Server Written in Python With A Simple UI

Mailsack contains a dummy smtp server (mailsackd.py) to intercept mails from localhost and an UI written in tk to view the mails. I personally use the daemon on the dev server. The simple UI is for my development machine. The UI can connect to remote host or local host to show intercepted mails by the server.

---
mailsackd.py (server)
---
The dummy smtp server takes three parameters - host, port and listen. If you leave them empty, the defaults are localhost and port 25. You can run it on a different port by the passing the parameters on the command line. Passing the --listen parameter with a port number makes the server listen for incoming connection from the UI, otherwise, it just prints the incoming mails to the standard output. 

The UI is handy, not necessary. 

    $./mailsackd.py --host=localhost --port=9090 --listen=9999
    
--
mailsack.py (Client)
---

    $./mailsack.py --host=localhost --port=9999

In the example, host is where the remote server is running and port is as the "listen" port of the server. You can leave the client running in the background, it will poll the server periodically for updated emails. 



Feel free to use and fork! Any suggestions or contributions are welcome.
