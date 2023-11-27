import sys 
from collections import deque

input = sys.stdin.readline 

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]

ripeSoCheck = deque()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            ripeSoCheck.append((i,j,0))

dx = [-1, 1, 0, 0] #  LEFT RIGHT UP DOWN  
dy = [0, 0, -1, 1]

while ripeSoCheck:
    x, y, days = ripeSoCheck.popleft()
    
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        
        if (0 <= newX < n) and (0 <= newY < m):
            if tomatoes[newX][newY] == 0:
                tomatoes[newX][newY] = 1
                ripeSoCheck.append((newX, newY, days+1))

def CheckTomatoes():
    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 0:
                return False 
    return True

allRipe = CheckTomatoes()
print(days) if allRipe else print(-1)