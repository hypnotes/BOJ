import sys
from collections import deque

a = sys.stdin.readline()[:-1]

t = ''
s = deque()

for i in range(len(a)):
    
    if a[i] == '*' or a[i]=='/':
        if s and (s[-1] == '*' or s[-1] == '/') :
            t+=s.pop()
        s.append(a[i])
            
    elif a[i] == '+' or a[i] == '-':
        while s and s[-1] != '(' :
            t+= s.pop()
        s.append(a[i]) 
    elif a[i] == ')':
        while s and s[-1] != '(' :
            t+= s.pop()
        if s[-1] == '(':
            s.pop()
    elif a[i] == '(':
        s.append(a[i])
    else:
        t += a[i]
        
while s:
    if s[-1] != '(':
        t+=s[-1]
    s.pop()
    
print(t)
