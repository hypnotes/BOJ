import sys 

input = sys.stdin.readline 

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0]*(m+1)
    dp[0] = 1
    for c in coins:
        for j in range(c, m+1):
            dp[j]+=dp[j-c]

    print(dp[m])