n = int(input())

di = { i : 0 for i in range(10) }

for i in range(1, n+1):
    ri = str(i)
    for j in range(len(ri)):
        di[int(ri[j])] += 1

for i in di.values():
    print(i, end = " ")