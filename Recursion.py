'''
# factorial

num = int(input("Enter no to find factorial: "))

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print("Factorial: ", fact(num))

'''
# Fibonacci series

num = int(input("Enter value of n: "))

def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x-1) + fib(x-2)

print("Fibonacci series:")
for i in range(num):
    print(fib(i))
