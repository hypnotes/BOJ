#https://chelseashin.tistory.com/10
#에서 알고리즘 참고했습니다

from collections import deque

n = int(input())

area = []
for _ in range(n):
    a = input()
    area.append([int(w) for w in a])

cx = [1, -1, 0, 0]  #갈 수 있는 좌표 4가지 (위아래, 양옆)
cy = [0, 0, 1, -1]

def BFS(nx, ny, ):
    
    
    
    
visited = deque([(0, 0)])
result = 0

while visited:
    x, y = visited.popleft()
    for i in range(len(cx)):
        nx = x + cx[i]  #x좌표 받기
        ny = y + cy[i]  #y좌표 받기
        if 0 <= nx < n and 0 <= ny < m: #받아온 x,y좌표 범위 내 인지 확인
            if area[nx][ny] == 1:   #벽이 아닌 길일 때
                area[nx][ny] = area[x][y] + 1   #방문+기록
                visited.append((nx, ny))
                
print(area[n - 1][m - 1])