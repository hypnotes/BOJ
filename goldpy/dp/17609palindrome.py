import sys


def check(a, flag):
    alen = len(a)
    for i in range(alen//2):
                
        if a[i] != a[alen-i-1]:
            if not flag:
                b = a[:i] + a[i+1:]
                c = a[:alen-i-1]+a[alen-i:]
                if check(b, 1)!=2:
                    return 1
                elif check(c, 1)!=2:
                    return 1
                else:
                    return 2
            else:
                return 2
        
    return flag
            

input = sys.stdin.readline 

n = int(input())

for _ in range(n):
    print(check(input()[:-1], 0))
    
    