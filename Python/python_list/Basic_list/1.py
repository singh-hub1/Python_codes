#=========================================================anonymous function============================================================================
x=lambda a:a+10 #function name is lambda
print(x(5)) #15

#================================Functional programming tools - filter(), map(), and reduce()========================================================

#python code to illustrate filter() with lambda()
st=[2,4,7,9,12,23,44,61]
st_result=list(filter(lambda x:(x%2!=0),st))
print(st_result)#[7, 9, 23, 61]
#=======================================================================================================================

#=================================use of lambda() with map()==============================================================================
st=[2,4,7,9,12,23,44,61]
st_result=list(map(lambda x:(x%2!=0),st))
print(st_result)
#[False, False, True, True, False, True, False, True]

#use of lambda with map()
st=[2,4,7,9,12,23,44,61]
st_result=list(map(lambda x: x**2,st))
print(st_result)
#[4, 16, 49, 81, 144, 529, 1936, 3721]

#==============================================================use of lambda()with reduce()===============================================
from functools import reduce
st=[2,4,7,9,12,23,44,61]
sum = reduce((lambda x,y:x+y),st)
print(sum)#162
#=====================================================================================================================================
