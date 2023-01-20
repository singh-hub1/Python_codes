"""
Write a python program to remove and return an arbitrary set element.Raise Key Error if
the set is empty
"""
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s);
print(s.remove(5))
print(s)
s.clear();
print(s.remove(0))
