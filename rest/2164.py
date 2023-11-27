
from collections import deque

a = int(input())

li = list(range(1, a+1))

q = deque(li)

while(len(q)>1):
    q.popleft()
    q.append(q.popleft())
   
print(q[0])

