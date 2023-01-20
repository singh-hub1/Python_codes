"""
Write a Python program to filter a list of integers using Lambda
"""
n=int(input('\nEnter how many nos u want\n'))
a=[];
for i in range(0,n):
    elem=int(input('Enter the element:='))
    a.append(elem);
print("Original list of integers:")
print(a)
print("\nEven numbers :\n")
even_nums = list(filter(lambda x: x%2 == 0,a))
print(even_nums)
print("\nOdd numbers :\n")
odd_nums = list(filter(lambda x: x%2 != 0,a))
print(odd_nums)
