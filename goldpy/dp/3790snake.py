from collections import deque

b = int(input())
a = int(input())

apple, dir, cur = [], deque(), deque()
coor = [[0,1], [1,0],[0,-1],[-1,0]]
for _ in range(a):
    apple.append(list(map(int, input().split())))
d = int(input())
for _ in range(d):
    x, y = input().split()
    dir.append([int(x), y])

cur.append([0,0])
time, turn = -1, 0

while True:
    time += 1
    print(time, cur)
    
    if cur[0][0] < 0 or cur[0][0]>=b or cur[0][1] < 0 or cur[0][1] >=b:
        break
    
    if dir and time== dir[0][0]:
        if dir[0][1] == "L":
            turn = (turn-1)%4
            print("TURN ", test[turn])
        else:
            turn = (turn+1)%4
            print("TURN ", test[turn])
        dir.popleft()
    
    newcur = [cur[0][0]+coor[turn][0], cur[0][1]+coor[turn][1]]
    print("next location: ", newcur)
    if newcur not in cur:
        cur.appendleft(newcur)
    else:
        break
    
    enlarge = 0 
    for i in range(len(apple)):
        if enlarge==0 :
            if apple[i] == cur[0]:
                print("APPLE EATEN")
                del apple[i]
                enlarge = 1
            
    if not enlarge:
        cur.pop()
    
    #print(time, cur)
    
    #time += 1
    
   
    
    
print(time)
