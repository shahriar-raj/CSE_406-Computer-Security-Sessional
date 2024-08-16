from BitVector import *
import time
import random
from Crypto.Util.number import getPrime

def point_addition(x1, y1, x2, y2, p):
    s= ((y2-y1)*pow(x2-x1,-1,p))%p
    x3 = (s**2 - x1 - x2)%p
    y3 = (s*(x1-x3) - y1)%p
    return (x3, y3)

def point_doubling(x1, y1, a, p):
    s = ((3*x1**2 + a)*pow(2*y1,-1,p))%p
    x3 = (s**2 - 2*x1)%p
    y3 = (s*(x1-x3) - y1)%p
    return (x3, y3)


def multiplication(x1, y1, k, p, a):
    bitstring = bin(k)[2:]
    xi = x1
    yi = y1
    i=1
    while i < len(bitstring):
        x1, y1 = point_doubling(x1, y1, a, p)
        if bitstring[i] == '1':
            x1, y1 = point_addition(x1, y1, xi, yi, p)
        i+=1
    return (x1, y1)

def main(Bitsize):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    a=0
    b=0
    p = getPrime(Bitsize)
    # print(p)
    while (4*a**3 + 27*b**2)%p == 0:
        a = random.randint(1, 100)
        b = y**2 - x**3 - a*x
    
    ka = random.getrandbits(Bitsize)
    # print(ka)

    A_start_time = time.time()
    A = multiplication(x, y, ka, p, a)
    A_end_time = time.time()
    A_time = (A_end_time - A_start_time)*1000

    kb = random.getrandbits(Bitsize)
    # print(kb)

    B_start_time = time.time()
    B = multiplication(x, y, kb, p, a)
    B_end_time = time.time()
    B_time = (B_end_time - B_start_time)*1000

    R_start_time = time.time()
    R = multiplication(A[0], A[1], kb, p, a)
    R_end_time = time.time()
    R_time = (R_end_time - R_start_time)*1000

    # print("A: ", A)
    # print("B: ", B)
    return A_time, B_time, R_time

