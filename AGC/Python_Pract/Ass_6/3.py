"""
Write a Python function to check whether a number is in a given range.
"""

def test_range(lower,upper,x):
    if x in range(lower,upper):
        print( 'the number is in the range')
    else :
        print("The number is outside the given range.")
lower=int(input('\nEnter lower bound\n'))
upper=int(input('\nEnter upper bound\n'))
x=int(input('\nEnter a number to check\n'))
test_range(lower,upper,x);
