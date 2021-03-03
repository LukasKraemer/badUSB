import socket                   
from datetime import datetime as datestamp

port = 50000                    
s = socket.socket()             
host = ""   
s.bind((host, port))           
s.listen(100)                     

print ('Server listening....')

while True:
    conn, addr = s.accept()     
    print ('Got connection from', addr)
    data = conn.recv(1024)

    if(data.decode('utf-8') =='Linux'):
        print("linux")
        filename='sample.py' 
    if(data.decode('utf-8') =='Windows'):
        print("windows")
        filename='sample.exe' 

    #send File to Server
    
    f = open(filename,'rb')
    l = f.read(1024)

    while (l):
       conn.send(l)
       l = f.read(1024)
    f.close()

    print(f'Done sending to {addr}')
    with open("logs.txt", "a") as logs:
        logs.write(f'{addr[0]};{str(datestamp.now())}\n')
    conn.close()