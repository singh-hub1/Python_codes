
# Write a Python program to accept the strings which contains all vowels
def check_vowels(string):

   vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

   for i in string:
      if i not in vowels:
         print( "Not accepted")
         break
   else:
      print("Accepted")

s=str(input('Enter a string\n'));
check_vowels(s);