#Write a Python program to remove the characters which have odd index values of a given string
s=str(input('\nEnter a string\n'));

result = " "
for i in range(len(s)):
    if i % 2 == 0:
      result = result + s[i]

print(result);

