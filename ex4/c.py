import socket
sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
print("Connection done")
tt= input("Enter message to be sent ")
sock.sendto(tt.encode(), ("127.0.0.1",1234))

t=sock.recvfrom(1024)

print("message received from server is")
print(t[0].decode())

#print("doone")doone
