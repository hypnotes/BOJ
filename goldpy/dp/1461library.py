import sys 
from collections import deque 

input = sys.stdin.readline 

n, m = map(int, input().split())
li = list(map(int, input().split()))
steps = 0 
isLast = True

li.sort()
if abs(li[0]) < abs(li[-1]):
    li = [li[i]*-1 for i in range(n)]
    li.reverse()
    
li = deque(li)
prev = 0
while li:
    for i in range(m):
        if not li:
            break
        if i==0:
            if isLast:
                steps += abs(li[0])
                isLast = False
            else:
                steps += abs(li[0])*2 
        prev = li.popleft()
        if li and li[0] > 0 and prev < 0:
            li.reverse()
            break

print(steps)