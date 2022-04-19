from lib.SocketHandler import *

if __name__ == '__main__':
    socket_handler = SocketHandler('127.0.0.1', 1234)
    socket_handler.start_server()
    socket_handler.accept_connection()