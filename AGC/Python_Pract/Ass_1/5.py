#Write a program which prints Fibonacci series of a number

"""def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


n=int(input('\nEnter how many terms u want\n'))
print(Fibonacci(n));
"""

n=int(input('\nEnter how many terms u want\n'))
x, y = 0, 1
print(x)
while y < n:
    print(y)
    x, y = y, x + y



