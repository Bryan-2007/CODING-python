"""
To find the type of a variable:
===============================
a=10
print (type(a))
===============================
name = input("Enter your name:")
print("Your name is" +  name)
===============================
Many values to multiple Variables:
==========
x,y,z = "Red", "Orange","Green"
print (x)
print (y)
print (z)
==============================
Unpacking a list:
================
x,y,z=["red","orange","green"]
print (x,y,z)
==============================
x=5
y="Five"
print (y,x)
==============================
Global Variable:
================
x=5
def ffun():
    print (x)
ffun()
===============================
Local and Global variable:
local variable can be accessed inside the function
and global can be accessed throughout the program
==========================
x= "Andria"
def myfun():
    x="Bryan"
    print (x)

myfun()
print (x)
===================================================
global keyword inside function.
throughout the program it displays the value assigned inside the function
=========================================================================
x="global"
def myfun():
    global x
    x="change"
    print (x)
myfun()
print(x)
print(type(x))
======================================================================
Type conversion
===============
a=1.5
b=int(a)
print(type(b))
=================
Generating random number within the range:
==========================================
import random
print(random.randrange(1, 67))
==================================
Casting- converting a data type into another datatype:
=====================================================
a=int(1.4)
b=float(2)
print(a)
print(b)
======================
Python strings with single/multiple lines:
===============
print("Femila")
a= '''Python stringsPython stringsPython strings
     Python stringsPython stringsPython strings
     Python stringsPython stringsPython strings'''
print(a)
=================================================
Slicing Strings:
================
Starts with index 0 and the end position will not be included:
==============================================================
x="femila"
print(x[0:3])
=============
x="femila"
print(x[:3])
=============
Starts with index 0 and the end position will be included:
==========================================================
x="femila"
print(x[0:])
============
Negative slicing:
It starts from the back and not include -4th position but displays -3 to -2:
================
x="femila"
print(x[-4:-2])
==================
Changing to upper case:
=======================    
a="Femila"
print(a.upper())
======================
changing to lower case:
=======================
b="BRYAN"
print(b.lower())
=========================
Removes unwanted spaces at the begining and at the end:
======================================================
b="   Bryan   "
print(b.strip())
=======================================================
This method replaces a string with another string:
==================================================
b="   Bryan   "
print(b.replace("Bryan","Alice"))
=================================
Split()- seperates the words when there is a seperator:
=======================================================
a="femi.la"
print(a.split("."))
====================
Concatenates two strings
========================
a="Andria"
b="bryan"
c= a+b
print (c)
=======================
Format Strings:
===============
format() method adds a string and number:
=========================================
age = 36
txt = "My name is John, I am {}"

print(txt.format(age))
=================================
To create a login:
==================
users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}  
  
def login():  
    username = input("Enter your username: ")  
    password = input("Enter your password: ")  
  
    if username in users and users[username] == password:  
        print("Login successful!")  
    else:  
        print("Invalid username or password. Please try again.")  
  
login()
============================================================================
"""


    



