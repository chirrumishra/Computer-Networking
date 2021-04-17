import socket
sock = socket.socket()
sock.bind(('',1234))
sock.listen(10)
r,addr = sock.accept()
print("connection done")
t="menu: +,-,*,/"
r.send(t.encode())
tt=r.recv(1024).decode()
r.send("send first number".encode())
t1=r.recv(1024).decode()
r.send("send second number".encode())
t2 = r.recv(1024).decode()
t1 = int(t1)
t2 = int(t2)
if(tt=="+"):
    r1=t1+t2
if(tt=="-"):
    r1=t1-t2
if(tt=="*"):
    r1=t1*t2
if(tt=="/"):
    r1=t1/t2
res = "The result is "+ (str(r1))
r.send(res.encode())
