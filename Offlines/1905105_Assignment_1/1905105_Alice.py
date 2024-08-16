# Import socket module 
import importlib
import socket
import random
from BitVector import *
from Crypto.Util.number import getPrime

task_1 = importlib.import_module("1905105_task1_helper")
task_2 = importlib.import_module("1905105_task2_helper")

def list_to_string(s1):
    str1 = ""
    for ele in s1:
        str1 += ele
    return str1

# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 12345               
 
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
 
# receive data from the server and decoding to get the string.
if(s.recv(1024).decode() == 'Bob'):
    print("Connected to Bob")

x = random.randint(1, 100)
x = random.randint(1, 100)
y = random.randint(1, 100)
a=0
b=0
p = getPrime(128)
while (4*a**3 + 27*b**2)%p == 0:
    a = random.randint(1, 100)
    b = y**2 - x**3 - a*x

ka = random.getrandbits(128)
A = task_2.multiplication(x, y, ka, p, a)

s.send(str(a).encode('utf-8'))
string2 = s.recv(1024).decode()

s.send(str(b).encode('utf-8'))
string2 = s.recv(1024).decode()

s.send(str(x).encode('utf-8'))
string2 = s.recv(1024).decode()

s.send(str(y).encode('utf-8'))
string2 = s.recv(1024).decode()

s.send(str(A[0]).encode('utf-8'))
string2 = s.recv(1024).decode()

s.send(str(A[1]).encode('utf-8'))
string2 = s.recv(1024).decode()

s.send(str(p).encode('utf-8'))
string2 = s.recv(1024).decode()

B = [0,0]
B[0] = int(s.recv(1024).decode())
s.send('B[0] received'.encode('utf-8'))

B[1] = int(s.recv(1024).decode())
s.send('B[1] received'.encode('utf-8'))

R = task_2.multiplication(B[0], B[1], ka, p, a)
key = BitVector(intVal=R[0], size=128).get_bitvector_in_ascii()
# print("Key: ", key)

if(len(key)<16):
    key += " "*(16-len(key))

s.send('From Alice: Requesting Transmission Start'.encode('utf-8'))
print(s.recv(1024).decode())

IV = task_1.Generate_IV()
IV_str = list_to_string(IV)
s.send(IV_str.encode('utf-8'))
string2 = s.recv(1024).decode()

Message = input("\nEnter Message: ")
# print(IV)
# print(Message)
if(len(Message)==0):
    Message = " "*16 # if the plain text is empty, it will be filled with spaces
if(len(Message)%16 != 0):
    Message += " "*(16-len(Message)%16) # if the plain text is not a multiple of 16, it will be filled with spaces

cypher_text_M = task_1.Encryption(Message, task_1.ascii_to_hex(key), task_1.round_key_generator(task_1.ascii_to_hex(key)), IV)
cypher_text_ascii = ""
# print(cypher_text_M)
i=0
while i < len(cypher_text_M):
    cypher_text_ascii = cypher_text_ascii+task_1.hex_to_ascii(cypher_text_M[i])
    i += 1

# print("length of cypher text: ", len(cypher_text_ascii))
print("\nSent Cyphered text:\n", cypher_text_ascii)
# s.send(str(len(cypher_text_ascii)).encode('utf-8'))
s.send(cypher_text_ascii.encode('utf-8'))
print("\n"+s.recv(1024).decode())
# close the connection 
s.close()