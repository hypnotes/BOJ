import sys 

input = sys.stdin.readline 

n, m = map(int, input().split())
li = [int(input()) for _ in range(n)]
li.sort()
ans =  2000000001
i, j = 0, 0

while i < n:
    temp = abs(li[i]-li[j]) 
    if temp < m :
        i+=1
        continue 
    if temp == m:
        ans = m 
        break 
    ans = min(ans, temp)
    j+=1 

print(ans)
