def find():
    for i in range(2, n+1):
        li[i] = li[i-1] + li[i-2]
    return li[-1]

n = int(input())


if n < 2:
    print(n)
else:
    li = [0] * (n+1)
    li[0] = 0
    li[1] = 1
    print(find())