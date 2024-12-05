# Import socket module
import socket
import importlib
Elliptic=importlib.import_module("1905117_Ecc")
aes=importlib.import_module("1905117_aes")
import pickle
# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

while(True):
    print(s.recv(1024).decode())
    recVars = s.recv(1024)
    list=pickle.loads(recVars)


    print("a")
    kb=Elliptic.generateKb(list['e'])
    print("b")
    keyserver=Elliptic.double_and_add((list['x'], list['y']), kb, list['a'], list['b'], list['p'])
    print(keyserver)
    objectkey = {'x': keyserver[0], 'y': keyserver[1]}
    keysend = pickle.dumps(objectkey)
    s.sendall(keysend)


    # keyrcv = s.recv(1024)
    # rcvkey = pickle.loads(keyrcv)

    # inp = input("Input")
s.close()