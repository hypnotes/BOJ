import sys 
from collections import deque
input = sys.stdin.readline 

peopleCount, partyCount = map(int, input().split())
knowsTruth = [0] * peopleCount 
knowLine = list(map(int, input().split()))
needsVisit = deque() 

for i in range(knowLine.pop(0)):
    knowsTruth[knowLine[i]-1] = 1
    needsVisit.append(knowLine[i])

closeWeb = {i : set() for i in range(1, peopleCount+1)}

parties = [] # [attendMemberCount, attendingMembers]
for party in range(partyCount):
    members = list(map(int, input().split()))
    totalAttend = members.pop(0)
    parties.append([totalAttend, members])
    for person in members:
        closeWeb[person].update(members)

def bfs():
    visited = [False] * (peopleCount)
    while needsVisit:
        current = needsVisit.popleft()
        visited[current-1]=True
        knowsTruth[current-1] = 1

        for friend in closeWeb[current]:
            if not visited[friend-1]:
                knowsTruth[friend-1] = 1
                needsVisit.append(friend)

bfs()

answer = 0
for i in range(partyCount):

    for j in range(parties[i][0]):
        if knowsTruth[parties[i][1][j]-1]:
            break
    else:
        answer += 1


print(answer)