import sys 

input = sys.stdin.readline 

n = int(input())
li = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 21):
        if li[i-1]+dp[i-1][j] <= 20:
            dp[i][j] = li[i-1]+dp[i-1][j]
        if dp[i-1][j] - li[i-1] >= 0:
            dp[i][j] =   dp[i-1][j] - li[i-1]
        
        print(dp[i][j], end=" ")
    print()
print(dp[-1][-1])