'''
#TURTLE MODULE:
#Drawing equilateral triangle[ Turtle ]:
import turtle as a
import time
a.shape('turtle')
a.speed(1)
a.forward(200)
a.left(120)
a.forward(200)
a.left(120)
a.forward(200)

'''

#Drawing parallelogram pattern:
def function_():
    import turtle as t
    import time
    t.pensize(2)
    t.pencolor('black')
    t.fillcolor('green')
    t.shape('turtle')
    t.begin_fill()
    t.speed(10)
    t.fd(200)
    t.lt(60)
    t.fd(100)
    t.left(120)
    t.fd(200)
    t.left(60)
    t.fd(100)
    t.right(170)
    t.end_fill()

for i in range(36):
    function_()


'''

#Printing letters using python turtle:
import turtle as s
import time
s.speed(10)
s.shape('turtle')
s.pencolor('black')
style =('Courier', 90, 'normal')
s.write('$ WISTAN $', font= style, align='center')
s.fd(400)
s.lt(90)
s.fd(150)
s.lt(90)
s.fd(800)
s.lt(90)
s.fd(150)
s.lt(90)
s.fd(400)
s.penup()
s.rt(90)
s.fd(20)
s.pendown()
s.lt(90)
s.fd(420)
s.lt(90)
s.fd(190)
s.lt(90)
s.fd(840)
s.lt(90)
s.fd(190)
s.lt(90)
s.fd(420)

#Move function:
import turtle as t
t.write("GeeksForGeeks", move=True)

#Drawing circle:
import turtle as t
t.circle(100)

#using goto function:
import turtle as t
import time
t.speed(5)
t.pencolor('red')
t.goto(100,0)
t.goto(100,200)
t.goto(-100,200)
t.goto(-100,0)
t.goto(0,0)

#Corona drawing:
from turtle import*
color('yellow')
bgcolor('red')
speed(1000)
hideturtle()
b=0
while b<200:
    right(b)
    forward(b*3)
    b=b+1
'''
