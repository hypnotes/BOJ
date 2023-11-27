memberCount = int(input())

friendRelationships = [[None for _ in range(memberCount+1)] for _ in range(memberCount+1)]

while(True):
    a, b = map(int, input().split(' '))
    
    if(a==-1 and b==-1):
      break
    friendRelationships[a][b] = 1
    friendRelationships[b][a] = 1

def getFriendList(member):
   return friendRelationships[member][1:member]

def getVerticalFriendList(member):
   friendList = []
   for i in range(member+1, memberCount+1):
      friendList.append(friendRelationships[i][member])
   return friendList

for member in range(1, memberCount+1):
   friendList = getFriendList(member)
   for j in range(1, len(friendList)):
      if(friendList[j]!=None):
        friendList2 = getVerticalFriendList(j)
        bestChoice = memberCount+1
        print('for friend', j, ':', friendList2)
        for k in range(1, len(friendList2)):
           if(friendList2[k] and friendList[friendList2[k]] and friendList2[k]+1 < bestChoice):
              bestChoice= friendList2[k]+1
        friendRelationships[member][j] = None if(bestChoice == memberCount+1) else bestChoice

# for i in friendRelationships:
#    print(i)         
