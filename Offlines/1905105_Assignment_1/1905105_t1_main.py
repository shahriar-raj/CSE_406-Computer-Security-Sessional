import importlib
import time
import random
from BitVector import *

task_1 = importlib.import_module("1905105_task1_helper")

#Input.........................................
key = input("key: \nIn ASCII: ")
if(len(key)<16):
    key += " "*(16-len(key))
if(len(key)>16):
    key = key[:16]
key = task_1.ascii_to_hex(key)
print("In HEX: ", end="")
i=0
while i < len(key):
    print(str.upper(key[i]), end=" ")
    i += 1
print("")
plain_text = input("\nplain text: \nIn ASCII: ")
#...............................................

#processing plain_text as a multiple of 16 and making it into a hex string----------------------
if(len(plain_text)==0):
    plain_text = " "*16 # if the plain text is empty, it will be filled with spaces
if(len(plain_text)%16 != 0):
    plain_text += " "*(16-len(plain_text)%16) # if the plain text is not a multiple of 16, it will be filled with spaces

# print(plain_text)
# print(Block_count)
plain_text_h = task_1.ascii_to_hex(plain_text) # makes the plain text into a hex string
print("In HEX: ", end="")
i=0
while i < len(plain_text_h):
    print(str.upper(plain_text_h[i]), end=" ")
    i += 1
print("")
#------------------------------------------------------------------------------------------------

#key_scheduling---------------------------------------------------------------------------------
k_start_time = time.time()
key_schedule = task_1.round_key_generator(key)
k_end_time = time.time()
k_time = (k_end_time - k_start_time)*1000
#------------------------------------------------------------------------------------------------

#Generating IV-----------------------------------------------------------------------------------
IV = task_1.Generate_IV()
# print(IV)
stored_IV = IV
#................................................................................................

#Encryption-------------------------------------------------------------------------------------
c_start_time = time.time()
cypher_text = task_1.Encryption(plain_text, key, key_schedule, IV)
cypher_text_ascii = ""
print("\nCyphered text: \nIn HEX: ", end="")
i=0
while i < len(cypher_text):
    j=0
    while j < len(cypher_text[i]):
        print(str.upper(cypher_text[i][j]), end=" ")
        j += 1
    cypher_text_ascii = cypher_text_ascii+task_1.hex_to_ascii(cypher_text[i])
    i += 1

print("")
print("In ASCII:")
print(cypher_text_ascii)
c_end_time = time.time()
c_time = (c_end_time - c_start_time)*1000
#------------------------------------------------------------------------------------------------

#Decryption-------------------------------------------------------------------------------------
IV = stored_IV
d_start_time = time.time()
decrypted_text = task_1.Decryption(cypher_text_ascii, key, key_schedule, IV)
decrypted_text_ascii = ""
print("\nDecyphered text: \nIn HEX: ", end="")
i=0
while i < len(decrypted_text):
    j=0
    while j < len(decrypted_text[i]):
        print(str.upper(decrypted_text[i][j]), end=" ")
        j += 1
    decrypted_text_ascii = decrypted_text_ascii+task_1.hex_to_ascii(decrypted_text[i])
    i += 1

print("")
print("In ASCII: "+decrypted_text_ascii)
d_end_time = time.time()
d_time = (d_end_time - d_start_time)*1000
#------------------------------------------------------------------------------------------------

print("\nExecution time Details:")
print(f"Key Scheduling time: {k_time:.4f} ms")
print(f"Encryption time: {c_time:.4f} ms")
print(f"Decryption time: {d_time:.4f} ms")