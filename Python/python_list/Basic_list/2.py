#STACK and QUEUE in python
"""s=[1,2,3,4,5]
print(s)#[1, 2, 3, 4, 5]
s.append(6) #append meaning is push into the stack
print(s)#[1, 2, 3, 4, 5, 6]
s.pop()
print(s)#[1, 2, 3, 4, 5]
"""
from collections import deque
#queue in python
s=deque([1,2,3,4,5])
print(s)#deque([1, 2, 3, 4, 5])
s.appendleft(6)
print(s)#deque([6, 1, 2, 3, 4, 5])
s.popleft()
print(s)#deque([1, 2, 3, 4, 5])
