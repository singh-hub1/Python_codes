def power(a,b):
    """this is print only comment line in python"""

print(power.__doc__)




def add(a,b):
    """returns addition of two numbers"""
    print(a+b)
print(add.__doc__)


def longlen(*strings):
    """this will find maximum length of the string"""
    m=0;
    for s in strings:
        if len(s)>m:
            m=len(s);
    print(m);
print(longlen.__doc__)
longlen("vishal","singh","aaa","arya")


def func1(farg,*args):
    print("Formal argument is: ",farg);
    for i in args:
        print("Another argument is:= ",i)
func1(1,2,"vishal","singh","arya")


def func2(**arg):
    for i in arg:
        print(i,arg[i]);
func2(a=1,b=2,c=3,d=4,e=5)



def func1(a1,a2,*args):
    print("Formal argument is: ",a1,a2);
    for i in args:
        print("Another argument is:= ",i)
func1(1,2,"vishal","singh","arya")


square=lambda x1:x1*x1
print("square of the number is= \n",square(10))

#========================================================

"""
to find the factorial of a number in recursion function
"""
def recur(x):
    if x==1:
        return 1;
    else:
        return(x*recur(x-1))
print("\nThe factorial of a number is= ",recur(4))

#====================================================
"""
to find fibonacci series using recursion
"""
def fib(n):
    if n<=1:
        return n;
    else:
        return(fib(n-1)+fib(n-2))

a=int(input("\n'Enter how many terms u want'\n"))
for i in range(a):
    print(fib(i))
