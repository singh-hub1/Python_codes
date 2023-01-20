"""Write a program to replace all occurrences of ‘a’ with $ in a String. (Ex. apple then output is
$pple)."""
s=str(input('\nEnter a string\n'));
s=s.replace('a','$')
s=s.replace('A','$')
print("\nModified string:\n")
print(s)
