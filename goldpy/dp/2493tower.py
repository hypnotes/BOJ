import sys
from collections import deque

n = int(sys.stdin.readline())
t = deque(map(int, sys.stdin.readline().split()))
rec = [0] * n
temp = deque()
trear = n-1 #4

while t:
    cur = t.pop()
    trear -= 1
    
    if trear > -1 and cur <= t[trear]:
        
        while temp and temp[0][0] <= t[trear]:
            
            rec[temp[0][1]] = trear+1 
            temp.popleft()
                
        rec[trear+1] = trear+1
    
    else:
        temp.appendleft([cur, trear+1])
    

print(*rec)
