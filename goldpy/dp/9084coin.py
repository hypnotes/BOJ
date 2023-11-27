#LATER

import sys

n = int(sys.stdin.readline())
coin = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

dp = [0]* (m+1)

for i in range(n):
    dp[coin[i]] = 1

print(dp)

for i in range(1, m+1):
    
    for j in range(1, i//2+1):
        print("COMAPRING %d and %d" %( j , i-j))
        if dp[j] and dp[i-j]:
            dp[i] =  dp[j] + dp[i-j]
            print("ADDING UP %d + %d = %d" %( dp[j] , dp[i-j], dp[i]))

print(dp)