t = int(input())
p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def padovan(n):
    
    if n <= len(p):
        return p[n-1]
    
    else:
        s = len(p)
        for i in range(s+1, n+1):
            #print("%d + %d = %d" %(p[i-6], p[i-2], p[i-6] + p[i-2]))
            p.append(p[i-6] + p[i-2])
            #print(p)
        
        return p[-1]

for _ in range(t):
    n = int(input())
    print(padovan(n))