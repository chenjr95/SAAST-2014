

def spread():
    print 'Open jar'
    print 'Spread on bread with knife'

def <name>():
    <statement>
    <statement>
    <statement>

## white space matters (indentation means it belongs to the funtion)

## end infinite loops with ctrl+c

## function name cannot begin with a number.

##function names can only have letters, numbers and underscores

##function names should be concise and tell what it does


int(6.0/4.0) rounds down
6.0//4.0 rounds down

bool(1) --> True
bool(0) --> False

Exponents
3**2 = 9

Combining Strings
'hello' + 'bye'
'hello bye'

'hello' * 5
'hellohellohellohellohello'

print 'my value is: ' + 5
DOES NOT WORK

int('5')
5

int('5') +5
10

'5' + 5
DOES NOT WORK

print 'my value is: ' + str(5)
my value is: 5

VARIABLE DECLARATION
<name> = ____
x = 5
y = 'hi'

y+ str(x)
'hi5'

For Loop Syntax
for <name> in range (<lo>,<hi>):
    <functions>
range goes from lo number to (n-1) of hi number

for <name> in range (<lo_range>, <hi_range>, <step_number>)

for i in range (0,10,-1)
DOES NOT WORK

for i in range (10,0,-1)
WORKS

Comma after print '____', makes text stay on line

FUNCTION PARAMETERS/ARGUMENTS

def <name>(<name>,<name>,<name>,...):
"name"s in parentheses are local variables taken with the function when called


    def first_line(index):
        print ' ' * (2 + 5 * ((NUM_PEOPLE -1) - index)) + \
              'O  ' +     \
              '*'*6  +     \
              ' '*(5*index) +    \
              '*'

    def people():
        for i in range(0,NUM_PEOPLE):
            first_line(i)

'i' is put into the first_line function as index
    index=i

RETURN PROCESS
def inc(x):
    return x + 1

print inc(5)

^^Returns one more than x, thus prints 6

Returns can only reside inside a function
return<expression>
Return also exits a function prematurely

IMPORTING LIBRARIES
from math import*
sqrt(<number>)
WORKS
from math import sqrt
sqrt(<number>)
WORKS ALSO

Look through directory
dir()

"FOR" LOOPS WORK WITH ANY SEQUENCES
def print_lineified(s):
    for ch in s:
        print ch


print_lineified('hello')
WORKS


DRAWINGS
from drawingpanel import*
panel=DrawingPanel(500,500)
panel.set_background('wheat')
for i in range(0,15):
    panel.sleep(10)
    panel.canvas.create_rectangle(0, 0, 500, 500,
        outline = 'wheat', fill = 'wheat')
    panel.canvas.create_oval(
        40+i*25, 60+i*25, 210+i*25, 210+i*25, outline = 'brown', fill = 'hotpink')


IF STATEMENTS
if ___:
    <do this>
else:
    <do this>

can use equalities:
    x<n
    x<=n
    x>n
    x>=n
    x==n
    x!=n

for more than two if statement sets
if ___:
    print slkajfdla;sk
elif (='else if') ___:
    print ;alksjfd
else: print ;lakjdsf;a

RECURSION
def print_stars(n):
    if we are in the base case:
        do the base case
    else we are in the recursive case
        do the recursive case

USER INPUT
x1 = raw_input("Enter a number: ")
Enter a number: 5
x1=5
this produces a string!
To make a number that is input:
x1=int(raw_input("Enter a number: "))

input does eval(raw_input('<text> ')
raw_input simply returns the input as a string
                

BOOLEAN EXPRESSIONS
b=bool(<number>)
b=True if not 0
else, b = False
b = bool(raw_input('Are you a boy? ')

simple boolean expressions:
         >=
         <=
         >
         <
         0<= x <= 10

>>> def get_response(x):
	if x==0:
		return raw_input('Response? ')
	else:
		return None	
>>> resp=get_response(0)
Response? 'Hello'
>>> if resp.startswith('H'):
	print 'H'
>>> resp
"'Hello'"
>>> resp= get_response(5)
>>> if resp.startswith('H'):
	print 'H!'

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    if resp.startswith('H'):
AttributeError: 'NoneType' object has no attribute 'startswith'

PROGRAM VERIFICATION/ DEBUGGING
         
def foo(x, y):
    if x>= 0:
        return -1
    else:
        #POINT A Is x<0? Always; y < 0? Sometimes
        while x<0:
            #POINT B Is x<0? Always; y < 0? Sometimes
            if y>0:
                x=x+y
            elif y<0:
                x=x-y
                #POINT C Is x<0? Sometimes, y < 0? Always
                else:
                x=x+1
        #POINT D Is x<0? Never, y < 0? Sometimes
        return x+y

"""
Program assertion: condition on the state of a program at a particular point.
Invariants: cornerstone of program reasoning.
Program verification: the study of program assertions
Pre-conditions
"""

FILE STUFF
f = open('test.txt', 'r')
    'r' = read
    'w' = writing
    'a' = appending
import os
os.getcwd()
    getcwd= get current directory

f = open('scratch/t.cpp', 'r')
f = open('../peter/address.txt', 'r')

help(open('sample1.txt','r'))
         shows a list of possible commands

f.read()
f.close()
         you must recall close function after going through it

>>> f = open('sample1.txt','r')
>>> sum=0
>>> for line in f:
	for tok in line.split(','):
		sum=sum+int(tok)

>>> sum
351

you can pass in a parameter line.split()
         () = ' ' or any whitespace by itself

f = open('pg98.txt', 'r')
         count = 0
         max_cols = (0,0)
         for line in f:
             count = count +1
             if len(line) > max_cols[0]:
                 max_cols = (len(line), count)
print 'This book is {} lines long'.format(count)
print 'The longest line is {} colmuns at line {}'.format(max_cols[0], max_cols[1])

comma-separated values -- .csv
         1,2,3,4,5,6,7,8...

f=open('pg98.txt','r')

def base_ord(ch):
         return ord(ch) - ord('a')

def is_letter(ch):
         return 0<=base_ord(ch)<26
counts = []
for i in range(0,26):
         counts.append(0)

for line in f:
         tokens = line.split()
         for tok in tokens:
         for ch in tok:
             ch=ch.lower()
             if is_letter(ch):
                 index = case_ord(ch)
                 counts[index] = counts[index] + 1
index = 0
for count in counts:
         print '{}: {}'.format(chr(index+ord('a')),count)
         index=index+1
    
print count


f = open('movies.list','r')
         f.next()
         f.next()
         f.next()
         for i in range(0,1000)
             x=f.next()
         f.next()
         line=f.next()
         line
         tokens=line.split()
         tokens
         tokens=line.split('\t')
         tokens
         tokens[0]
         tokens[len(tokens)-1]
         '1 contre 100' in tokens[0]
         '100' in tokens[0]
         for line in f:
             tokens = line.split()
             if tokens[len(tokens)-1] == '2000':
                 count+= 1



def find_earliest():
         f=open('movies.list','r')
         year = 2020
         for line in f:
             tokens = line.split()
             line_year = tokens[len(tokens)-1]
             if line_year.isdigit() and int(line_year) < year:
                 year=line_year
        return year

def find_first(year):
         f = open('movies.list','r')
         for line in f:
             tokens = line.split()
             if tokens[len(tokens)-1] == year:
                 return token[0]
         return None

year = find_first(year)


def find_movies(actress):
         f=open('actresses.list','r')
         for line in f:
             line.strip()
             tokens = line.split('\t')
             if tokens[0] == actress:
                 result = [ tokens[len(tokens)-1] ]
                 line = f.next().strip
                 while line != '':
                     tokens = line.split('\t')
                     result.append(tokens[len(tokens)-1])
                     line = f.next().strip()
                 return result
         return None

result = find_movies('Bullock, Sandra')
print len(result)

# Mapping operation
for i in range(0, len(results)):
         results[i] = results[i].lower()

# 
results=[title.lower() for title in results]

         
# Reduce operation
for i in range(0, len(results)):
         print results[i]
-------------------------------------------------------
LISTS/ARRAYS

x= [1,2,3,4,5,6,7,8,9,10]
[e*2 for e in x]
[2,4,6,8,10,12,14,16,18,20]

[x*y for x in x1 for y in x2]

zip(x1,x2)
[(0,10).....(9,19)]

[x * y for (x,y) in zip(x1,x2)]
[0,11,24,39,56,75,96,119,144,171]

[x*y*z for x,y,z for x,y,z in zip(range(0,10),range(10,20),range(20,30))]
-------------------------------------------------------

f = open('pg98.txt')

##unigrams={k:0 for k in [chr(x) for x in range(ord('a'), ord('z')+1)]}
bigram = { }

for line in f:
    for tok in line.split():
        tok = tok.lower().strip()
        tok = [ch for ch in tok if tok.isalpha()]
####        print '-'.join(tok)
##puts hyphen between letters
        for ch in tok:
            unigrams[ch] = unigrams[ch]+1
print unigrams


zip(x[0:len(x):2], x[1:len(x):2])





----------------
DICTIONARY

x = {'a' : 5, 'b': 7, 'c' : 10}
>>> x['a']
         5
x={k : 0 for k in range(0,26)}

x={k:0 for k in range(ord('a'), ord('z')+1)}
>>> x
         {97:0, 98:0... 121:0, 122:0}

x={k:0 for k in [chr(x) for x in range(ord('a'), ord('z')+1)]|}


--------------------


bigrams = {}

for line in f:
         for tok in line.split():
         tok - tok.lower().strip()
         tok = [ch for ch in tok if tok.isalpha()]
         pairs = zip(tok[0:len(tok):2], tok [1:len(tok):2])
         for l,r in pairs:
             b = l_r
             if b not in bigrams:
                 bigrams[b]=0
             bigrams[b] = bigrams [b] +1

print bigrams




Object = state + behavior
         panel=DrawingPanel(600,800)
         panel.canvas
         panel.canvas.draw_rectangle(...)
