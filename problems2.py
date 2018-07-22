#----------------------------------------#
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 


def matrixmaker_naive(X,Y):

        lol_matrix = []
	for x in range(0,X):
		row = []
		for y in range(0,Y):
			row.append(x*y)

		lol_matrix.append(row)

	return lol_matrix


print("Please enter 2 integers separated by a comma")
X,Y = [ int(x) for x in raw_input().split(',') ]
print(matrixmaker_naive(X,Y))
#----------------------------------------#

#----------------------------------------#
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
list_of_words = raw_input().split(',')
list_of_words.sort()
print(list_of_words)

or

items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)
#----------------------------------------#

#----------------------------------------#
Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

def get_lines(lines=[]):

        print("Please enter a new line. Enter 'END' or nothing to terminate.")
        newline = raw_input()

        if newline in [ "", "END" ]:
                return lines
        else:
                lines.append(newline)
                get_lines(lines)

        return lines

paragraph = get_lines()
paragraph_upper = '\n'.join(x.upper() for x in paragraph)
print(paragraph_upper)

#----------------------------------------#

#----------------------------------------#
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

Solution:
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
#----------------------------------------#

#----------------------------------------#
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

print("Please enter 4 comma-separated 4-digit binary numbers")
bin_num_list = [ xbin for xbin in raw_input().split(',') ]
num_list = [ int(xbin, 2) for xbin in bin_num_list ]
dict_num_bin = dict(zip(num_list,bin_num_list))

print(",".join( xbin for x,xbin in dict_num_bin.items() if x%5==0))

or 

value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print ','.join(value)
#----------------------------------------#

#----------------------------------------#
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print ",".join(values)
#----------------------------------------#

#----------------------------------------#
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

# My solution is too wordy because it does not use the built-in methods of the str class .isdigit() and .isalpha()
import string
alphabet = string.ascii_letters  # "abc....xyzABC...XYZ"
alphabet = [ x for x in alphabet ]
digits = range(0,10)

print("Please enter any alphanumerical sentence")
input_str = raw_input()
num_digits, num_letters = 0,0
for x in input_str:
	if x not in alphabet and int(x) not in digits:
		continue  # This is an exotic character such as punctuation

	if int(x) in digits: num_digits = num_digits+1
	if x in alphabet: num_letters = num_letters+1

print("Number of letters = {} \nNumber of digits = {}".format(num_letters, num_digits))

Solution:
s = raw_input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]
#----------------------------------------#

#----------------------------------------#
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
s = raw_input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print "UPPER CASE", d["UPPER CASE"]
print "LOWER CASE", d["LOWER CASE"]
#----------------------------------------#

#----------------------------------------#
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

# My solution first:
print("Please enter a single digit")
a = raw_input()
if not a.isdigit():
	print("That is a not a digit, please enter a digit")
	a = raw_input()

n_sum = sum([ int(a*i) for i in range(1,5) ])
print(n_sum)

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
a = raw_input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print n1+n2+n3+n4
#----------------------------------------#

#----------------------------------------#
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9


l_num = raw_input().split(',')
l_odd = [ x for x in l_num if int(x)%2!=0 ]
print(",".join(x for x in l_odd))

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
values = raw_input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print ",".join(numbers)
#----------------------------------------#

Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500


# My solution
def get_trans(trans_dict={'D':0, 'W':0}):

        newtrans = raw_input()
        # Enter nothing to terminate
        if newtrans == "":
                return trans_dict

        trans_type, trans_amt = newtrans.split(" ")
        trans_dict[trans_type] += int(trans_amt)
        get_trans(trans_dict)

        return trans_dict

total_trans = get_trans()
print("Net change: {}".format( total_trans['D'] - total_trans['W'] ))


Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
netAmount = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print netAmount
#----------------------------------------#

#----------------------------------------#
Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


import string

def is_pwd_good(pwd):

	num_digits = 0
	num_lower = 0
	num_upper = 0
	num_exotic = 0

        if len(pwd) < 6:
		return False

        if len(pwd) > 12:
		return False

	for c in pwd:
		if c.isdigit():
			num_digits +=1
		elif c.isalpha():
			if c.islower(): num_lower += 1
			else: num_upper += 1
		elif c in ['$', '#', '@']:
			num_exotic += 1

	return ( num_digits>0 and num_lower>0 and num_upper >0 and num_exotic > 0 )

def good_pwd_list(pwd_list):
	good_pwd_list = []
	for pwd in pwd_list:
		good_pwd_list.append(is_pwd_good(pwd))

	return pwd_list[good_pwd_list]


pwd_list = raw_input().split(',')
print(good_pwd_list)

Solutions:
import re
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print ",".join(value)
#----------------------------------------#

#----------------------------------------#
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


# My solution
def get_candidate(list_cand=[]):

	new_cand = raw_input().split(',')

	if new_cand = "":
	    return list_cand
	
	new_cand = tuple( new_cand[0], new_cand[1], new_cand[2] )
        list_cand.append(new_cand)
        get_candidate(list_cand)


list_candidates = get_candidate()
list_candidates.sort(key=itemgetter(0,1,2))

print(list_candidates)

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.

Solutions:
from operator import itemgetter, attrgetter

l = []
while True:
    s = raw_input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print sorted(l, key=itemgetter(0,1,2))
#----------------------------------------#

#----------------------------------------#
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield


class DivBy7():
	def __init__(self):
		numrange = range(0,int(raw_input())+1)
		self.mygen = ( x for x in numrange if x%7==0 )  #parenthesis give a generator

divby7_100 = DivBy7()
for x in divby7_100.mygen:
	print(x)


# The 'official' solution is not a class
Solution:
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in putNumbers(100):
    print i
#----------------------------------------#

