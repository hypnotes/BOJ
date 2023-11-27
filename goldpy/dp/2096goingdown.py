import sys 

input = sys.stdin.readline

n = int(input())

minarr = list(map(int, input().split()))
maxarr = list(x for x in minarr)

for x in range(n-1):
    li = list(map(int, input().split()))
    minTmp = [0, 0, 0]
    maxTmp = [0, 0, 0]
    for i in range(3):
        if i == 0:
            minTmp[i] = min(minarr[i]+li[i], minarr[i+1]+li[i]) 
            maxTmp[i] = max(maxarr[i]+li[i], maxarr[i+1]+li[i]) 
        elif i == 2:
            minTmp[i] = min(minarr[i]+li[i], minarr[i-1]+li[i]) 
            maxTmp[i] = max(maxarr[i]+li[i], maxarr[i-1]+li[i])  
        else:
            minTmp[i] = min(minarr[i-1]+li[i], minarr[i]+li[i], minarr[i+1]+li[i]) 
            maxTmp[i] = max(maxarr[i-1]+li[i], maxarr[i]+li[i], maxarr[i+1]+li[i])   
    
    minarr = minTmp 
    maxarr = maxTmp

print(max(maxarr), min(minarr))