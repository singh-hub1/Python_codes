"""
Write a Python function that takes a number as a parameter and check the number is
prime or not.
"""

def check_prime(num):
 if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

 else:
    print(num, "is not a prime number")

num = int(input("Enter a number: "))
check_prime(num)