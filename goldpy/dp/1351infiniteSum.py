import sys 
from collections import defaultdict

n, p, q = map(int, sys.stdin.readline().split())
di = defaultdict(int)
di[0] = 1

a = 1

def infiniteSum(n):
    if di[n]:
        return di[n]
    else: 
       di[n] = infiniteSum(n//p) + infiniteSum(n//q)
       return di[n] 

infiniteSum(n)
print(di[n])
