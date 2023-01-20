#Write a Python program to add an item in a tuple.
T1=(10,50,20,9,40,25,60,30,1,56)
L1=list(T1)

L1.append(100)
T1=tuple(L1)
print(T1);
