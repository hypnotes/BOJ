import sys
import re
a = int(sys.stdin.readline())

for _ in range(a):
    
    b = int(sys.stdin.readline())
    flag = 'None'
    
    li = [sys.stdin.readline()[:-1] for _ in range(b)]
    li.sort()

    for i in range(1, len(li)):
       
        if len(li[i]) > len(li[i-1]):
            a, b= li[i-1], li[i]
        else:
            a, b = li[i], li[i-1]
        
        flag = 1 if a == b[:len(a)] else 0        
        if flag:
            break
        
    print("NO") if flag else print("YES")
        