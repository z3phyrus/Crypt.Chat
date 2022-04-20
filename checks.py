import requests


class Colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'


def internet_connection():
    print(Colors.blue+"[+] Checking internet connection ....")
    try:
        request = requests.get('https://google.com', timeout=3)
        print(Colors.blue + "[" + Colors.green + '\u2713' + Colors.blue + "]""Connection established\n")
    except (requests.ConnectionError, requests.Timeout) as exception:
        exit(Colors.red+"[!] No internet connection.")

