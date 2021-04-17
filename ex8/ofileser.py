import socket
import os
import tqdm
sock = socket.socket()
sock.bind(('',1234))
sock.listen(10)
r,addr = sock.accept()
filename = r.recv(1024).decode()
print(filename)
#filename = "client.py"
filesize = os.path.getsize(filename)
#r.send(filename.encode())
r.send(str(filesize).encode())
progress = tqdm.tqdm(range(filesize),f"Sending {filename}",unit ="B",unit_scale = True, unit_divisor = 102)
with open(filename ,"rb") as f:
    for _ in progress:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        r.sendall(bytes_read)
        #print(bytes_read.decode())
        print("###########")
        progress.update(len(bytes_read))
r.close()






