########
KEYWORDS
########

'''
These are multi line comments.
seperated by three apostrophe's
'''

# This is a single line comment by the way.



and
def
exec
if
not
return
assert
del
finally
import
or
try
break
elif
for
in
pass
while
class
else
from
is
print
yelid
continue
except
global
lambda
raise



#########################################

   F U N C T I O N S  &  M O D U L E S

#########################################


def add(num1, num2)


Some important functions.


print()

input()  # to take input from the user. By default it is a string.

int()   # Function integer. If you are expecting an interger input, write as belo

int(input("Enter an integer"))



A module can have multiple functions, variables and classes.

Some important modules.

# Math is a module and has multiple functions in it.


math.pi()

math.sin(90)



#####################################

     O  P  E  R  A  T  O  R  S

######################################


1. Arity of the Operator.

        Number of operands required to user the operator.



2. Precedence of the Operator.

        BODMAS nahi PEMDAS, Parantheses, Exponents, Multiplication, Division, Addition and Substraction


3. Associativity of the Operator.

        if two operands have same Priority, we move from left to right

        that is in

        a = b + c -d

        we add b and c first and then substract d.



Boolean - True or False

Equal - ==


Bitwise operators

        Binary Operators

        and         &       --> to turn off the bit
        or          |       --> turn on the bit
        xor         ^       --> toggle the bit.


        Unary Operator

        negation    ~       --> inversion of all bits

        left shift  <<      --> shift bits by n bits
            number << 2     --> number * 2^n where n is the number of bits shifted.

        right shift >>      --> shifts bits to right by n bits.
            number >> 2     -->

Logical Operators

        and

        or

        not



Membership Operators

        in

        not in

Identity Operators

        is

        is not






Relational

        !=	Not equal to				(5 != 2) is True, (5 != 5) is False
        >	Greater than				(5 > 5) is False
        <	Less than					(5 < 5) is False
        >=	Greater than or equal to	(2 >= 2) is True
        <=	Less than or equal to		(5 <= 2) is False

Arithmatic


        +     	addition
        -     	subtraction
        *     	multiplication
        /     	division                 In 2.x division returns integer, while in 3.x division returns float.
        %     	modulus
        **     	exponentiation
        //     	floor division


            Python 3.x doesn't suppport ternary operators.
            So a++ is not valid






Priority order would be PEMDAS

Parantheses
Exponents
Multiplication and Division
Addition and Substraction




###########################

		Strings

###########################


You can print raw data by adding an r just before the quotes in print.
>>> print(r"Hello How are you. It's important to write directory names clear as escaping special chracrecters is difficult. For example: C:\sree\kanth\sai")


String literals can span multiple lines.
>>> print("""

	Hello How are you

	I am fine

	""")


Strings can be concatenated using + and repeated using *
>>> "Sai "*8
'Sai Sai Sai Sai Sai Sai Sai Sai '

>>> "Sai" + " " + "Sreekanth"
'Sai Sreekanth'


Two strings that are placed next to each other are automatically concatenated.
>>> print("Hello How are you"
... "?   I am Fine!")
Hello How are you?   I am Fine!


Strings can be indexed. That is converted into a list.
>>> word="Sreekanth"
>>> for i in range(len(word)):
...     print(word[i])
...
S
r
e
e
k
a
n
t
h


Strings can be sliced :D

>>> word
'vishnu'
>>>
>>> word[:2]
'vi'
>>> word[2:]
'shnu'
>>> word[:2]+word[2:]
'vishnu'
>>> word[:7]+word[7:]
'vishnu'
>>> word[:7]
'vishnu'
>>> word[7:]
''

 -5 -4 -3  -2  -1
 H   e  l   l   o

 0 1 2 3 4 -1 -2 -3 -4 -5

Strings are immutable. A new object has to be created if you want to modify a string.



############################################ S T R I N G   F O R M A T T I N G



















###########################

         L I S T S

###########################



Lists are mutable. Meaning you can change the content of the lists.


>>> s = []
>>> type(s)
<class 'list'>

>>> s=[1,2,4,9]

>>> s
[1, 2, 4, 9]

>>> s[0]
1

>>> s[1]
2

>>> s[-1]
9


>>> len(s)
4

>>> s.append(16)

>>> s
[1, 2, 4, 9, 16]


One can also nest lists.

>>> s
[1, 2, 4, 9, 16]

>>> c=[1,8,27]

>>> a=[s,c]
>>> a
[[1, 2, 4, 9, 16], [1, 8, 27]]


You can assign to lists, slices of lists and also empty part of full lists.

>>> letters[2:5]=['C','D','E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g', 'h', 'i', 'j', 'k', 'l']


>>> letters[:]=[]
>>> letters
[]





List comparision

l1 < l2








#################################

|         T  U  P  L  E         |

#################################









###########################

		S  E  T  S

###########################

-  A set is an unordered collection with no duplicate elements.


>>> s={}
>>> type(s)
<class 'dict'>

>>> s=set()
>>> s
set()
>>> type(s)
<class 'set'>

>>> s=set('123445665456765432')
>>> s
{'5', '6', '1', '4', '2', '3', '7'}

>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}






















######################################

		D I C T I O N A R I E S

######################################

- It is best to think of a dictionary as a set of key: value pairs,
  with the requirement that the keys are unique (within one dictionary).

- A pair of braces creates an empty dictionary: {}.


>>> D={'sai':'sree','sai':'kanna'}
>>> D
{'sai': 'kanna'}
>>> D={'sai':'sree','sree':'sreekanth','kanna':'sai'}
>>> D
{'sai': 'sree', 'sree': 'sreekanth', 'kanna': 'sai'}


- When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

>>> for i,v in enumerate(D):
...     print(i,v)
...
0 sai
1 sree
2 kanna


- To loop over two or more sequences at the same time, the entries can be paired with the zip() function.


>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.































##################################

     C O N T R O L   F L O W

##################################



CONDITIONS AND LOOPS


You can also do this if...else...

print("Do this" if 0 < 1 else "Do that")


One can interate with range() function. Range always starts with 0 and ends with the value-1 given.

>>> for i in range(4):
...     print(i)
...
0
1
2
3       # value -1, but prints 9 values altogether.

>>> for i in range(-8):
...     print(i)
...
>>>

>>> for i in range(6,10):
...     print(i)
...
6
7
8
9
>>>

Read: Control flow. You can also use else, break,


https://docs.python.org/3/tutorial/controlflow.html






##############################################

  F U N C T I O N S   A N D    M E T H O D S

##############################################

Define function by the def keyword

def function_name():

    global variable_name_defined_out_of_this_function



Note that you can give a default value to the passing variable and you can pass different variable at runtime.
However, NOTE that a non default argument cannot follow a default argument.

def say(message, times=1): # definition is Okay
# def say(times=1, message) ## Not valid.
    print(times * message)

>>> terminal_print.say("Hello")
Hello
>>>
>>> terminal_print.say("Hello",3)
HelloHelloHello
>>>



#########################

     M O D U L E S

#########################











































##############################################

      A  L  G  O  R  I  T  H  M  S

##############################################

Search Algorithms

Sorting Algorithms

Computational Algorithms

Collection Algorithms

''''''''''''''''''''
ek s
Algorithm Performance

Notation        Description             Example
O(1)            Constant time







##############################################

       D A T A    S T R U C T U R E S

##############################################


Arrays

Linked Lists

Stacks and Queues

Browser back button, where the visited web pages are stored in a stack (LAST IN FIRST OUT)
Message processing queues. where a message that entered the queue first should be processed first.

Trees
Hash Tables


Lists:

list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].


Sorting Data

Bubble Sort




list=[7, 4, 4, 3, 2, 9, 1, 0]

for i in range(len(list)):
    if list[n] > list[n+1]:
        temp = list[n]
        list[n] = list[n+1]
        list[n+1] = temp



Sets





































































































.
