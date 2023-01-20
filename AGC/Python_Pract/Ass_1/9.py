"""
Write a program to reverse a given number.
"""
n=int(input("Enter number: "))
reverse=0
while(n>0):
    dig=n%10
    reverse=reverse*10+dig
    n=n//10
print("Reverse of the number:",reverse)