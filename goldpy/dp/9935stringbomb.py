import sys
from collections import deque

a = sys.stdin.readline()[:-1]
b = sys.stdin.readline()[:-1]

s = []


for i in range(len(a)):
    
    s.append(a[i])
    
    if s[-1] == b[-1] and ''.join(s[-len(b):]) == b:
        del s[-len(b):]

print(*s, sep="") if s else print('FRULA')