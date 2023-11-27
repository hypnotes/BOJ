import sys 

input = sys.stdin.readline 

n, m = (lambda li: (int(li[0]), int(float(li[1])*100+0.5)))(input().split())

while n!=0 and m !=0:
    
    dp = [0] * (10001)
    li = [(lambda li: [int(li[0]),  int(float(li[1])*100+0.5)])(input().split()) for _ in range(n)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j < li[i-1][1]:
                continue
            dp[j] = max(dp[j-li[i-1][1]]+li[i-1][0], dp[j])

    print(dp[m])
    n, m = (lambda li: (int(li[0]),  int(float(li[1])*100+0.5)))(input().split())

