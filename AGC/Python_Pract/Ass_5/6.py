#Write a Python program to sort a dictionary by key.

dict_color = {'Red':'#FF0000',
          'Green':'#008000',
          'Black':'#000000',
          'White':'#FFFFFF'}

for key in sorted(dict_color):
    print("%s:= %s" % (key,dict_color[key]))