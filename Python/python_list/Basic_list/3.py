#***********************************************************************************************************************

#TUPLE() are fater than the list[]
#TUPLE() are immutable,cannot be changed.

#***********************************************************************************************************************

#tuples are immutable, but we know Lists are mutable.
# So if you change a tuple to a list, it will be mutable.
# Then you can delete the items by the condition, then after changing the type to a tuple again.

#***********************************************************************************************************************

t=(1,2,3,45,5);
print(t);#(1, 2, 3, 45, 5)

y=("vishal","singh");
print(y);#('vishal', 'singh')


t1=()
print(t1);#()--empty tuple

t2=('aaa',(2,3),[4,5])#nested tuple
print(t2);#('aaa', (2, 3), [4, 5])

t3='zzz',(4,7),[9,1] #without circular bracket is called 'tuple packing'
print(t3)#('zzz', (4, 7), [9, 1])

"""
a,b,c=t2
print(a,b,c)
"""

tup=("apple","orange",2019,1,2,3,4)
print(tup) #('apple', 'orange', 2019, 1, 2, 3, 4)

"""
del tup
print("after the deleting tup\n");
print(tup)
"""

print(tup[2:5]) #(2019, 1, 2)
print(tup[2:])#(2019, 1, 2, 3, 4)
print(tup[:4])#('apple', 'orange', 2019, 1)
print(tup[::-1])#(4, 3, 2, 1, 2019, 'orange', 'apple')
#reversing the tuple

#tup[0]="green"
#tup[0]="green"------TypeError: 'tuple' object does not support item assignment


#t=tuple("greps")
#print(t+tup) #('g', 'r', 'e', 'p', 's', 'apple', 'orange', 2019, 1, 2, 3, 4)

t=("greps",4)
print(t+tup)#('greps', 4, 'apple', 'orange', 2019, 1, 2, 3, 4)

l=list(tup)
print(l)#['apple', 'orange', 2019, 1, 2, 3, 4]

l.remove("apple")
print(l)#['orange', 2019, 1, 2, 3, 4]

tup=tuple(l)
print(tup)#('orange', 2019, 1, 2, 3, 4)

for x in tup:
    print(x,"\t")
#orange
#2019
#1
#2
#3
#4

print(tup*2)#('orange', 2019, 1, 2, 3, 4, 'orange', 2019, 1, 2, 3, 4)

print("orange" in tup)#true
print("orange" not in tup)#false
#in & not in are membership operator

#   0   1        2
t5=(1,[2,3,4,5],(6,7,8))
print(t5)#(1, [2, 3, 4, 5], (6, 7, 8))

print(t5[0])#1
print(t5[1][2])#4
print(t5[2][1])#7

print(len(t5))#3

t7=(8,9,0,6,5)
print(max(t7))#9
print(min(t7))#0
