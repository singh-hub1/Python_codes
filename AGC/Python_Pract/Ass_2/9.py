#Write a Python program to count the occurrences of each word in a given sentence

s=str(input('\nEnter a string\n'));
counts = dict()
w= s.split(" ")

for i in w:
   if i in counts:
        counts[i] += 1
   else:
      counts[i] = 1

print(counts);

"""
def word_occurences(str,word):
   x = str.split(" ")
   c = 0
   for i in range(0, len(x)):
      if (word == x[i]):
         c = c + 1
   return c

str=input("Enter String ::>")
word=input("Enter the word to count occurrence ::>")
print("THE NUMBER OF OCCURRENCE OF A WORD ",word,"is",word_occurences(str, word))

"""