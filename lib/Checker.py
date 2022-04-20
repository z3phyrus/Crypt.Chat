import requests
import sys
from lib.Colors import *

class Checker:
    def __init__(self):
        sys.dont_write_bytecode = True

    def internet_connection(self):
        print(Colors.blue+"[+] Checking internet connection ....")
        try:
            request = requests.get('https://google.com', timeout=3)
            print(Colors.blue + "[" + Colors.green + '\u2713' + Colors.blue + "]""Connection established\n")
        except (requests.ConnectionError, requests.Timeout) as exception:
            exit(Colors.red+"[!] No internet connection.")