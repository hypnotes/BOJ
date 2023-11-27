import sys 
input = sys.stdin.readline 

n = int(input())
tree = list(map(int, input().split()))
xnode = int(input())

def dfs(vertex):
    tree[vertex] = -2
    for i in range(n):
        if vertex == tree[i]:
            dfs(i)

dfs(xnode)
count = 0

for i in range(n):
    if tree[i] != -2 and i not in tree:
        count+=1

print(count)