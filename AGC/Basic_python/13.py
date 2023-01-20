#***************Function In Python********************************

"""def my_function(): #this is function defination
    print("vishal singh");

my_function();#this is function call

#==================================================================

def my_func(n):
    print(n**2);

a=int(input("\nEnter one number\n"));
my_func(a);

#===================================================================

def my_fun(name):
    print("Welcome "+"\t" +name);

x=str(input("\nEnter your name\n"));
my_fun(x);"""

#=========================================

"""def addition(x,y):
    print("Avg = ",x+y/2)
    print("sum = ",x+y)



a = int(input("\nEnter one number\n"));
b = int(input("\nEnter second number\n"));
addition(a,b);"""

#==========================================================
#CALL BY VALUE
"""#Find largest among three nos.
def my_func(x,y,z):
    if((x>=y) and(x>=z)):
        large=x;
    elif((y>=x) and(y>=z)):
        large=y;
    else:
        large=z;

    print("the largest among three numbers is ",large);

a = float(input("\nEnter first number\n"));
b = float(input("\nEnter second number\n"));
c = float(input("\nEnter third number\n"));
my_func(a, b,c);"""

#=================================================================
"""#CALL BY OBJECT(REFERENCE)

def my_func(lst):
    lst.append([2,4,5]);
    print(lst);
    print((lst[2:5]))

lst=[1,4,8,0];
my_func(lst);"""

#=============================================================
"""#KEYWORD ARGUMENT

def func(str,age):
    print(str,age);

func(str= "SYBCA",age=20);"""

#================================================================

def func(str,age):
    print(str,age);

func(age=20,str= "SYBCA");

#=======================================================================





