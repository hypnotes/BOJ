t = int(input())

for _ in range(t):
    n = int(input())
    li = []
    for _ in range(n):
        a = int(input())
        li.append(a)
    k = 1
    pointedperson = li[0]   #1번 -> 2번
    while k!=n and pointedperson!=n:
        pointedperson = li[pointedperson-1]    #2번 -> 3번 ...
        k+=1
    if pointedperson == n:
        print(k)
    else:
        print(0)