from collections import deque 

li = deque(input())
plus, mul = [0], [0]

while li:
    if len(li) > 1 and li[1] == '(':
        mul.append(int(li[0]))
        plus.append(0)
        li.popleft()
    elif li[0] == ')':
        plus[-2] += ((plus[-1]) * mul[-1])
        plus.pop()
        mul.pop()
    else:
        plus[-1]+=1
        
    if li :
        li.popleft()

while len(plus) != 1:
    plus[-2] += ((plus[-1]) * mul[-1])
    plus.pop()
    mul.pop()
    
print(plus[0])
