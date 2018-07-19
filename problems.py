
#----------------------------------------#

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


def fact(x):

    if x==0:
        return 1
    else:
        return x*fact(x-1)


Solution:
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(raw_input())
print fact(x)
#----------------------------------------#


#----------------------------------------#
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

Solution:
n=int(raw_input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print d
#----------------------------------------#


#----------------------------------------#
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

Solution:
values=raw_input()
l=values.split(",")
t=tuple(l)
print l
print t
#----------------------------------------#


#----------------------------------------#
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

Solution:
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()
#----------------------------------------#


#----------------------------------------#
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 

Solution:
#!/usr/bin/env python
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)
#----------------------------------------#


def findIndex(A,x):

    l,h = findRange(A,x)

    i = l
    while x > A[i]:
        i=i+1

    return i-1


def findRange(A,x):
    l = 0
    h = 1
    print x, A[h]
    while x > A[h]:
        l = h
        h = min(2*h,len(A)-1)
        print l,h

    return l,h


def main():

    A = [1,2,3,4,5,6,7,10,15,20,25,27,30,36,450]
    x = 45

    i=0
    i = findIndex(A,x)

    print("Nearest position of x is index {0} with value {1}".format(i, A[i]))


if __name__=="__main__":
    main()

