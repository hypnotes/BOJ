import heapq

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

li.sort(key= lambda x:x[1])
room = []
heapq.heappush(room, li[0][2])

print(li)
for i in range(1, n):
    if li[i][1] < room[0]:
        heapq.heappush(room, li[i][2])
    else:
        heapq.heappop(room)
        print('after popped:', room)
        heapq.heappush(room, li[i][2])
    print(room)
print(len(room))