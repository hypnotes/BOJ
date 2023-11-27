from collections import deque

def bfs(graph:  dict[int, list]):
    
    visited = deque([])
    tobevisited = deque([1])

    while tobevisited:
        temp = tobevisited.popleft()
        if temp not in visited:
            visited.append(temp)
            tobevisited.extend(graph[temp])

    return len(visited)
    

testCount = int(input())

for _ in range(testCount):
    li = list(map(int, input().split()))
    nodeCount = li[0]
    connectionCount = li[1]
    connections = {i:[] for i in range(nodeCount)}

    for i in range(2, len(li), 2):
        connections[li[i]].append(li[i+1])
        connections[li[i+1]].append(li[i])

    print('Connected.') if bfs(connections)==nodeCount else print('Not connected.')