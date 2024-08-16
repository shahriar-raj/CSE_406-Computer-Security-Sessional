
# first of all import the socket library 
import importlib
import socket  
import random
from BitVector import *
from Crypto.Util.number import getPrime

task_1 = importlib.import_module("1905105_task1_helper")
task_2 = importlib.import_module("1905105_task2_helper")
# next create a socket object 
s = socket.socket()         
print ("Socket successfully created")
 
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345               
 
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
 
# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")            
 
# a forever loop until we interrupt it or 
# an error occurs 
while True: 
 
# Establish connection with client. 
  c, addr = s.accept()     
  print ('Got connection from', addr )
  print("Connected to Alice")
  # send a thank you message to the client. encoding to send byte type. 
  c.send('Bob'.encode('utf-8'))

  A = [0,0]
  a = int(c.recv(1024).decode())
  c.send('a received'.encode('utf-8'))

  b = int(c.recv(1024).decode())
  c.send('b received'.encode('utf-8'))

  x = int(c.recv(1024).decode())
  c.send('x received'.encode('utf-8'))
  y = int(c.recv(1024).decode())
  c.send('y received'.encode('utf-8'))

  A[0] = int(c.recv(1024).decode())
  c.send('A[0] received'.encode('utf-8'))
  A[1] = int(c.recv(1024).decode())
  c.send('A[1] received'.encode('utf-8'))
  
  p = int(c.recv(1024).decode())
  c.send('p received'.encode('utf-8'))
  
  kb = random.getrandbits(128)

  B = task_2.multiplication(x, y, kb, p, a)
  c.send(str(B[0]).encode('utf-8'))
  string2 = c.recv(1024).decode()
  c.send(str(B[1]).encode('utf-8'))
  string2 = c.recv(1024).decode() 
  
  R = task_2.multiplication(A[0], A[1], kb, p, a)
  key = BitVector(intVal=R[0], size=128).get_bitvector_in_ascii()
  
  # print(len(key))
  if(len(key)<16):
    key += " "*(16-len(key))
  print(c.recv(1024).decode())
  c.send('From Bob: Start Transmission'.encode('utf-8'))
  
  IV_str = c.recv(1024).decode()
  print('Received IV From Alice:', IV_str)
  c.send('Ok'.encode('utf-8'))
  i=0
  IV = []
  while i<len(IV_str):
    IV.append(IV_str[i:i+2])
    i += 2

  cypher_text = c.recv(1024).decode()
  # print("length of cypher text: ", len(cypher_text))
  c.send('From Bob: Message Received'.encode('utf-8'))
  print('\nReceived Cypher text:\n', cypher_text)
  decrypted_text = task_1.Decryption(cypher_text, task_1.ascii_to_hex(key), task_1.round_key_generator(task_1.ascii_to_hex(key)), IV)
  decrypted_text_ascii = ""
  # print(decrypted_text)
  i=0
  while i < len(decrypted_text):
      decrypted_text_ascii = decrypted_text_ascii+task_1.hex_to_ascii(decrypted_text[i])
      i += 1
  
  print("\nDecrypted text:", decrypted_text_ascii)
  # Close the connection with the client 
  c.close()
   
  # Breaking once connection closed
  break
