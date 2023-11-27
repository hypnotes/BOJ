import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = True
    while queue:
        now = queue.popleft()
        for i in range(1, 7):
            next_move = now + i
            if 1 <= next_move <= 100 and not visited[next_move]:
                if next_move in snack.keys():
                    next_move = snack[next_move]
                if next_move in ladder.keys():
                    next_move = ladder[next_move]
                if not visited[next_move]:
                    queue.append(next_move)
                    visited[next_move] = True
                    board_cnt[next_move] = board_cnt[now] + 1


N, M = map(int, sys.stdin.readline().split())
board_cnt = [0] * 101
visited = [False] * 101

snack = dict()
ladder = dict()
for _ in range(N):
    u, v = map(int, sys.stdin.readline().split())
    ladder[u] = v
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    snack[u] = v

bfs()
print(board_cnt[100])

