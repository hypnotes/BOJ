import sys
from collections import deque 

input = sys.stdin.readline

n = int(input())
li = deque(map(int, input()[:-1].split()))

st = [deque([0]), deque([0]), deque([0]), deque([0])]

for i in li:
    
    mindiff, place = 100000, -1
    
    for x in range(4):
        
        if st[x] and st[x][-1] > i and i-st[x][-1] < mindiff:
            print("here")
            mindiff = i-st[x][-1]
            place = x

    if place >= 0:
        st[place].append(i)
    else:
        print("NO")
        break
    
print(st)
        