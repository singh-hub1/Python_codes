#Write a Python program to perform different set operations.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
#B = {1, 2, 3, 4, 5}

print(A.union(B));#{1, 2, 3, 4, 5, 6, 7, 8}

print(B.union(A));#{1, 2, 3, 4, 5, 6, 7, 8}

print(A.intersection(B));#{4, 5}

print(B.intersection(A));#{4, 5}

print(A - B);#{1, 2, 3}

print(A.difference(B));#{1, 2, 3}

print(B - A);#{8, 6, 7}

print(B.difference(A));#{8, 6, 7}

print(A.isdisjoint(B));#false

print(A.issubset(B));#set A is a subset of set B if all elements of A are also in elements of B

print(A.issuperset(B));#set A is a superset of set B if all elements of the set B are elements of the set A.
