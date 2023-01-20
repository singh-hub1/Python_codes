"""
Write a Python program to create a dictionary of keys x, y, and z where each key has as
value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key
from the dictionary.
"""
d = dict(x=list(range(11, 21)), y=list(range(21, 31)), z=list(range(31, 41)))
print(d);
print(d["x"][4])
print(d["y"][4])
print(d["z"][4])


