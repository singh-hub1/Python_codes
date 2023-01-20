"""
Write a program which finds sum of digits of a number.
Example n=130 then output is 4 (1+3+0)
"""
n=int(input("\nEnter a number:\n"))
total=0
while(n>0):
    digit=n%10
    total=total+digit
    n=n//10
print("The total sum of digits is:",total)