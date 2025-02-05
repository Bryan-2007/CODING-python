#printing variables:
print ('Andria is a good girl')

#printing multiple lines:
print (''' Python is a high-level,
interpreted, general-purpose
programming language. Its design
philosophy emphasizes code
readability with the use of
significant indentation. ''')

#value for variable
x=5
y='Sally'
print (x)
print (y)

sing= '''Python is a high-level, interpreted,
general-purpose programming language.'''
print(sing)

king=38
print (king)

#concatenating or adding variable to give variable with values; [for adding space]
x=5
y=10
z= x + y
print (z)

x=32
y=8
print (x+y)

zion= 'blissful' + ' ' + 'paradise'
print (zion)


#printing only particular characters in a string:
x= 'donkey'
print(x[5])
print (x[0])

#Get the characters from one position to another:
W= 'QWERTY'
print(W[1:4])

#getting characters from the start to another position:
U= 'Universal Set'
print(U[:6])

#getting characters from one position to last:
sun= 'Very Bright'
print(sun[3:])

#getting characters in reverse:
birds= 'DOVE123456'
print(birds[-7:-3])

#getting output in uppercase letters:
DJ= 'smaller case'
print(DJ.upper())

#getting output in lowercase letters:
DJ= 'LOWER CASE'
print(DJ.lower())

#removing spaces from the start and end:
hi= ' today is beautiful! '
print(hi.strip())

#replacing a string with another:
Rolex= 'Always gethu!'
print(Rolex.replace('gethu','villain'))

#splitting string into list:
UTURN= 'apple, orange, grapes, mango'
print(UTURN.split(","))

#finding length of string:
S= 'GodIsGreat'
print(len(S))

#checking if a character is present in a string:
sentence= 'Hardwork Never Fails!'
print('work' in sentence)

#printing a statement if a character is present in a string:
line= 'Try Again And Again Until U Succeed'
if 'Succeed' in line:
 print('The statement is true!')

#checking if a character is not present in a string:
sentence= 'Hardwork Never Fails!'
print('work' not in sentence)

#printing a statement if a character is not present in a string:
line= 'Try Again And Again Until U Succeed'
if 'Succeed' not in line:
 print('The statement is false!')

#adding int with str in a sentence using format string:
age= 14
txt= 'Bryan Roger is {} years old.'
print(txt.format(age))

carrots= 5
beetroot=3
beans=25
brinjal= 4
List= 'I have {} carrots, {} beetroots, {} beans, {} brinjals in my home.'
print(List.format(carrots, beetroot, beans, brinjal))

#deciding the position of format string in a sentence:
eggs= 10
biriyani= 5
fried_rice= 3
tomato_sos_packets= 10
list2= 'I want {3} fried rice bowls, {2} eggs, {0} biriyani bowls , {1} tomato sos packets '
print(list2.format(biriyani,tomato_sos_packets,eggs,fried_rice))

#using illegal characters *_inside a string_*:[just insert a backslash before the illegal character]
example1= 'here we use \' U \' inside '
print(example1)
example2= 'It\'s fun with python'
print(example2)
example3= 'BE \"\\ HAPPY'
print(example3)

#to take the variable to the next line:
ex1= 'Taking Python \nto next line'
print(ex1)

#leaving 3 spaces using tab:
myname= 'incredible\tpython'
print(myname)

#deleting one character from before[backspace]:
don= "python kaa\b king"
print(don)

#Octal value:
txt1 = "\110\145\154\154\157"
print(txt1) 

#hex value:
txt2 = "\x48\x65\x6c\x6c\x6f"
print(txt2)

#capitalize-[it turns only the first letter]:
movie1= 'beast thalapathy vijay'
print(movie1.capitalize())

#converting string into lower case:
movie2= 'Beast Thalapathy Vijay'
print(movie2.casefold())

#centering a string:
movie3= 'Beast Thalapathy Vijay'
print(movie3.center(50))

#getting the number of a character in a string: 
movie4= 'Beast Thalapathy Vijay'
print(movie4.count('a'))

#to find the first occurance of the specified value:
value1= 'Peter piper piped a peck of pickled peppers'
print(value1.find('p'))

value2= 'hee hee haa haa'
print(value2.find('b'))

#to find the first occurance of the specified value between limits:
value3= 'hee hee haa haa'
print(value3.find('a',11,14))

#looping through letters in string
for x in "banana":
 print(x)

#assigning different values for a same identifier: [then last value only will be counted]
x=46
x='sallu'
x=800
print (x)

kong= 'godzilla'
kong= 'skull crawler'
kong= 'KING KONG'
print(kong)

# str(string)-[prints variables,numbers,or both] ,int(integer)-prints only numbers ,float-prints numbers (with decimal), with power e]:
a= str (23)
x= str('3dihnf')
y= int(8)
z= float(130)
ab= float(34e3)
print (a)
print (x)
print (y)
print (z)
print (ab)

#converting data types:
don= 22
a= float(don)
x= int(3.8)
y= float(34)
z= complex(1)
print(a)
print(x)
print(y)
print(z)
#getting the data type
x1= 31
y3= 'queen'
Z= 8.3
Br= 1j
v= 5868437570
L= -386859686
O= -35.69e3
ki=35e5
oil=3j+5
print (type(x1))                     
print (type(y3))
print (type(z))
print (type(Br))
print (type(v))
print (type(L))
print (type(O))
print (type(ki))
print (type(oil))

#variable names are case-sensitive-[upper case-capitals, lower case-small letters]
a= 'good'
A= 'GOOD'
A_= 37
print (a)
print (A)
print (A_)

#variable name cannot start with number, cannot contain spaces, it can contain underscores[anywhere], numbers[only in between]
qwerty= 6
QwE_Rt1y= 'forgive'
_light3= '34king'
MyFirstVar= 10
print (qwerty)
print (QwE_Rt1y)
print (_light3)
print (MyFirstVar)

#assigning values to multiple variables in same line:
x, y, z, A= 'Red', 'orBit', '1going', '_knight2'
print (x)
print (y)
print (z)
print (A)

#printing variables in same line after assigning values:
x= 5
y= 10
z= 'hog_rider'
print (x, y, z)

#assigning the same value to multiple variables in same line:
x= y = z ='5Wizard_COC'
print (x)
print (y)
print (z)

x=y=z=50
print(x, y, z)
#Unpacking a Collection of elements-[extracting the values into variables]:
Vegetables= [ "beans", "cucumber", "carrot", "potato", "brinjal"]
a, b, c, d, e = Vegetables
print (a)
print (b)
print (c)
print (d)
print (e)

#Unpacking a Collection of elements[in a same line]:
Fruits= [ "apple", "orange", "grapes"]
a, b, c = Fruits
print (a,b,c)

#Unpacking a list of elements[with single print, down down looping]
Vegetables= [ "beans", "cucumber", "carrot", "potato", "brinjal"]
for king in Vegetables:
    print (king)

#printing multiple variables in a same line using ' + ':
x= 'Python '
y= 'is '
z= 'Awsome'
print (x+y+z)

a= 'HTML '
b= 'is'
c= '10'
print (a+b+c)

#listing elements:
games= ['PUBG', 'Garena free fire', 'COC', 'CR']
print (games)



#


#area of rectangle
l=3
b=4
area= b*l
print(area)

length = 10 
breadth = 20 
area = length * breadth 
print(area)

#area of tiangle
b=3
h=4
area= (1/2 * b* h) 
print("area of triangle is" , area)

#average of my 10th mark
import statistics
print(statistics.mean([94,95,96,97,97]))

#if condition
if 5>2:
 print('true')

#value for false statement
if 1>2:
 print('true')
elif 1<2:
    print('false')


#one line comment
# this line is a comment. it will not be taken or considered by python

#several line comment
'''
these lines
will not be considered
by python
'''
#



 
#giving different outputs with same variable names using def function: [here we cannot use '+' between 2000 and barbarian]:
Barbarian= '100power'
def myfunc():
 Barbarian= 'archer queen'
 print (2000,'Barbarian')
myfunc()
print (Barbarian)

#global variable takes the value of variable even from outside the function:
x= 'fantastic'
def myfunc():
  global x
myfunc()
print("Python is " + x)

#printing the variable inside function from outside using global variable:
x= 'Good'
def myfunc():
    global x
    x= 'excellent'
myfunc()
print (x)

#tuple prints variable values in a list:
List_Of_Programming_Languages= ('Python', 'HTML', 'CSS', 'Java')
print (List_Of_Programming_Languages)

#import a random number:
import random
print (random.randrange(1,10))

#finding range
print(range(-5))

#finding id of a variable:
name= 'vijay'
print(id(name))

result='end'
print(id(result))

