n = int(input())

tri = []
for i in range(n):
    
    line = list(map(int, input().split()))
    
    if i:
        for j in range(i+1):
            if j == 0:
                line[j] += tri[-1][0]
            elif j == i:
                line[j] += tri[-1][-1]
            else:
                line[j] += max(tri[-1][j], tri[-1][j-1])
        
        del tri[0]
    tri.append(line)

print(max(tri[0]))