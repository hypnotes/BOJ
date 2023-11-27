import sys 
sys.setrecursionlimit(10**6)

## UNDONE 
input = sys.stdin.readline 

n = int(input())

friends = {i: [0]+[n+1]*(i-1)+[0]+[n+1]*(n-i) for i in range(1, n+1)}

best = n+1
bestPeople = []

a, b = map(int, input().split())

while a!= -1 and b!= -1:
    friends[a][b]=1
    friends[b][a]=1
    a, b = map(int, input().split())

print(friends)

def dfs(cur, find, depth):
    print('visiting ', cur, end=" ")
    # if friends[cur][find-1] == n+1: # visited but no relationship
    #     print('oops not here')
    #     return n+1
    if friends[cur][find] == 1: # found and return depth
        print('found it! returning ', 1+depth)
        return 1+depth
    
    for relationships in range(1, n+1):
        if friends[cur][relationships] != 1 and friends[cur][relationships]!= 0:
            for canVisit in friends[cur]:
                if canVisit==1:
                    friends[cur][find] = min(friends[cur][find], dfs(canVisit, relationships, depth+1))
    
    return depth+friends[cur][find]

dfs(2, 5, 0)
# for person in friends.keys():
#     dfs(person)
print(friends)
