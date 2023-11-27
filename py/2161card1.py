n = int(input())

q = [i for i in range(1, n+1)]

while len(q)!= 1:
    print(q.pop(0), end=" ")
    q.append(q.pop(0))

print(q[0])