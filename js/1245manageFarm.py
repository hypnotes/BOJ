N, M = map(int, input().split(" "))

visited = [[False for _ in range(M)] for _ in range(N) ]

farmland = [ list(map(int, input().split(" "))) for _ in range(N)]

isPeak = True 
answer = 0

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

def dfs(x, y):
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if(nx < 0 or nx >= N or ny <0 or ny >= M ):
        continue
      if(farmland[x][y] < farmland[nx][ny]):
        isPeak = False
      if(visited[nx][ny]):
        continue
      if(farmland[x][y] == farmland[nx][ny]):
        visited[nx][ny] = True
        dfs(nx, ny)
    return 
  
for i in range(N):
  for j in range(M):
    if(visited[i][j]):
      continue
    isPeak = True 
    visited[i][j] = True
    dfs(i, j)
    if(isPeak):
      answer+=1

print(answer)