import sys 

input = sys.stdin.readline 
c, n = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

dp = [[100001]*(1101) for _ in range(n+1)] 
ans = 100001
for i in range(1, n+1):
    dp[i][0] = 0
    for j in range(1, 1101):
        if j >= li[i-1][1]:
            dp[i][j] = dp[i][j-li[i-1][1]]+li[i-1][0]
        dp[i][j] = min(dp[i][j], dp[i-1][j])
    for j in range(c, 1101):
        ans = min(ans, dp[i][j])

print(ans)