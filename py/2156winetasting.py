n = int(input())

dp = [[0, 0]] * 3
curmax = 0
for i in range(3, n+3):
    w = int(input())
    dp.append([max(w + max(dp[i-2]), w + max(dp[i-3])), w + dp[i-1][0]])
    
    tempmax = max(dp[i])
    curmax = tempmax if tempmax > curmax else curmax
print(curmax)