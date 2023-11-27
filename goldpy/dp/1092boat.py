import sys

input = sys.stdin.readline 

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
cranes.sort(reverse=True)
box.sort(reverse=True)
sec = 0
if box[0] > cranes[0]:
    print(-1)
else:
    while box:
        if not box: 
            break
        for i in range(n):
            for j in range(len(box)):
                if cranes[i] >= box[j]:
                    del box[j]
                    break
        sec +=1

    print(sec)