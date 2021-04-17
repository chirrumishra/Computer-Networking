import uuid 
import os
# printing the value of unique MAC 
# address using uuid and getnode() function  
print("Printing the ARP table")
print(" ")
os.system('arp -a')
print(" ")
print("Enter ip address ")
getnodee = input()
print(" ")
print("The mac address is:")
print (hex(uuid.getnode())) 


