import sys
from collections import deque
li = deque([])

a = int(sys.stdin.readline())

for i in range(a):
    command = sys.stdin.readline().split()
    if command[0] =="push":
        li.append(command[1])
    elif command[0] == "pop":
        if not li:
            print(-1)
        else:
           print(li.popleft())
    elif command[0] == "size":
        print(len(li))
    elif command[0] == "empty":
        if len(li)==0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not li:
            print(-1)
        else:
            print(li[0])
    elif command[0] == "back":
        if not li:
            print(-1)
        else:
            print(li[len(li)-1])
