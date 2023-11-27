from collections import deque
import sys 

input = sys.stdin.readline

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
bag = [[int(input()), i+1] for i in range(m)]

for b in range(m):
    w = bag[b][0]
    dp = deque([[0]*(w+1), [0]*(w+1)]) 

    for i in range(1, n+1):
        for j in range(1, w+1):
            if li[i-1][0] > j: 
                dp[1][j] = dp[0][j]
            else:
                dp[1][j] = max(dp[0][j], li[i-1][1]+dp[0][j-li[i-1][0]])
        dp.popleft()
        dp.append([0]*(w+1))
    bag[b][0] = dp[0][-1]/w
bag.sort()
print(bag[-1][1])