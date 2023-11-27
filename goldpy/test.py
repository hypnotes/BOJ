all = 0
small = 101

for i in range(7):
    a = int(input())
if a%2==1:
        all+=a
        small = min(small, a)

if all:
    print(all)
    print(small)
else:
    print(-1)    
