#Write a Python program to calculate the Number of Digits and Letters in a string.

s = str(input("\nInput a string\n"))
digit=letter=0
for c in s:
    if c.isdigit():
        digit=digit+1

    elif c.isalpha():
        letter=letter+1

    else:
        pass
print("Numbers of Letters:= ", letter)
print("Numbers of Digits:= ", digit)
