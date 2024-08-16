import random
import time
from BitVector import *

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]


Rc = [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="04"), BitVector(hexstring="08"), BitVector(hexstring="10"),
      BitVector(hexstring="20"), BitVector(hexstring="40"), BitVector(hexstring="80"), BitVector(hexstring="1B"), BitVector(hexstring="36")]

AES_modulus = BitVector(bitstring='100011011')

def ascii_to_hex(string): # makes the ascii string into a hex string
    i = 0
    string_hex = []
    while i < len(string):
        hex_key = int(ord(string[i]))
        hex_key = BitVector(intVal=hex_key, size=8)
        string_hex.append(hex_key.get_hex_string_from_bitvector())
        i += 1
    return string_hex

def hex_to_ascii(hex_string): # makes the hex string into a ascii string
    i = 0
    string_ascii = ""
    while i < len(hex_string):
        ascii_key = BitVector(hexstring=hex_string[i])
        string_ascii += ascii_key.get_bitvector_in_ascii()
        i += 1
    return string_ascii

# takes a 4 byte hex string and returns a 4 byte hex string by 3 operations.
# The function is used in the key schedule
def g(string, round): 
    w_i = [0,0,0,0]
    w_i[0:3] = string[1:4]
    w_i[3] = string[0]
    w_i[0:4] = [Sbox[BitVector(hexstring=w_i[0]).intValue()], Sbox[BitVector(hexstring=w_i[1]).intValue()], Sbox[BitVector(hexstring=w_i[2]).intValue()], Sbox[BitVector(hexstring=w_i[3]).intValue()]]
    w_i[0:4] = [BitVector(intVal=w_i[0], size=8).get_bitvector_in_hex() , BitVector(intVal=w_i[1], size=8).get_bitvector_in_hex() , BitVector(intVal=w_i[2], size=8).get_bitvector_in_hex(), BitVector(intVal=w_i[3], size=8).get_bitvector_in_hex()]
    w_i[0] = (BitVector(hexstring=w_i[0])^Rc[round]).get_bitvector_in_hex()
    return w_i

def substitute_bytes(state):
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            state[i][j] = Sbox[BitVector(hexstring=state[i][j]).intValue()]
            state[i][j] = BitVector(intVal=state[i][j], size=8).get_bitvector_in_hex()
            j += 1
        i += 1
    return state

def inv_substitute_bytes(state):
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            state[i][j] = InvSbox[BitVector(hexstring=state[i][j]).intValue()]
            state[i][j] = BitVector(intVal=state[i][j], size=8).get_bitvector_in_hex()
            j += 1
        i += 1
    return state

def Mix_Columns(state):
    new_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # new state matrix
    i=0
    while i<4:
        j=0
        while j<4:
            k=0
            temp = BitVector(hexstring="00")
            while k<4:
                # print(Mixer[i][k])
                # print(state[k][j])
                multiple = Mixer[i][k].gf_multiply_modular(BitVector(hexstring=state[k][j]), AES_modulus, 8)
                # print(multiple)
                temp = temp^multiple
                k+=1
            new_state[i][j] = temp.get_bitvector_in_hex()
            # print(new_state[i][j])
            j+=1
        i+=1
    return new_state

def inv_Mix_Columns(state):
    new_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # new state matrix
    i=0
    while i<4:
        j=0
        while j<4:
            k=0
            temp = BitVector(hexstring="00")
            while k<4:
                # print(Mixer[i][k])
                # print(state[k][j])
                multiple = InvMixer[i][k].gf_multiply_modular(BitVector(hexstring=state[k][j]), AES_modulus, 8)
                # print(multiple)
                temp = temp^multiple
                k+=1
            new_state[i][j] = temp.get_bitvector_in_hex()
            # print(new_state[i][j])
            j+=1
        i+=1
    return new_state


def offset(state):
    i = 0
    while i < 4:
        j = 0
        while j < i:
            state[i].append(state[i][0])
            state[i].pop(0)
            j += 1
        i += 1
    return state

def inv_offset(state):
    i = 0
    while i < 4:
        j = 0
        while j < i:
            state[i].insert(0, state[i][3])
            state[i].pop(4)
            j += 1
        i += 1
    return state

def add_xor_op(string1, string2):
    i = 0
    string_xor = []
    while i < len(string1):
        xor = BitVector(hexstring=string1[i])^BitVector(hexstring=string2[i])
        string_xor.append(xor.get_bitvector_in_hex())
        i += 1
    return string_xor

def round_key_generator(string):
    w=[]
    round = 0
    while round < 11:
        if round == 0:
            w.append(string[0:4])
            w.append(string[4:8])
            w.append(string[8:12])
            w.append(string[12:16])
        else:
            w.append(add_xor_op(g(w[round*4-1], round-1),w[round*4-4]))
            w.append(add_xor_op(w[round*4],w[round*4-3]))
            w.append(add_xor_op(w[round*4+1],w[round*4-2]))
            w.append(add_xor_op(w[round*4+2],w[round*4-1]))          
        round += 1
    return w  

def Add_Round_Key(state, round_keys, round):
    temp_mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    i = 0
    while i < 4:
        j=0
        while j < 4:
            temp_mat[j][i] = round_keys[round*4+i][j]
            j+=1
        i += 1

    i = 0
    while i < 4:
        state[i] = add_xor_op(state[i], temp_mat[i])
        i += 1
    return state

def making_matrix_from_round_keys(round_keys,round):
    temp_mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    i = 0
    while i < 4:
        j=0
        while j < 4:
            temp_mat[j][i] = round_keys[round*4+i][j]
            j+=1
        i += 1
    return temp_mat

def Add_matrix(state, temp_mat):
    i = 0
    while i < 4:
        state[i] = add_xor_op(state[i], temp_mat[i])
        i += 1
    return state

def Block_encrypt(plain_text, key, round_keys):
    # print(round_keys)
    i=0
    state=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    while i<4:
        j=0
        while j<4:
            state[i][j] = plain_text[j*4+i]
            j += 1
        i+=1
    # print(state)
    state = Add_Round_Key(state, round_keys, 0)
    # print(state)
    round_count = 1
    while round_count < 11:
        state = substitute_bytes(state)
        state = offset(state)
        if round_count != 10:
            state = Mix_Columns(state)
        temp_mat = making_matrix_from_round_keys(round_keys,round_count)
        state = Add_matrix(state, temp_mat)
        # print(state)
        round_count += 1
    c_t=[]
    i=0
    while i<4:
        j=0
        while j<4:
            c_t.append(state[j][i])
            j+=1
        i+=1
    return c_t

def Block_decrypt(cypher_text, key, round_keys):
    # round_keys = round_key_generator(key)
    i=0
    state=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    while i<4:
        j=0
        while j<4:
            state[i][j] = cypher_text[j*4+i]
            j += 1
        i+=1
    # print(state)
    state = Add_Round_Key(state, round_keys, 10)
    round_count = 9
    while round_count >= 0:
        state = inv_offset(state)
        state = inv_substitute_bytes(state)
        temp_mat = making_matrix_from_round_keys(round_keys,round_count)
        state = Add_matrix(state, temp_mat)
        if round_count != 0:
            state = inv_Mix_Columns(state)
        # print(state)
        round_count -= 1
    p_t=[]
    i=0
    while i<4:
        j=0
        while j<4:
            p_t.append(state[j][i])
            j+=1
        i+=1
    return p_t

def Generate_IV():
    IV1 = []
    while len(IV1) < 16:
        random_bitvector = BitVector(intVal=random.getrandbits(8), size=8)
        IV1.append(random_bitvector.get_hex_string_from_bitvector())
    return IV1

def Encryption(plain_text, key, key_schedule, IV):
    Block_count = int(len(plain_text)/16) # number of blocks
    # print("Block count: ", Block_count)
    plain_text = ascii_to_hex(plain_text) # makes the plain text into a hex string
    cypher_text=[]
    i=0
    while i<Block_count:
        plain_text_i = plain_text[i*16:(i+1)*16]
        plain_text_i = add_xor_op(plain_text_i, IV)
        cypher_text_i = Block_encrypt(plain_text_i, key, key_schedule)
        IV = cypher_text_i
        cypher_text.append(cypher_text_i)
        i+=1
    return cypher_text

def Decryption(cypher_text_ascii, key, key_schedule, IV):
    Block_count = int(len(cypher_text_ascii)/16) # number of blocks
    cypher_text = ascii_to_hex(cypher_text_ascii) # makes the cypher text into a hex string
    decrypted_text=[]
    i=0
    while i<Block_count:
        cypher_text_i = cypher_text[i*16:(i+1)*16]
        decrypted_text_i = Block_decrypt(cypher_text_i, key, key_schedule)
        decrypted_text_i = add_xor_op(decrypted_text_i, IV)
        IV = cypher_text_i
        decrypted_text.append(decrypted_text_i)
        i+=1
    return decrypted_text