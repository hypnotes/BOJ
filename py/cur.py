from collections import deque
n = 5
r, c = 1, 1 #13

ans = 2**(n-1) * r +  c
li = deque(i for i in range((2**n)*2))

for i in range(len(li)):
    if (i) % (2**(n-1)) == 0:
        print()
    print(li[i], end=" ")
    

print(ans)