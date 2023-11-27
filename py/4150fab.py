n = int(input()) -1

a, b = 1 , 1

for i in range(n):
    a, b = b, a+b

print(a)

