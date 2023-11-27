import sys 

input = sys.stdin.readline 

n = int(input())
arr = [0] * n
lose= [0] * n 
lose[-1] = 1000000000
count = [0] * n 

for i in range(n):
    arr[i] = int(input())


for i in range(n-2, -1, -1):
    cmpIdx = i+1 

    while cmpIdx < n and arr[i] > arr[cmpIdx]:   
        count[i]+=1 
        count[i]+=count[cmpIdx]
        cmpIdx = lose[cmpIdx]
    
    lose[i] = cmpIdx
print(sum(count))
