#Sets=->A collection is unoredered and unindexed
s={"vishal","arya",'c++','arti'};

print(s);#'c++', 'arya', 'arti', 'vishal'}

print(len(s));#4

s.add("java")

print(s);#{'c++', 'arti', 'java', 'arya', 'vishal'}

s.remove("c++")

print(s);#{'arya', 'vishal', 'java', 'arti'}

s.sort()#ERROR!
print(s);#AttributeError: 'set' object has no attribute 'sort'