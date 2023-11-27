import sys

a = sys.stdin.readline()[:-1]
b = sys.stdin.readline()[:-1]

if len(a) < len(b):
    b, a = a, b

adi = [0] * len(a)

adin = [0] * len(a)
maxcur = 0
for i in range(len(b)):
    adi = [0] * len(a)

    for j in range(len(a)):
        
        if b[i] == a[j] and j:
            adi[j] = adin[j-1] + 1
            maxcur = adi[j] if adi[j] > maxcur else maxcur
        elif b[i] == a[j]:
            adi[j] = 1
        else:
            adi[j] = 0
        
    adin = adi
print(maxcur)