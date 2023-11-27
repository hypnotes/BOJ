a = input()
b = input()

dp = [0] * 1000

for i in range(len(a)):
    curmax = 0
    for j in range(len(b)):
        if curmax < dp[j]:
            curmax = dp[j]
        elif a[i] == b[j]:
            dp[j] = curmax + 1

print(max(dp))