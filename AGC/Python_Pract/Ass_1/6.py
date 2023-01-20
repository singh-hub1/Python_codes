"""
Write a program which accept an integer value ‘n’ and display all prime numbers till ‘n’.
"""
n = int(input("Enter the value of range: "))

for num in range(2, n):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
