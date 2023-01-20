#list is mutable and denotes with []
#   0     1    2
l=["ccc",100,"pp"]
print(l) #['ccc', 100, 'pp']
l[0]="vishal"
print(l) #['vishal', 100, 'pp']

print(l[0:3]) #['vishal', 100, 'pp']

#------------------------------------------------------
#tuple is not mutable and denotes with ()
t=(1,2,3)
print(t)#(1, 2, 3)
print(t[0:3])#(1, 2, 3)

k=1 in t
print(k) #True

k=1 not in t
print(k)#False

"""
t[0]="vishal" error hoga bcoz tuple is not mutable
print(t)
"""
list(t)#here tuple is converted into list i.e typecasting
s={1,2,3,4}

print(s)#{1, 2, 3, 4}
#s=set,no indexing in the set

#----------------------------------------------------------------

#dict=({})--another method of displaying of dictionary
dict={'roll':'10','name':"vishal","addr":"pune"}

print(dict)#{'roll': '10', 'name': 'vishal', 'addr': 'pune'}




