"""
Write a program which accepts 6 integer values and prints “DUPLICATES” if any of the
values entered are duplicates otherwise it prints “ALL UNIQUE”.
 Example: Let 5 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be printed.
"""


n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
flag=0
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if(a[i] == a[j]):
            flag=1;
            break;

if flag == 1:
    print('DUPLICATES');
else:
    print('ALL UNIQUE')