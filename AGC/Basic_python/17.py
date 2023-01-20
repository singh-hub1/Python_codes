#unpacking argument list in python
"""a=10;
b=20
c=30;
c,d=a,b;
print(c,d);#10 20
"""
#==============================================
# *(tuples)  or **(dictionary)
"""def fun(a,b,c,d):
    print(a,b,c,d)#1 2 3 4

my_list=[1,2,3,4];
fun(*my_list);"""

#===========================================

"""def fun(a,b,c,d):
    print(a,b,c,d)

d=(2,3,4,5)#2 3 4 5
fun(*d);
"""
#======================================

"""def fun(a,b,c,d):
    print(a,b,c,d)#a b c d

d={'a':2,'b':1,'c':5,'d':6}
fun(*d);"""

#=======================================

"""def fun(a,b,c,d):
    print(a,b,c,d)#2 1 5 6

d={'a':2,'b':1,'c':5,'d':6}
fun(**d);
"""
#======================================

def foo(text):
    return text.upper();

print(foo('hello'));#HELLO


u=foo;

print(u('hello'))#HELLO

#=====================================================

#Duck_Typing:

#=======================================================

#demonstrtate of class
class Duck:
    def fly(self):
        print('duck flying')

class Airplane:
    def fly(self):
        print('airplane flying')

class Whale:
    def swim(self):
        print('whale swimming')
    """def fly(self):
        print('whale swimming')"""

def lift_off(entity):
    entity.fly()



duck=Duck();
airplane=Airplane();
whale=Whale();

lift_off(duck);
lift_off(airplane);
lift_off(whale);

#===========================================================



