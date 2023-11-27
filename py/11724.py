n, m = map(int, input().split())
 
graph = {}

graph = {key : [] for key in [i for i in range(1, n+1)]}

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * n
components = []

def DFS(v):

    visited[v-1] = 1

    for i in graph[v]:
        if visited[i-1] == 0: 
            DFS(i)


count = 0

for i in range(len(visited)):
    if visited[i]== 0:
        DFS(i+1)
        i == 0
        count += 1 
        
print(count)