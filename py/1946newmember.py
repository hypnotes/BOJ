
t = int(input())

for i in range(t):
    n = int(input())
    
    li = []
    for i in range(n):
        doc, interview = map(int, input().split())
        li.append([doc, interview])
    
    li.sort()
    count = 1
    bestinterview = li[0][1]
    for i in range(1, n):
        if li[i][1] < bestinterview:
            count+=1
            bestinterview = li[i][1]
    print(count)