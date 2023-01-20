"""Write a Python program to create a list of tuples with the first element as the number and second
element as the square of the number."""
l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))
a=[(x,x**2)
for x in range(l_range,u_range+1)]
print(a)