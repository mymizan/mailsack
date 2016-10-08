import socketserver

'''
Request Handler class for the TCP Server
'''
class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

'''
TCP Server class
'''
class sockserver:

  def __init__(self, host, port):
    self.host = host
    self.port = port

  def listen(self):
    server = socketserver.TCPServer((self.host, int(self.port)), RequestHandler)
    server.serve_forever()

if __name__ == '__main__':
  # for tests. should not be invoked directly
  s = sockserver('localhost', 9999)
  s.listen()
