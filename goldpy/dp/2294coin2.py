import sys

n, m = map(int, sys.stdin.readline().split())
MAXVAL = 100001
dp = [MAXVAL] * (MAXVAL)

for i in range(n):
    dp[int(sys.stdin.readline())] = 1

if  n > 1 and dp[2] == MAXVAL:
    dp[2] = dp[1] * 2

for i in range(3, m+1):
    if dp[i] != MAXVAL:
        pass 
    else:
        for j in range(1, i//2+1):
            dp[i] = min(dp[i], dp[i-j] + dp[j])
            
print(-1) if dp[m] == MAXVAL else print(dp[m])