"""
Write a Python program to get a single string from two given strings, separated by a space and
swap the first two characters of each string.
Sample String: 'ppk', 'abc’
Expected Result: 'abkppc
"""
s=str(input('\nEnter first string\n'));
t=str(input('\nEnter second string\n'));
a = t[:2] + s[-1:]

b=s[0:2] +t[-1:]
print(a+b)





