
# Client for Crypt.Chat 
from checks import *
import socket 
import threading 
import requests

internet_connection()

nickname = input(Colors.cyan+"[+] Enter a nickname > ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 55555))


def receive_data():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
        
            if message == "NICK": 
                client.send(nickname.encode("utf-8"))
            else:
                print(f'[!] {Colors.green}> {Colors.green}{message}')
        except:
            print(Colors.red+"[+] Error in connection ...")
            client.close()
            break

def writing():
    while True:
        message = f'{nickname}: {input("")}'
        # Always waiting for new messages
        client.send(message.encode('ascii'))


# threads for each function 

receive_thread = threading.Thread(target=receive_data)
receive_thread.start()

writing_thread = threading.Thread(target=writing)
writing_thread.start()
