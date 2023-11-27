import sys

n = int(sys.stdin.readline())

li = [0] * n

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li[i] = [a,b]

li.sort()

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    cmax = 0
    for j in range(0, i):
        if li[i][1] > li[j][1]:
            cmax = dp[j] if cmax < dp[j] else cmax 
    
    dp[i] = cmax + 1
    
print(n-max(dp))
        