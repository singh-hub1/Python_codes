"""
Write a generator function that reverses a given string
"""

def reverse_string(str):
    str1 = " ";
    for i in str:
        str1 = i + str1 #here it shift the index by one towars its right
    return str1

s=str(input('\nEnter a string\n'))
print('The reverse string is:= ',reverse_string(s))