str='vishal singh'
print(str) #vishal singh

str="justin"
print("The updated string is:=",str) #The updated string is:= justin

s1=input("enter the name=:")
print(s1)#enter the name=:singh

print(s1+str)#singhjustin

# 0  1  2  3  4  5
# j  u  s  t  i  n
#-6 -5 -4 -3 -2 -1

print(str[0])#j
print(str[2:5])#sti--start from 2nd index(including) but excluding 5th index
print(str[2:])#stin--start from 2nd index(including) till last
print(str[:3])#jus--start from first index(including) but excluding 3rd index
print(str*2)#justinjustin--justin print 2 times here
s=len(str) #it print length of the string
print(s)#6
print(str[-5:-1])#usti-- including -5th index but excluding -1th index
print(str[::-1])#nitsuj--including all the index in the string and print in the reverse order
