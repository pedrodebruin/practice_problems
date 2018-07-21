# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 19:19:58 2018

@author: Pedro
"""
"""
The basic operations are len(A), A.append(42), A.remove(2), and A.insert(3, 28).
"""
A = [1,5,2,4,6,7,7,4]
print('A={}'.format(A))
print('len(A): {}'.format(len(A)))
A.append(6)
print('A={}'.format(A))
A.remove(7)
print('A={}'.format(A))
A.insert(1,27)
print('A={}'.format(A))

"""
Your input is an array of integers, and you have to reorder 
its entries so that the even entries appear first.
"""


def even_odd(A):
    
    even_A, odd_A = [], []
    
    for x in A:
        print (x)
        if x % 2 == 0:
            even_A.append(x)
        else:
            odd_A.append(x)
    
    print (even_A)
    print (odd_A)
    #A = even_A
    #A.extend(odd_A)   # extend is an in-place function
    # cleanest imho:
    A = even_A + odd_A
    return A
    
if __name__=='__main__':
    
    A = [1,7,6,4,8,7,2,5,4,39,10]
    
    A_even_odd = even_odd(A)
    
    print(A_even_odd)