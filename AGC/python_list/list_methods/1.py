"""
Sr. No	    Methods with Description

1	        list.append(obj) Appends object obj to list
2	        list.count(obj) Returns count of how many times obj occurs in list
3	        list.extend(seq) Appends the contents of seq to list
4	        list.index(obj) Returns the lowest index in list that obj appears
5	        list.insert(index, obj) Inserts object obj into list at offset index
6	        list.pop(obj=list[-1]) Removes and returns last object or obj from list
7	        list.remove(obj) Removes object obj from list
8	        list.reverse() Reverses objects of list in place
9       	list.sort([func]) Sorts objects of list, use compare func if given

"""
#=======================================================================================================================
# append():append at the last
aList = [123, 'xyz', 'abc', 'fgh'];

aList.append( 2009 );

print ("Updated List : ", aList);#Updated List :  [123, 'xyz', 'abc', 'fgh', 2009]

#=======================================================================================================================

#count():This method returns count of how many times obj occurs in list.

aList = [123, 'xyz', 'zara', 'abc', 123];

print ("Count for 123: ", aList.count(123));#Count for 123:  2
print("Count for zara: ", aList.count('zara'));#Count for zara:  1

#=======================================================================================================================

#extend():This method does not return any value but add the content to existing list.

aList = [123, 'xyz', 'zara', 'abc', 123];

bList = [2009, 'manni'];

aList.extend(bList)

print ("Extended List: ", aList); #Extended List:  [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']

#=======================================================================================================================

# index():This method returns index of the found object otherwise raise an exception indicating that value does not find.

aList = [123, 'xyz', 'zara', 'abc'];

print ("Index for xyz: ", aList.index( 'xyz' ));#Index for xyz:  1

print ("Index for zara: ", aList.index( 'zara' ));#Index for zara:  2

#=======================================================================================================================

#insert():This method does not return any value but it inserts the given element at the given index.

aList = [123, 'xyz', 'zara', 'abc']

aList.insert( 3, 2009)

print ("Final List :" , aList);#Final List : [123, 'xyz', 'zara', 2009, 'abc']

#=======================================================================================================================

#pop():This method returns the removed object from the list.

aList = [123, 'xyz', 'zara', 'abc'];

print ("A List: ", aList.pop());#A List:  abc

print ("B List: ", aList.pop(2));#B List:  zara

#=======================================================================================================================

#remove():This method does not return any value but removes the given object from the list.

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.remove('xyz');

print ("List: ", aList);#List:  [123, 'zara', 'abc', 'xyz']

aList.remove('abc');

print ("List: ", aList);#List:  [123, 'zara', 'xyz']

#=======================================================================================================================

#reverse():This method does not return any value but reverse the given object from the list.

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.reverse();

print ("List : ", aList);#List :  ['xyz', 'abc', 'zara', 'xyz', 123]

#=======================================================================================================================

#sort():sort the list

alist=[9,4,6,1,4,8]
alist.sort();
print("sorted list are:",alist);#sorted list are: [1, 4, 4, 6, 8, 9]

#=======================================================================================================================