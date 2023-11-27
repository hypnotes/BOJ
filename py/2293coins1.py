n, k = map(int, input().split())

dp = [0] * (k+1)
v = []

for _ in range(n):
    v.append(int(input()))

dp[0] = 1

for i in v: #1, 2, 5 
    for j in range(i, k+1):
        dp[j] = dp[j] + dp[j-i]

print(dp[-1])    