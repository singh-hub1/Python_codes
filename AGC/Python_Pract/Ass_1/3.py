"""Write a program which accepts an integer value as command line and print “Ok” if value is
between 1 to 50 (both inclusive) otherwise it prints” Out of range”
"""

n=int(input("enter any number\n"))
if n in range(1,51):
    print("ok")
else:
    print("out of range")

