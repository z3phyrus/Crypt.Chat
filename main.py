# Main

from lib.ClientHandler import *
from lib.Checker import *
import threading

if __name__ == '__main__':
    checker = Checker()
    checker.internet_connection()
    client_handler = ClientHandler('127.0.0.1', 1234)
    client_handler.connect()
    receive_thread = threading.Thread(target=client_handler.get_response)
    receive_thread.start()

    send_thread = threading.Thread(target=client_handler.send_response)
    send_thread.start()
