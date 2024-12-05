import socket
import threading
import importlib
Elliptic=importlib.import_module("1905117_Ecc")
aes=importlib.import_module("1905117_aes")
import pickle

s = socket.socket()
print("Socket successfully created")


port = 12345


s.bind(('', port))
print("socket binded to %s" % (port))


s.listen(5)
print("socket is listening")

def handle_client(client_socket,addr):
    # Function to handle each client connection
    try:
       while(True):

           list=Elliptic.returningvalues(128)

           p =list[0]
           x = list[1]
           y = list[2]
           a = list[3]
           b = list[4]
           e = list[5]
           sharedVariables={'p':p,'x':x,'y':y,'a':a,'b':b,'e':e}
           sharedVars=pickle.dumps(sharedVariables)
           client_socket.sendall(sharedVars)

           ka=Elliptic.generateKa(list[5])

           keyserver=Elliptic.double_and_add((list[1], list[2]),ka,list[3],list[4],list[0])

           # objectkey={'x':keyserver[0],'y': keyserver[1]}
           # keysend=pickle.dumps(objectkey)
           # client_socket.sendall(keysend)
           keyrcv = client_socket.recv(1024)
           rcvkey = pickle.loads(keyrcv)
           print(rcvkey)
           inp = input("Input")


    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        # Close the client socket
        client_socket.close()
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())
    client_thread = threading.Thread(target=handle_client, args=(c, addr))
    client_thread.start()
    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break