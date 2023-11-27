mod = 1000000000

n, k = map(int, input().split())

dp = [[0]* (201) for _ in range(201)]

for i in range(1, k+1):
    dp[0][i] = 1
for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] =( dp[i-1][j] + dp[i][j-1]) % mod

print(dp[n][k])