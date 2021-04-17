import socket
import threading
from termcolor import colored 
def send_msg(r):

    while True:
        t=input()
        #print("enter")
        t = "SERVER: "+str(t) 
        r.send(t.encode())
def recvv(r):
    while True:
        tt = (r.recv(1024).decode())
        tt = str(tt)
        print((colored(tt,'green')))


sock = socket.socket()
sock.bind(('',1234))
sock.listen(10)
r,addr=sock.accept()
ts = threading.Thread(target=send_msg, args=(r,))
tr = threading.Thread(target=recvv,args=(r,))
ts.start()
tr.start()

