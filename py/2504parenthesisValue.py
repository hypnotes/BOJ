import sys

n = sys.stdin.readline()

stack = []
ans = 0
temp = 1

for i in range(len(n)-1):
    
    if n[i] == "(":
        stack.append(n[i])
        temp *= 2 
    elif n[i] == "[":
        stack.append(n[i])
        temp *= 3
    elif n[i] == ")" and (not stack or stack[-1]=="["):
        ans = 0
        break
    elif n[i] == "]" and (not stack or stack[-1] =="("):
        ans = 0
        break
    elif n[i] == ")":
        if n[i-1] == "(":
            ans += temp
        temp //= 2
        stack.pop()
         
    else:
        if n[i-1] == "[":
            ans += temp
        temp //= 3
        stack.pop() 
        
if stack:
    print(0)
else:
    print(ans)
