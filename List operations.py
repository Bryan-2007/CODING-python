def push(s,x):
    s.append(x)
def pop(s):
    print('the deleted element is: ',s.pop())
s=[]
while True:
    print('1:push\n2:pop\n3:show\n4:exit')
    a = int(input('Enter your option: '))
    if a == 1:
        b = input('Enter the element to insert: ')
        push(s,b)
    elif a == 2:
        pop(s)
    elif a == 3:
        print(s)
    elif a == 4:
        print('Exiting...')
        exit()