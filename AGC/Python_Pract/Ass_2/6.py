#Write a python program to check if a string is a Palindrome or Not.

s=str(input('\nEnter a string\n'));

if(s==s[::-1]):
   print("The string is a palindrome")
else:
   print("The string isn't a palindrome")