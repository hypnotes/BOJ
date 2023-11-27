import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

dp = [[0,0] for _ in range(n)]

dp[0][0] = li[0]
answer = li[0]
for i in range(1, n):
    
    
    dp[i][0] = li[i] if dp[i-1][0] < 0 else dp[i-1][0] + li[i]
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+li[i])
    answer = max(dp[i][1], dp[i][0], answer)

print(answer)