#Write a Python program to create a dictionary from a string.

st=str(input('Enter a string\n'));
print(st);
count={};
for x in st:
    if x in count.keys():
        count[x]+=1;
    else:
        count[x]=1;
print(count);