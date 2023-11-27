m = [500, 100, 50, 10, 5, 1]

a = int(input())
a = 1000-a
count = 0

for i in m:
    count += a//i
    a -= (a//i)*i
    if a==0:
        break

print(count)
