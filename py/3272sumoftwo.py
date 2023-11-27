n = int(input())
li = list(map(int, input().split()))
x = int(input())

dp = [0] * 1000002
count = 0

li.sort()
for i in li:
    dp[i] = 1

for i in li:
    if i >= x-i:
        break
    elif x-i <= 1000000 and dp[x-i]:
        count+=1 

print(count)