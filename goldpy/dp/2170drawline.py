import sys

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

li.sort()
ans = [li[0]]

for i in range(1, n):
    if li[i][0] <= ans[-1][1] and li[i][1] <= ans[-1][1]:
        pass
    elif li[i][0] <= ans[-1][1]:
        ans[-1][1] = li[i][1]
    else:
        ans.append(li[i])

plen = 0
for i in ans:
    plen+=(i[1]-i[0])

print(plen)