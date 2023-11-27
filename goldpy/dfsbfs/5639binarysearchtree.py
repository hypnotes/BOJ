import sys 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline 
li = []
while True:
    try:
        li.append(int(input()))
    except:
        break

def iterate(a, b):
    if a > b:
        return
    breakpoint = b + 1
    for i in range(a+1, b+1):
        if li[a] < li[i]:
            breakpoint = i
            break 
    iterate(a+1, breakpoint-1)
    iterate(breakpoint, b)
    print(li[a])

iterate(0, len(li)-1)