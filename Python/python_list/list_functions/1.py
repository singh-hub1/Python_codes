"""
Sr. No  |	 Function with Description
1	    |    cmp(list1, list2) Compares elements of both lists
2	    |    len(list) Gives the total length of the list.
3	    |    max(list) Returns item from the list with max value
4	    |    min(list) Returns item from the list with min value.
5	    |    list(seq) Converts a tuple into list.
"""
#=======================================================
#cmp()
"""list1, list2 = [123, 'xyz'], [456, 'abc'];

print (cmp(list1, list2));

print (cmp(list2, list1));

list3 = list2 + [786];

print (cmp(list2, list3));

#===================================================================================
#len()
list1, list2 = [123, 'vvv', 'rrr'], [456, 'eee']

print ("First list length : ", len(list1));#First list length :  3

print ("Second list length : ", len(list2));#First list length :  2
"""
#==================================================================================
#max()
list1, list2 = [123, 222,777,457], [456, 700, 200]

print ("Max value element : ", max(list1));#Max value element :  777

print ("Max value element : ", max(list2));#Max value element :  700

#==================================================================================
#min()
list1, list2 = [123, 45], [456, 700, 200]

print ("min value element : ", min(list1));#min value element :  45

print ("min value element : ", min(list2));#min value element :  200

#===============================================================================