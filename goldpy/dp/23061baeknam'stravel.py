import sys 

input = sys.stdin.readline 

n, m = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]
bag = [[int(input()), i+1] for i in range(m)]

bag.sort()

dp = [[0]*(bag[-1][0]+1) for _ in range(n+1)] 

for i in range(1, n+1):
    for j in range(1, bag[-1][0]+1):
        if li[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], li[i-1][1]+dp[i-1][j-li[i-1][0]])

ans = [0, 0]
for i in range(len(bag)):
    if dp[n][bag[i][0]]/bag[i][0] > ans[0]:
        ans = [dp[n][bag[i][0]]/bag[i][0], bag[i][1]]
print(ans[1])