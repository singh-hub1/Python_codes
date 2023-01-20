#Write a Python program to create a shallow copy of sets.

p={1,2,3,4};
q=p.copy();
q.add('5');
print('numbers',p);#numbers {1, 2, 3, 4}

print('new_numbers',q);#new_numbers {1, 2, 3, 4, '5'}