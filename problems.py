
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
def dict_sq(n):

	dict_n = {}
	for i in range(1,n+1):
		dict_n[i] = i*i

        return dict_n


n = int(raw_input())
print("Generating dictionary from 1 to {}".format(n))
dict_obj = dict_sq(n)
print(dict_obj)
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


import math

def formula(C,D,H):
	return int(round(math.sqrt(2*C*D/H)))

def func(list_D):

	return [ formula(50, D, 30) for D in list_D ]


print("Please enter a comma-separated list of numbers")
list_n = raw_input()
list_n = list_n.split(',')
list_n = [ float(x) for x in list_n ]
print(func(list_n))

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

#--------------------------------------------#


def find_attributes(request, dataset):
	    """
	    Takes in a dictionary {string: string} representing strings to search for in the input dataset and the attribute
	    to report for each.  Should output a dictionary of each requested element mapped to it's requested
	    attribute.

	    :param request:  {string: string} dictionary mapping from a requested search string to a requested attribute.
	    Search string can be anything while attribute will be one of:
		"first_idx": we want to output the index of the first instance of this element in the dataset
		"last_idx": we want to output the index of the final instance of this element in the dataset
		"count": we want the count of total occurrences of this element in the dataset
	    e.g. we might get a request like: {"apple": "first_idx", "orange": "last_idx", "pear": "count", ...}

	    :param dataset:  [string]  a simple list of strings, possibly including duplicates
	    e.g. ["orange", "apple", "orange", "pear", "avocado", "pear", "apple"]

	    :return: dictionary mapping each requested string to the requested (int) attribute, indices as None if no instances
	    """

	    # implement code here

	    out_dict = {}
            rev_dataset = [ dataset[-n] for n in range(1,len(dataset)+1) ]

	    for k,v in request.items():
		if v=="first_idx":
		    out_dict[k] = dataset.index(k)
		else if v=="last_idx":
		    out_dict[k] = rev_dataset.index(k)
		else if v=="count":
                    out_dict[k] = Counter(dataset.keys())
		else:
		    raise("The request '{}:{}'is not understood".format(k,v))

	    return out_dict



# SAMPLE TEST CASE
sample_request = {"apple": "first_idx", "orange": "last_idx", "pear": "count", "avocado": "first_idx"}
sample_dataset = ["orange", "apple", "orange", "pear", "avocado", "pear", "apple"]
sample_expected_output = {"apple": 1, "orange": 2, "pear": 2, "avocado": 4}
assert find_attributes(sample_request, sample_dataset) == sample_expected_output


### PROVIDED SOLUTION BELOW, MY SOLUTION ABOVE ###
#---------------------------------------------------------#

def find_attributes_naive(request, dataset):
    """
    Takes in a dictionary {string: string} representing strings to search for in the input dataset and the attribute
    to report for each.  Should output a dictionary of each requested element mapped to it's requested
    attribute.

    :param request:  {string: string} dictionary mapping from a requested search string to a requested attribute.
    Search string can be anything while attribute will be one of:
        "first_idx": we want to output the index of the first instance of this element in the dataset
        "last_idx": we want to output the index of the final instance of this element in the dataset
        "count": we want the count of total occurrences of this element in the dataset
    e.g. we might get a request like: {"apple": "first_idx", "orange": "last_idx", "pear": "count", ...}

    :param dataset:  [string]  a simple list of strings, possibly including duplicates
    e.g. ["orange", "apple", "orange", "pear", "avocado", "pear", "apple"]

    :return: dictionary mapping each requested string to the requested (int) attribute, indices as None if no instances
    """

    # naive solution
    output = {elem: 0 if attr is "count" else None for elem, attr in request.items()}
    for search_str, attr in request.items():
        if attr == "first_idx":
            for idx, elem in enumerate(dataset):
                if elem == search_str:
                    output[search_str] = idx
                    break
        elif attr == "last_idx":
            for idx, elem in enumerate(reversed(dataset)):
                if elem == search_str:
                    output[search_str] = len(dataset) - 1 - idx
                    break
        else:
            for idx, elem in enumerate(dataset):
                if elem == search_str:
                    output[search_str] += 1
    return dict(output)


def find_attributes_one_pass(request, dataset):
    """
    Takes in a dictionary {string: string} representing strings to search for in the input dataset and the attribute
    to report for each.  Should output a dictionary of each requested element mapped to it's requested
    attribute.

    :param request:  {string: string} dictionary mapping from a requested search string to a requested attribute.
    Search string can be anything while attribute will be one of:
        "first_idx": we want to output the index of the first instance of this element in the dataset
        "last_idx": we want to output the index of the final instance of this element in the dataset
        "count": we want the count of total occurrences of this element in the dataset
    e.g. we might get a request like: {"apple": "first_idx", "orange": "last_idx", "pear": "count", ...}

    :param dataset:  [string]  a simple list of strings, possibly including duplicates
    e.g. ["orange", "apple", "orange", "pear", "avocado", "pear", "apple"]

    :return: dictionary mapping each requested string to the requested (int) attribute, indices as None if no instances
    """

    # single pass solution
    output = {elem: 0 if attr is "count" else None for elem, attr in request.items()}
    for idx, elem in enumerate(dataset):
        if elem in request:
            if request[elem] == "count":
                # just add to the count
                output[elem] += 1
            elif request[elem] == "last_idx":
                # overwrite any previous index so we end up with final index
                output[elem] = idx
            else:
                # first_idx case, set if not already set
                if output[elem] is None:
                    output[elem] = idx
    return output


# SAMPLE TEST CASE
sample_request = {
    "apple": "first_idx",
    "orange": "last_idx",
    "pear": "count",
    "avocado": "first_idx"
}
sample_dataset = ["orange", "apple", "orange", "pear", "avocado", "pear", "apple"]
sample_expected_output = {"apple": 1, "orange": 2, "pear": 2, "avocado": 4}
assert find_attributes_naive(sample_request, sample_dataset) == sample_expected_output
assert find_attributes_one_pass(sample_request, sample_dataset) == sample_expected_output
