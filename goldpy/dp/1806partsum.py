import sys

input = sys.stdin.readline

n, s = map(int, input().split())
li = list(map(int, input().split()))
i, j = 0, 0
ans = 100001
prefix = li[0]

while True:
    if prefix >= s:
        prefix -= li[i]
        ans = min(ans, j - i + 1)
        i += 1
    else:
        j += 1
        if j == n:
            break
        prefix += li[j]
 
print(0) if ans == 100001 else print(ans)

