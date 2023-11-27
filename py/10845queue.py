import sys

q = []
n = int(sys.stdin.readline()) 

for _ in range(n):

    com = sys.stdin.readline()
    
    if com == "pop\n":
        print(q.pop(0)) if q else print(-1)
    elif com == "size\n":
        print(len(q))
    elif com == "empty\n":
        print(0) if q else print(1)
    elif com == "front\n":
        print(q[0]) if q else print(-1)
    elif com == "back\n":
        print(q[-1]) if q else print(-1)
    else:
        a, c = com.split()
        q.append(c)
    
