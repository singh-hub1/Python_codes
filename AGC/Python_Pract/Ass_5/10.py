"""Write a Python program to create a dictionary from two lists without losing duplicate
values."""
a=['vishal','singh','sybca',20];
b=['first_name','last_name','class','age'];
d=dict(zip(b,a));
#first it convert to tuples and then convert to dictionary
print(d);