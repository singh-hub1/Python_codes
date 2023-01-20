#Write a Python program to calculate the Length of a String without using a Library Function.

s=str(input('\nEnter a string\n'));
print(s)
y=0
for i in s:
   y=y+1
print("The length of the string "+ s +" is ")
print(y)