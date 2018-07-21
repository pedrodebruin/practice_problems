# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import random

## Convert string to binary
#st = 'hello'
#ba = bytearray(st)


## Print integer in binary
#x = 1024
#b_x = bin(x)
#print b_x


"""
The key methods in random are random.randrange(28), random.randint(8,16),
random.random(), random.shuffle(A), and random.choice(A).

random() returns an int from 0 to 1
>>> random.random()
0.7890067922205295

uniform(a,b) returns a float from a to b

# randrange returns an int from 0 to x-1. randint(x) returns an int from 0 to x
>>> random.randrange(1,3)
2

random.shulffe(A) shuffles A and random.choice(A) picks a random element of A
"""


"""
1.1 Computing the parity of a word

The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. For
example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity checks are used to detect
single bit errors in data storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word.
"""


def parity(x):
    result = 0
    print("original x is {}. x in binary is {}".format(x, bin(x)))
    
    n=1
    while x:
        print(bin(x))
        #print('bin(x)={}'.format(bin(x)))
        #print('bin(n)={}'.format(bin(n)))
        result ^= x & 1
        #print(bin(x&n))
        #print(result)
        x >>= 1
    
    return result


if __name__=='__main__':
    
    x = 11
    
    print('Parity of x: {}'.format(parity(x)))
    
    