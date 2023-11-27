import sys

input = sys.stdin.readline 

n = int(input())
li = []

for i in range(n):
    li.append([int(input()), i])
    
li.sort()

maxround = 0

for i in range(n):
    maxround = li[i][1] - i if li[i][1]-i > maxround else maxround 


print(maxround+1)
