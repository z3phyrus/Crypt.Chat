import socket
import threading

class SocketHandler:
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.clients = []
        self.nicks = []

    def start_server(self):
        try:
            self.server.bind((self.host, self.port))
            self.server.listen()
        except socket.error as error:
            print(error)

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle_connection(self, connection):
        while True:
            try:
                data = connection.recv(1024)
                self.broadcast(data)
            except:
                index = self.clients.index(connection)
                self.clients.remove(connection)
                connection.close()
                nick = self.nicks[index]
                self.broadcast(nick + " has left the chat.".encode('utf-8'))
                self.nicks.remove(nick)
                break

    def accept_connection(self):
        while True:
            client, address = self.server.accept()
            client.send('nick?'.encode('utf-8'))
            nick = client.recv(1024)
            self.nicks.append(nick)
            self.clients.append(client)
            self.broadcast(nick + " has connected to the chat.".encode('utf-8'))
            thread = threading.Thread(target=self.handle_connection, args=(client,))
            thread.start()



