n, k = map(int, input().split())

dp = [[1001]*(k+1) for _ in range(n+1)] 
li = list(map(int, input().split()))

cup = n+1

for i in range(1, n+1):
    for j in range(1, k+1):
        if li[i-1] > j: 
            dp[i][j] = dp[i-1][j]
        elif li[i-1] == j:
            dp[i][j] = 1
        else:
            if dp[i-1][j-li[i-1]]:
                dp[i][j] = min(dp[i-1][j], 1+dp[i-1][j-li[i-1]])

if dp[n][k] != 1001:
    print(dp[n][k])
elif not k:
    print(0)
else:
    print(-1)
