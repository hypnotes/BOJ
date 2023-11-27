import heapq

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

li.sort()
room = []
heapq.heappush(room, li[0][1])

for i in range(1, n):
    if li[i][0] < room[0]:
        heapq.heappush(room, li[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, li[i][1])
print(len(room))