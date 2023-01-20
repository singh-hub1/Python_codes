"""
Write a Sequential search function which searches an item in a sorted list. The function
should return the index of element to be searched in the list.
"""
def linear_Search(list1, n, key):

    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1

n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)

x=int(input('\nEnter to key value to be search\n'));
print('The index of ', x ,'is',linear_Search(a,n,x))