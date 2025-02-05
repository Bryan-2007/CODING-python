'''
#To open a file:
x=open('file.txt','w')


#Opening file with "with clause" [It is statement, so leave indentation]:
with open('file.txt','a+') as y:

    
#To close a file:
x.close()


#read only mode:
x=open('file.txt','r')


#binary read mode:
x=open('file.txt','rb')


#read and write mode[use <+r> or <r+>]:
x=open('file.txt','r+')


#write only mode:
x=open('file.txt','w')


#Read, write and binary mode[use <+wb> or <wb+>]:
x=open('file.txt','wb+')


#append mode [ to add text to existing text in a file]:
x=open('file.txt','a')


#append and read mode [to append and read text from a file][we can use <a+> or <+a>]:
x=open('file.txt','a+')


### #To write in a file using write():
x=open('note.txt','r+')
x.write('What are u doing? (-_^)\n Halamithi habibo!')
x.close()

    #write() [with clause]:
with open('file.txt','w') as x:
    x.write('Hi  And!')


#To write in a file using writelines():
x=open('file.txt','w')
x.writelines(['Hi Femila!\n','How are you? (^_^)'])
x.close()


### #Using read(n) function [n is number of characters] :
x=open('file.txt','r')
print(x.read(50))
x.close()

    #Using read() in [with clause]:
with open('file.txt','r') as y:
    print(y.read())
    y.close()


#Using readline(n) function [n is number of characters][only reads upto the \n character] :
x=open('file.txt','r')
print(x.readline(50))
x.close()


##Using readlines(n) function [n is number of characters][returns as a list of strings] :
x=open('file.txt','r')
print(x.readlines(50))
x.close()


#To append some text to a file containing text:
x=open('file.txt','a')
x.writelines('ria!')
x.close()


#write text in write, read and binary mode:
x=open('file.txt','wb+')
x.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
x.close()

'''
#Using tell() function[ tells the byte position of the object ][ no argument should be passed ]:
x=open('note.txt','r')
x.tell()
x.close()
'''

#Using seek() function[ change the position of a file object ],[ the default second argument value is 0 ]:
x=open('note.txt','r')
x.seek(10)
x.close()


#Write a python program to read a text file, line by line and display each word separated by #.
file=open('sample1.txt','r')
x=file.readlines()
for i in range(len(x)):
    y=x[i].split()
    print('#'.join(y))
file.close()


#To create binary file and search for a given roll number and display the name and if not found then display an appropriate message:
import pickle
myfile=open('sample2.dat','wb+')
a={}
found=False
for i in range(5):
    roll=int(input('Enter the roll number: '))
    name=input('Enter the name: ')
    a['roll']=roll
    a['name']=name
    pickle.dump(a,myfile)
myfile.seek(0)
c=int(input('Enter the roll number to search: '))
try:
    while True:
        b=pickle.load(myfile)
        if b['roll']==c:
            print(b)
            found=True
except EOFError:
    if found:
        myfile.close()
    else:
        print('Student details not found!')
    myfile.close()


#To read a csv file:
import csv
f=open('new.csv','r')
row=csv.reader(f)
for i in row:
    print(i)


#To write in csv file[ writerow() ]:
import csv
f=open('new.csv','w')
w=csv.writer(f)
w.writerow(['hi','hello','bye'])
f.close()


#Using newline statement in writing in csv file:
import csv
f=open('new.csv','w',newline='')
w=csv.writer(f)
w.writerows(['hi','hello','bye'])
f.close()


##2 PROGRAMS |
#To write in csv file[ Writerows() ]:

import csv
x=[['NAME','AGE','CLASS'],['Bryan','15','XI'],['Surya','16','XI'],['Akhilan','16','XI']]
f=open('new.csv','w',newline='')
w=csv.writer(f)
w.writerows(x)
f.close()

# [ OR ]

import csv
f=open('new.csv','w')
w=csv.writer(f)
w.writerows(['hi','hello','bye'])
f.close()


#Adding delimeter:
import csv
f=open('new.csv','r')
row=csv.reader(f)
for i in row:
    print(i)


#STACK 1:

stack=[]
a=input('Enter element to insert:')
stack.append(a)
print(a)
while True:
    x=input('Do you need to enter more elements?(y/n):')
    if x=='y' or x=='Y':
        a=input('Enter element to insert:')
        stack.append(a)
    elif x=='n' or x=='N':
        break


#STACK 2:

stack=[]
print('Select the operation to perform(1/2/3/4):\n1.Add element\n2.Delete element\n3.Show elements\n4.Quit')
while True:
    x=int(input('Enter option:'))
    if x==1:
        y=input('Enter element to insert:')
        stack.append(y)
    elif x==2:
        stack.pop()
    elif x==3:
        print(stack)
    elif x==4:
        print('Quiting...!')
        quit()


#Program to reverse a string using stack(1):

x=input('Enter the string:')
a=[]
for i in x:
    a.append(i)
b=[]
for i in range(-1,-(len(a))-1,-1):
    b.append(a[i])
print('The reversed string is: ')
for i in b:
    print(i,end='')


#Program to reverse a string using stack(2):

x=input('Enter the string:')
a=[]
for i in x:
    a.append(i)
c=[]
for j in range(len(a)):
    b=a.pop()
    c+=b
for k in c:
    print(k,end='')
'''

#
