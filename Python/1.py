#list:->It is collection or ordered or changeable or duplicate data are allowed
list=["vishal","singh",'arya'];
print(list);#['vishal', 'singh', 'arya']

print(list[0]);

print(list[1]);

print(list[2]);

print(len(list));#3

(list.append("jasu"));#It will append t the very last in the list

print(list);#['vishal', 'singh', 'arya', 'jasu']

(list.insert(1,"swati"))

print(list);#['vishal', 'swati', 'singh', 'arya', 'jasu']

(list.remove("vishal"));

print(list);#['swati', 'singh', 'arya', 'jasu']

(list.sort(reverse=True));

print(list);#['swati', 'singh', 'jasu', 'arya']

(list.sort)

print(list);#['swati', 'singh', 'jasu', 'arya']
