import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
s = list(map(int, input().split()))

d = []
if n<=k:
    print(0)
else:
    s.sort()
    for i in range(1,n):
        d.append(s[i]-s[i-1])

    d.sort()    
    
    for i in range(k-1):
        d.pop()
        
    print(sum(d))