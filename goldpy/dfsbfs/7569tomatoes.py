import sys 
from collections import deque

input = sys.stdin.readline 

m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

ripeSoCheck = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 1:
                ripeSoCheck.append((i,j, k, 0))

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

TOTAL_DIRECTIONS = 6

while ripeSoCheck:
    z, x, y, days = ripeSoCheck.popleft()
    
    for i in range(TOTAL_DIRECTIONS):
        newX = x + dx[i]
        newY = y + dy[i]
        newZ = z + dz[i]
        if (0 <= newX < n) and (0 <= newY < m) and (0 <= newZ < h):
            if tomatoes[newZ][newX][newY] == 0:
                tomatoes[newZ][newX][newY] = 1
                ripeSoCheck.append((newZ, newX, newY, days+1))

def CheckTomatoes():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomatoes[i][j][k] == 0:
                    return False 
    return True

    
allRipe = CheckTomatoes()
print(days) if allRipe else print(-1)