#알고리즘 참고: https://chaewsscode.tistory.com/m/138
import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    minh, maxh = [], []
    li = [0] * (n+1)
    
    for i in range(n):
        cmd, val = input().split()
        val = int(val)
        
        if cmd[0] == "I":
            heapq.heappush(minh, [val, i])
            heapq.heappush(maxh, [val*-1, i])
            li[i] = 1
            
        else:
            if val == 1:
                while maxh and li[maxh[0][1]]==0:
                    heapq.heappop(maxh)
                if maxh:
                    li[maxh[0][1]] = 0
                    heapq.heappop(maxh)
            else:
                while minh and li[minh[0][1]]==0:
                    heapq.heappop(minh)
                if minh:
                    li[minh[0][1]] = 0
                    heapq.heappop(minh)
  
    while minh and li[minh[0][1]] == 0:
        heapq.heappop(minh)
    while maxh and li[maxh[0][1]] == 0:
        heapq.heappop(maxh)
    if minh and maxh:
        print(maxh[0][0]*-1, minh[0][0])
    else:
        print("EMPTY")