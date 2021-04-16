#check
"""a=int(input("enter any number\n"))
if a %2==0:
    print(a,"is even number")
else:
    print(a,"number is odd\n")


a = int(input("enter first number\n"))
b=int(input("enter second number\n"))
c=int(input("enter third number\n"))

if a > b and   a > c:
    print(a,"greater")
elif b>a and b>c:
    print(a, "greater")
else:
    print(c, "greater")

sum=0
count=0
while(count<=4):
    sum=sum+count
    count+=1
print(sum)
    #count++ --not working in python
"""
# Sum of natural numbers up to num

"""number = int(input("Please Enter any Number: "))
total = 0

for value in range(1, number + 1):
    total = total + value

print(total)"""

num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    while (num > 0):
        sum += num
        num -= 1
    print(sum)