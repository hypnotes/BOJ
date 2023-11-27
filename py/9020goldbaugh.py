t = int(input())

for _ in range(t):
    n = int(input())

    p = [i for i in range(n+1)]
    p[0] = 0
        
    for i in range(2, n+1):
        flag = 1
        for j in range(i, n+1, i):
            if flag:
                flag = 0
            else: 
                p[j] = 0
        
    start = n//2

    while start!=1:
        comp = n - start
        if p[start] and p[comp]:
            print(start, comp)
            break
        start -= 1