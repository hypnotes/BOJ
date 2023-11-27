import sys 

input = sys.stdin.readline 

n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

dest, curfuel = map(int, input().split())
curlo,count = 0,0
li.sort()
stationIdx = 0
flag = 1
temp = []
while curfuel < dest: 
    
    for i in range(stationIdx , n):
        if li[i][0] < curfuel:
            temp.append(li[i][1])
        else:
            stationIdx = i
            break 
    if not temp:
        flag = 0 
        break
    
    count+=1
    curfuel += temp[-1]
    temp.pop()

print(count) if flag else print(-1)

# while li and cur lo < dest:

#     best = [0, 0]
    
#     for i in range(stationIdx, n):
#         print(stationIdx, n)
#         if li[i][0] <= dest
            
#             break
#         elif li[i][1] >= best[1]:
#             best = li[i]
#             stationIdx = i
#     print(best)
#     if curfuel < 0 or  curlo + curfuel >= dest:
#         break
#     count+=1 

#     curfuel = curfuel - (best[0]-curlo) + best[1]
#     curlo= best[0]
    

