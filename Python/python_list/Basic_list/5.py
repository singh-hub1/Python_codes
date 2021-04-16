# Python program to demonstrate working# of
# Set in Python
# creating two sets
My_Set1 = set()
My_Set2 = set()
# Adding elements to My_Set1
for i in range(1, 6):
   My_Set1.add(i)
# Adding elements to My_Set2
for i in range(3, 8):
   My_Set2.add(i)
print("My_Set1 = ", My_Set1)
print("My_Set2 = ", My_Set2)
print("\n")
# Union of My_Set1 and My_Set2
My_Set3 = My_Set1 | My_Set2# My_Set1.union(My_Set2)
print("Union of My_Set1&My_Set2: My_Set3 = ", My_Set3)
# Intersection of My_Set1 and My_Set2
My_Set4 = My_Set1&My_Set2# My_Set1.intersection(My_Set2)
print("Intersection of My_Set1&My_Set2: My_Set4 = ", My_Set4)
print("\n")
# Checking relation between My_Set3 and My_Set4
if My_Set3>My_Set4: # My_Set3.issuperset(My_Set4)
   print("My_Set3 is superset of My_Set4")
elif My_Set3<My_Set4: # My_Set3.issubset(My_Set4)
   print("My_Set3 is subset of My_Set4")
else : # My_Set3 == My_Set4
   print("My_Set3 is same as My_Set4")
# displaying relation between My_Set4 and My_Set3
if My_Set4<My_Set3: # My_Set4.issubset(My_Set3)
   print("My_Set4 is subset of My_Set3")
   print("\n")
# difference between My_Set3 and My_Set4
My_Set5 = My_Set3 - My_Set4
print("Elements in My_Set3 and not in My_Set4: My_Set5 = ", My_Set5)
print("\n")
# check if My_Set4 and My_Set5 are disjoint sets
if My_Set4.isdisjoint(My_Set5):
   print("My_Set4 and My_Set5 have nothing in common\n")
# Removing all the values of My_Set5
My_Set5.clear()
print("After applying clear on sets My_Set5: ")
print("My_Set5 = ", My_Set5)