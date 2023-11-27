from collections import deque
#DFS, BFS는 https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-BOJ-1260-DFS%EC%99%80-BFS 참고

n, m, v = map(int, input().split())
graph = {}

graph = {key : [] for key in [i for i in range(1, n+1)]}

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    graph[i].sort()
# print(graph)
# print(visited)

def DFS(v):
    print(v, end=" ")
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0: 
            DFS(i)
                
def BFS(v):
    
    visited[v] = 1
    needs_visit = deque()
    
    needs_visit.append(v)
    
    while needs_visit:
        next = needs_visit.popleft()
        print(next, end=" ")
        for i in graph[next]:
            if visited[i] == 0:
                visited[i] = 1
                needs_visit.append(i)
            

        
visited = {key: 0 for key in [i for i in range(1, n+1)]}
dfs = DFS(v)
print()
visited = {key: 0 for key in [i for i in range(1, n+1)]}
bfs = BFS(v)



