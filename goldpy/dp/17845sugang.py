import sys 

input = sys.stdin.readline 

n, k = map(int, input().split())

dp = [[0]*(n+1) for _ in range(k+1)] 
li = [list(map(int, input().split())) for _ in range(k)]

for i in range(1, k+1):
    for j in range(1, n+1):
        if li[i-1][1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], li[i-1][0]+dp[i-1][j-li[i-1][1]])

print(dp[k][n])