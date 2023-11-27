from collections import deque

n, m, r = map(int, input().split())

di = {key : [] for key in [i for i in range(1, n+1)]}

for i in range(m):
    u, v = map(int, input().split())
    di[u].append(v)
    di[v].append(u)
    
visited = [0] * n

for i in di:
    di[i].sort(reverse=True)
    
def BFS(v):
    order = 1
    visited[v-1] = order
    needs_visit = deque()
    
    needs_visit.append(v)
    
    while needs_visit:
        next = needs_visit.popleft()
        for i in di[next]:
            if visited[i-1] == 0:
                order+=1
                visited[i-1] = order
                needs_visit.append(i)
        
BFS(r)
for i in visited:
    print(i)