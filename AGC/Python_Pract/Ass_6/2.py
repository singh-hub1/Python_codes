"""
Write a Python function to multiply all the numbers in a list.
Sample-List :(8,2,3,-1,7)
Expected Output : -336
"""
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

n=int(input('Enter how many numbers u want\n'));
a=[];
for i in range(0,n):
    elem=int(input('Enter the element:='))
    a.append(elem)
print(a);

print('Output is :=',multiply(a))