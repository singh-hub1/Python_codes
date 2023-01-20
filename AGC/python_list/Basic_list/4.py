#SET in a Python

s=set({1,2,3,4,5})
print(s);#{1, 2, 3, 4, 5}

s1=set(['a','b',4,7])
print(s1);#{'b', 4, 7, 'a'}

s2={'vishal','singh','arya','arti'}
print(s2);#{'vishal', 'arti', 'singh', 'arya'}

#Accessing values in a set

for a in s2:
    print(a);
"""
singh
arti
vishal
arya
"""

#=======================================================================================================================

#SET OPERATION

a={1,2,3,4,5}
b={3,7,5,9,4}

print("Operation in a set:\n")

print(a|b);#{1, 2, 3, 4, 5, 7, 9}---UNION

print(a&b);#{3, 4, 5}---INTERSECTION

print(a^b);#{1, 2, 7, 9}-----symmetric difference

print(a-b);#{1, 2}

print(b-a);#{9, 7}


print(a.isdisjoint(b))#False

print(a.issubset(b))#False
#a.clear();

#=======================================================================================================================

#write a python program to create a copy.

x={1,2,3,4};
y=x;
y.add('5');
print('numbers',x);#numbers {1, 2, 3, 4, '5'}

print('new_numbers',y);#new_numbers {1, 2, 3, 4, '5'}

#=======================================================================================================================

#write a python program to create a copy with the help of copy().

p={1,2,3,4};
q=p.copy();
q.add('5');
print('numbers',p);#numbers {1, 2, 3, 4}

print('new_numbers',q);#new_numbers {1, 2, 3, 4, '5'}

#=======================================================================================================================

Q=set();
print(type(Q));#<class 'set'>

Z={};
print(type(Z));#<class 'dict'>

#=======================================================================================================================
"""
We can add a single element using the add() method,
 and multiple elements(like tuples,lists,strings)
  using the update() method
"""
my_set = {1, 3}
print(my_set);#{1, 3}

my_set.add(2)
print(my_set);#{1, 2, 3}

my_set.update([2, 3, 4])
print(my_set);#{1, 2, 3, 4}

my_set.update([4, 5], {1, 6, 8})
print(my_set);#{1, 2, 3, 4, 5, 6, 8}

#=======================================================================================================================
"""
discard() function leaves a set unchanged if the element is not present in the set. 
On the other hand, the remove() function will raise an error
 in such a condition (if element is not present in the set).
"""
my_set = {1, 3, 4, 5, 6}
print(my_set);#{1, 3, 4, 5, 6}

my_set.discard(4)
print(my_set);#{1, 3, 5, 6}

my_set.remove(6)
print(my_set);#{1, 3, 5}

my_set.discard(2)
print(my_set);#{1, 3, 5}

#print(my_set.remove(2));#KeyError: 2

#=======================================================================================================================
"""
we can remove and return an item using the pop() method.
We can also remove all the items from a set using the clear() method.
"""
my_set = set("HelloWorld")
print(my_set);#{'r', 'W', 'd', 'H', 'l', 'e', 'o'}

print(my_set.pop());#r

my_set.pop()
print(my_set);#{'d', 'H', 'l', 'e', 'o'}

print(my_set.clear());#None

#=======================================================================================================================

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
#B = {1, 2, 3, 4, 5}

print(A.union(B));#{1, 2, 3, 4, 5, 6, 7, 8}

print(B.union(A));#{1, 2, 3, 4, 5, 6, 7, 8}

print(A.intersection(B));#{4, 5}

print(B.intersection(A));#{4, 5}

print(A - B);#{1, 2, 3}

print(A.difference(B));#{1, 2, 3}

print(B - A);#{8, 6, 7}

print(B.difference(A));#{8, 6, 7}

print(A.isdisjoint(B));#false

print(A.issubset(B));#set A is a subset of set B if all elements of A are also in elements of B

print(A.issuperset(B));#set A is a superset of set B if all elements of the set B are elements of the set A.

#=======================================================================================================================
"""
Symmetric Difference of A and B is a set of elements in A and B but not 
in both (excluding the intersection).
Symmetric difference is performed using ^ operator. 
Same can be accomplished using the method symmetric_difference().
"""
print(A.symmetric_difference(B));#{1, 2, 3, 6, 7, 8}

print(B.symmetric_difference(A));#{1, 2, 3, 6, 7, 8}
#=====================================================================================================================================================================
"""
Method	                                                                      Description
add()	                        |                                   Adds an element to the set
clear()	                        |                                   Removes all elements from the set
copy()	                        |                                   Returns a copy of the set
difference()                   	|                                   Returns the difference of two or more sets as a new set
difference_update()             |	                                Removes all elements of another set from this set
discard()	                    |                                   Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	                |                                   Returns the intersection of two sets as a new set
intersection_update()           |                      	            Updates the set with the intersection of itself and another
isdisjoint()	                |                                   Returns True if two sets have a null intersection
issubset()	                    |                                   Returns True if another set contains this set
issuperset()	                |                                   Returns True if this set contains another set
pop()	                        |                                   Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	                    |                                   Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()          |                                   Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	|                                   Updates a set with the symmetric difference of itself and another
union()	                        |                                   Returns the union of sets in a new set
update()	                    |                                   Updates the set with the union of itself and others
"""

#=====================================================================================================================================================================

#We can test if an item exists in a set or not,
# using the 'in' keyword.

my_set = set("apple");

print('a' in my_set);#True

print('p' not in my_set);#False

#===============================================================

#We can iterate through each item in a set using a for loop.
for letter in set("apple"):
   print(letter);
   """
   p
  a
  e
  l
   """

#===================================================================

#Built-in Functions with Set:
"""
Function	Description
all()	Returns True if all elements of the set are true (or if the set is empty).
any()	Returns True if any element of the set is true. If the set is empty, returns False.
enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
len()	Returns the length (the number of items) in the set.
max()	Returns the largest item in the set.
min()	Returns the smallest item in the set.
sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
sum()	Returns the sum of all elements in the set.
"""
#============================================================

#Python Frozenset
"""
Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned.
 While tuples are immutable lists, frozensets are immutable sets.

Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.

Frozensets can be created using the frozenset() function.

This data type supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable, it does not have methods that add or remove elements.

"""
A = frozenset([1, 2, 3, 4]);
B = frozenset([3, 4, 5, 6]);

print(A.isdisjoint(B));#False

print(A.difference(B));#frozenset({1, 2})
frozenset({1, 2});
