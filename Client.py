import socket
import random

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


sup_num=[631, 919, 1657, 1801, 1951, 2269, 2437, 2791, 3169, 3571, 4219, 4447, 5167, 5419, 6211, 7057, 7351, 8269, 9241]
secret_key=sup_num[random.randint(1,18)]

p =  client.recv(1024)
p=p.decode()
print("From Server open key 1 :" ,p)
g =  client.recv(1024)
g=g.decode()
print("From Server open key 2 :" ,g)


first_half_key=int(p)**int(secret_key)%int(g)
client.sendall(bytes(str(first_half_key),'UTF-8'))
print("AND this is my part of key: ",first_half_key)

data = client.recv(2048).decode()

data=data[2:-1]
data=int(data)
print("Getting part Form User 1: ",data)
full_key=int(data)**int(secret_key)%int(g)
print("This is Full Key:",full_key)

def encrypt_message(full_key, message):
  encrypted_message = ""
  key = full_key
  print(key)
  for c in message:
       encrypted_message += chr(ord(c)+key)
  return encrypted_message

def decrypt_message(full_key, encrypted_message):
  decrypted_message = ""
  key = full_key
  for c in encrypted_message:
      decrypted_message += chr(ord(c)-key)
  return decrypted_message
             
while True:
  
  out_data = input("Enter the message: ")
  encrypted_message=encrypt_message(full_key,out_data)
  client.sendall(bytes(encrypted_message,'UTF-8'))
  if out_data=='bye':
    break
  msg=client.recv(2048).decode()
  dec_msg = decrypt_message(full_key,msg)
  print("Message from 2 user: ",dec_msg)
  
client.close()
