#Python Dictionary(Data Type)
"""d={'name':'vishal','roll':10}
print(d);
print(d['name']);
print(d['roll']);
d['roll']=40;
print(d['roll']);
del d['roll'];
print(d);
d.clear();#delete entire

d={}#empty dictionary
print(d);

x={'name':"vishal",1:[2,4,3]};
print(x);

dict={1:(1,'apple'),2:(2,'orange')}
print(dict);

for i in x:
    print(i);#it will print only key only"""

a={'name':'vishal','addr':'pune','phone':7875487500};
for i in a:
    print(i);

for i in a.values():
    print(i);

for i in a.items():
    print(i);

for i,j in a.items():
    print(i,j);


"""a.pop('name');
print(a);"""

a.popitem()#it will delete last item from the dictionary
print(a);
print(type(a));#it will display type of particular variable
print(len(a));
print(str(a));

"""q=a;#shallow copy
print(q);"""


