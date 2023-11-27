import sys
sys.setrecursionlimit(100000)


n, m, r = map(int, input().split())

di = {key : [] for key in [i for i in range(1, n+1)]}

for i in range(m):
    u, v = map(int, input().split())
    di[u].append(v)
    di[v].append(u)
    


visited = [0] * n
order = 0

def DFS(r):
    global order
    order += 1
    visited[r-1] = order
    
    di[r].sort()
    
    for i in di[r]:
        if visited[i-1]== 0:
            DFS(i)
        
DFS(r)

for i in visited:
    print(i)