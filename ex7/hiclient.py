import socket
import threading 
import termcolor 
from termcolor import colored
def sendomsg(r):
    true=True
    while true:

        t = input()
        rr = "CLIENT: "+str(t)

        r.send(rr.encode())
def recvv(r):
   true = True
   while true:
         tt= str(r.recv(1024).decode())
         print(colored(tt,'green'))
socek = socket.socket()
socek.connect(("127.0.0.1",1234))
ts = threading.Thread(target = sendomsg, args=(socek,))
tr = threading.Thread(target=recvv, args=(socek,))
ts.start()
tr.start()
