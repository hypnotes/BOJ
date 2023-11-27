
n = int(input())

l = list(map(int, input().split()))

li = list(sorted(set(l)))

c = [i for i in range(len(li))]
di = dict(zip(li, c))

for i in l:
    print(di[i], end=" ")