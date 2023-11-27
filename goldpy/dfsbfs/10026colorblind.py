import sys 

input = sys.stdin.readline 
sys.setrecursionlimit(1000000)

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

isColorBlind, notColorBlind = 0, 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    
    visited[x][y] = True
    color = board[x][y]
    
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if(0 <= newX < n) and (0 <= newY < n):
            if (visited[newX][newY] == False and board[newX][newY]==color):
                dfs(newX, newY)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            notColorBlind += 1

# R -> G
for i in range(n): 
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = 'G'
        visited[i][j] = False

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            isColorBlind += 1

print(notColorBlind, isColorBlind)