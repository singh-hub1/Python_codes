#range function in python

"""n=int(input("enter any number\n"))
if n in range(1,51):
    print("ok")
else:
    print("out of range")
  """


"""n=int(input("enter any number\n"))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print(n,"is not a prime number\n")
            break
        else:
            print(n,"is prime number\n")
            break
else:
    print("enter correct input!!")"""

"""for letter in "tybca":
    if letter=="b":
       break
    print("current letter is=",letter)
"""

"""for letter in "tybca":
    if letter=="b":
       continue
    print("current letter is=",letter)"""

for letter in "tybca":
    if letter=="b":
       pass
    print("current letter is=",letter)