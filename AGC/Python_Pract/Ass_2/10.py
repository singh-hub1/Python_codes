#Remove special symbols/Punctuation from a given string.

"""s=str(input('\nEnter a string\n'))
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

new = " "
for ch in s:
   if ch not in punctuations:
       new = new + ch

print(new)
"""
s=str(input('\nEnter a string\n'))
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


for x in s.lower():
   if x in punctuations:
            s = s.replace(x, " ")
            s = s.replace(" ","")
print(s)


