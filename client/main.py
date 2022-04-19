
# Client for Crypt.Chat 
# Basic / From tutorial 

import socket 
import threading 
import requests

# Checking internet connection , if active then continue 
def internet_connection():
    print("[+] Checking internet connection ....")
    try:
        request = requests.get('https://google.com', timeout=3)
        print("Connection established")
    except (requests.ConnectionError, requests.Timeout) as exception:
        exit("[!] No internet connection.")

internet_connection()

nickname = input("Enter a nickname")
# Can use config.ini files to store the nickname so the user wont have to input it all the time 
# When the user wants to chainge their nickname we can have a keywork in chat that asks for a new nickname and changes the value in config.ini


client = socket.socket(socket.AF_INET ,socket.SOCK_STREAM) 

client.connect(("127.0.0.1",55555))


def receive_data():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
        
            if message == "NICK": 
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("Error in connection")
            # Can use a function to keep the chat on till conneciton is back  and displaying an error symbol 
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

writing_thread = threading.Thread(target=writing)#
writing_thread.start()


# So far the user can only close client or write & send new messages 
