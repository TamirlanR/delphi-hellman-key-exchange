import socket, threading
import random

numbs=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
p=numbs[random.randint(1,45)]
g=numbs[random.randint(1,45)]
keys=[]
users=[]
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        
        
        while len(users)!=2:
            print(len(users))
        part_key_1 = self.csocket.recv(2048)
        if len(users)==2:
            if self.csocket ==users[0]:
                print("sending 1-2")
                users[1].send(str(part_key_1).encode())
                print("send 1-2")
            elif self.csocket==users[1]:
                print("sending 2-1")
                users[0].send(str(part_key_1).encode())
                print("send 2-1")
         

    
        print(part_key_1,sep="\n")
        
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='bye':
              break
            print (f"from client {clientAddress}:", msg)
            if self.csocket==users[0]:
                users[1].send(str(msg).encode())
            elif self.csocket==users[1]:
                users[0].send(str(msg).encode())
        print ("Client at ", clientAddress , " disconnected...")
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    
    server.listen(1)
    clientsock, clientAddress = server.accept()
    users.append(clientsock)
    print(users)
    clientsock.send(bytes(str(p),'UTF-8'))
    clientsock.send(bytes(str(g),'UTF-8'))
    
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
