import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

ans = [-1] * n
stack = [0]

for i in range(1, n):
    
    while stack and li[i] > li[stack[-1]]:
        ans[stack.pop()] = li[i]
    stack.append(i)

print(*ans)