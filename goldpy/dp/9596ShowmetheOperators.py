import sys
from collections import deque 

input = sys.stdin.readline

n = int(input())

for i in range(n):
    
    num = deque()
    op = deque()
    
    s = list(input()[:-1].split())
    order = deque()
    for x in range(len(s)):
        if x%2 == 0 and op and (op[-1] == "*" or op[-1]=="/"):
            order.append(op[-1])
            num.append(str(eval("%s%s%s" %(num.pop(), op.pop(), s[x]))))
        elif x%2 == 0:
            num.append(s[x])
        else:
            op.append(s[x]) 

    while op:
        order.append(op[0])
        num.appendleft(str(eval("%s%s%s" %(num.popleft(), op.popleft(), num.popleft()))))
    
    ans = int(float(num[0])) if float(num[0]).is_integer() else float(num[0])
    print("Case #%d:" %(i+1), *order, ans)
    