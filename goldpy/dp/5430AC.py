from collections import deque
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    cmd = input()
    n = int(sys.stdin.readline())
    li = []
    r , flag = 0, 1
    if n :
        li = deque(map(int, input()[1:-1].split(',')))
    else:
        b = input()
    
    for i in range(len(cmd)):
        if cmd[i] == "R":
            r+=1
        elif cmd[i == "D"]:
            if li:
                if r%2 == 0:
                    li.popleft()
                else:
                    li.pop()
            else:
                flag = 0
                break
                
    if flag and r%2 == 1: 
        li.reverse()
        
    print(str(list(li)).replace(" ", "")) if flag else print("error")
    