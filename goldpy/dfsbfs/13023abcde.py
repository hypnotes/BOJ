import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

lenPeople, lenRelationship = map(int, input().split())

people = [[] for _ in range(lenPeople)]
visited = [False]* lenPeople

for _ in range(lenRelationship):
    a, b = map(int, input().split())
    people[a].append(b)
    people[b].append(a)

answer = 0

def dfs(currentNode: int, relationships: int):    
    visited[currentNode] = True
    if relationships == 4:
        return relationships
    
    for node in people[currentNode]:
        if not visited[node]:
            ans = dfs(node, relationships+1)
            if ans == 4:
                return ans
    visited[currentNode] = False 
    return 0

for i in range(lenPeople):
    answer = dfs(i, 0)
    if answer == 4:
        break 
    
print(1) if answer == 4 else print(0)