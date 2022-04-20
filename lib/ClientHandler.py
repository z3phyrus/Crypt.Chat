import socket
import sys

class ClientHandler:
    def __init__(self, host, port):
        sys.dont_write_bytecode = True
        self.nick = input('Choose a nickname > ')
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.client.connect((self.host, self.port))
        except socket.error as error:
            return error

    def get_response(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == "nick?":
                    self.client.send(self.nick.encode('utf-8'))
                else:
                    print(message)
            except:
                print('Error!')
                self.client.close()
                break

    def send_response(self):
        while True:
            message = self.nick + ' > ' + input("")
            self.client.send(message.encode('utf-8'))