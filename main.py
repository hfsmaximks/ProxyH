import re
import socket
from colorama import init
from colorama import Fore, Back, Style

init()

logo = '''

______                    _   _ 
| ___ \                  | | | |
| |_/ / __ _____  ___   _| |_| |
|  __/ '__/ _ \ \/ / | | |  _  |
| |  | | | (_) >  <| |_| | | | |
\_|  |_|  \___/_/\_\\__,  \_| |_/
                     __/ |      
                    |___/       

                    

'''
print(Style.BRIGHT + logo)

print('\033[31m' + 'Email: hfsprobiv@gmail.com')

print(Fore.BLUE + "TG: @maximuspro999")

def validate_ip(ip):
    pattern = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    if re.search(pattern, ip):
        return True
    else:
        return False

def validate_port(port):
    pattern = "^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
    if re.search(pattern, port):
        return True
    else:
        return False

ip = input(Style.RESET_ALL + "введите ip: ")
if not validate_ip(ip):
    print("Не понимаю, что вы ввели.")
    exit()

port = input("введите порт: ")
if not validate_port(port):
    print("Не понимаю, что вы ввели.")
    exit()

def check_proxy(proxy):
    proxy_parts = proxy.split(":")
    proxy_host = proxy_parts[0]
    proxy_port = int(proxy_parts[1])

    proxy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_sock.settimeout(10)

    try:
        proxy_sock.connect((proxy_host, proxy_port))
        return True
    except:
        return False

# Test the function
proxy_to_check = (ip +":"+port)
if check_proxy(proxy_to_check):
    print(Fore.GREEN + "Этот proxy работает!")
    print(proxy_to_check)
else:
    print(Fore.RED + "Этот proxy не работает!")
    print(proxy_to_check)
