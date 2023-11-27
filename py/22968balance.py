#https://atgane.tistory.com/71 

t = int(input())

#make table for reusage
i=0
heightTable = [1, 2]
while heightTable[-1] < 1000000000:
    heightTable.append(heightTable[-2]+heightTable[-1]+1) #최소노드 (left) + 최소노드 (right) + parentnode(1)


def findHeight(v):
    
    for i in range(len(heightTable)):
        if v < heightTable[i]:
            print(i)
            return 


for _ in range(t):
    v = int(input())
    
    findHeight(v)


