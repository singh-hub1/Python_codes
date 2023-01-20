"""
Write a Python program to count the number of characters (character frequency) in a string.
Sample String: google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1
"""
s=str(input('\nEnter a string\n'));

dict = {}
for n in s:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1

print(dict);