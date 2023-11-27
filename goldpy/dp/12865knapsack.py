import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[0]* (k+1)  for _ in range(n+1)] 
li = []
for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))


for i in range(1, n+1):
    for j in range(1, k+1):
        if li[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(li[i-1][1]+dp[i-1][j-li[i-1 ][0]], dp[i-1][j])

print(dp[n][k])