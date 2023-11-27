n, t = map(int, input().split())

li = []
dp = [[0]*(t+1) for _ in range(n+1) ]
for i in range(n):
    li.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, t+1): 
        if li[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-li[i-1][0]]+li[i-1][1])
print(dp[n][t])