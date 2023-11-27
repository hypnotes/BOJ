import sys
input = sys.stdin.readline
n = int(input())
b = int(input())

def check(num):
    for i in range(len(num)):
        if broken[int(num[i])]:
            return 0
    return 1

if n==100:
    li = list(map(int, input().split()))
    print(0)
else:
    li = list(map(int, input().split()))        
    broken = [0] * 10
    for i in li:
        broken[i] = 1

    a = abs(n-100)

    for i in range(1000000):
        if check(str(i)):
            a = min(a, len(str(i))+abs(n-i))
    print(a)
    
