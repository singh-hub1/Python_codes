"""def foo(lst):
    lst.append([2,5,7])
    print(lst)
    return;

lst=[10,20,30]
foo(lst) #this is function call
print(lst)"""

"""#this is reference overwritten inside the function
def foo(lst):
    lst=[2,5,7]
    print(lst)
    return;

lst=[10,20,30]
foo(lst) #this is function call
print(lst)
"""

"""#default arguments
def mydata(name,age=20):
    print('name',name)
    print('age',age)
    return
mydata(age=22,name='vishal')
mydata(name='vishal')"""


"""def nsquare(x,y=2):
    return (x*x+2*x*y+y*y) #ther is no need to write return type
print(nsquare(2))
print(nsquare(2,6))
print(nsquare(4,2))
"""

"""
def printinfo(arg1,*vartuple):
    #first it take a argument and then it consider as a variable length in (*) symbol
    
    print('the output is')
    print(arg1)
    for var in vartuple:
        print(var)
    return;

printinfo(10)
printinfo(70,50,60,20);

"""

