#----------------------------------------#
Question 21
Level 3

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

import math

def get_step(dict_steps={'UP':0, 'DOWN':0, 'LEFT':0, 'RIGHT':0}):

        print("Please enter a direction plus a integer, e.g. UP 2")
        step = raw_input()

        if not step:
                print("You entered nothing, terminating...")
                return dict_steps

        step = step.split(" ")
        direction, nsteps = step[0], int(step[1])
        dict_steps[direction] += nsteps

        return get_step(dict_steps)


def get_distance(dict_steps):

        print (dict_steps)
        delta_x = dict_steps['RIGHT'] - dict_steps['LEFT']
        delta_y = dict_steps['UP'] - dict_steps['DOWN']

        return round(math.sqrt(delta_x**2 + delta_y**2))

steps_taken = get_step()
print("The distance travelled was {}".format(get_distance(steps_taken)))

Solution:
import math
pos = [0,0]
while True:
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print int(round(math.sqrt(pos[1]**2+pos[0]**2)))
#----------------------------------------#

#----------------------------------------#
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.

# str.count() method is your friend
s = raw_input()

count_dict = {}
for c in s:
	count_dict[c] = s.count(c)

count_dict.sort()
print(count_dict)

Solution:
freq = {}   # frequency of words in text
line = raw_input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
    print "%s:%d" % (w,freq[w])
#----------------------------------------#

#----------------------------------------#
Question 23
level 1

Question:
    Write a method which can calculate square value of number

Hints:
    Using the ** operator

Solution:
def square(num):
    return num ** 2

print square(2)
print square(3)
#----------------------------------------#

#----------------------------------------#
Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function
    
Hints:
    The built-in document method is __doc__


Solution:
print abs.__doc__
print int.__doc__
print raw_input.__doc__

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print square(2)
print square.__doc__
#----------------------------------------#

#----------------------------------------#
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later




class Employee():

        name = 'Pedro'
	def __init__(self, name=None):
		self.name = name	      
		Employee.company = 'Affirm'   # <---- this is a class variable


emp_1 = Employee('Pedro de Bruin')
print("{} works at {}".format(emp_1.name, emp_1.company)



Solution:
class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print "%s name is %s" % (Person.name, jeffrey.name)

nico = Person()
nico.name = "Nico"
print "%s name is %s" % (Person.name, nico.name)
#----------------------------------------#

#----------------------------------------#
Question:
Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the val

Solution
def SumFunction(number1, number2):
	return number1+number2

print SumFunction(1,2)

#----------------------------------------#
Question:
Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.

Solution
def printValue(n):
	print str(n)

printValue(3)
	

#----------------------------------------#
Question:
Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.

Solution
def printValue(n):
	print str(n)

printValue(3)

#----------------------------------------#
2.10

Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.

Solution
def printValue(s1,s2):
	print int(s1)+int(s2)

printValue("3","4") #7


#----------------------------------------#
2.10


Question:
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings

Solution
def printValue(s1,s2):
	print s1+s2

printValue("3","4") #34

#----------------------------------------#
2.10


Question:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string

Solution
def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1>len2:
		print s1
	elif len2>len1:
		print s2
	else:
		print s1
		print s2
		

printValue("one","three")



#----------------------------------------#
2.10

Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.

Solution
def checkValue(n):
	if n%2 == 0:
		print "It is an even number"
	else:
		print "It is an odd number"
		

checkValue(7)


#----------------------------------------#
2.10

Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.


def printdict():
	dict_range = range(1,4)
	for n in dict_range:
		adict[n] = n**2
	print adict

Solution
def printDict():
	d=dict()
	d[1]=1
	d[2]=2**2
	d[3]=3**2
	print d
		

printDict()



#----------------------------------------#
3.4

Question:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.

li = range(11)
even_list = filter(lambda x: x%2==0, li)
print(even_list)

Solution
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print evenNumbers


#----------------------------------------#
3.4

Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

sq_list = map(lambda x: x**2, range(11))
print(sq_list)



Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

Solution
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print evenNumbers




#----------------------------------------#
3.5

Question:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

even_1_20 = filter(lambda x: x%2==0, range(1,21))

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

Solution
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print evenNumbers


#----------------------------------------#
3.5

Question:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.

Solution
squaredNumbers = map(lambda x: x**2, range(1,21))
print squaredNumbers




#----------------------------------------#
7.2

Question:
Define a class named American which has a static method called printNationality.


class American():

	_country = USA

	def __init__(self):
		pass

	@staticmethod
	def printNationality():
		print(_country)


Hints:

Use @staticmethod decorator to define class static method.

Solution
class American(object):
    @staticmethod
    def printNationality():
        print "America"

anAmerican = American()
anAmerican.printNationality()
American.printNationality()




#----------------------------------------#

7.2

Question:
Define a class named American and its subclass NewYorker. 

Hints:

class American():
    @staticmethod
    def printNationality():
        print("America")

class NewYorker(American):

	@staticmethod
	def printState():
		print("New York")



Use class Subclass(ParentClass) to define a subclass.

Solution:

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print anAmerican
print aNewYorker




#----------------------------------------#


7.2

Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 


import math

class Circle():
	
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		self.area = math.pi*(self.radius**2)
		return self.area
Hints:

Use def methodName(self) to define a method.

Solution:

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()


