import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
a = sys.stdin.readline()

s = deque()
i= 0
for i in range(n):
    

    while s and k and s[-1] < int(a[i]):
        s.pop()
        k -= 1

    s.append(int(a[i]))
    
while k:
    s.pop()
    k-=1
    
print(*s, sep='')