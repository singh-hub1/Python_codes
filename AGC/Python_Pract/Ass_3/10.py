#Write a Python program to find the repeated items of a tuple.

tup=(1,3,4,32,1,1,1,31,32,12,21,2,3)
"""a=int(input('Enter a value\n'));
count=0;
for i in tup:
    if i==a:
        count=count+1;
print(count);

"""
i=0
for e in tup:
    if tup.index(e)==i:
        print(e,'---',tup.count(e));
    i+=1