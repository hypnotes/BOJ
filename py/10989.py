n = int(input())

li = [0] * 10001
for i in range(n):
    a = int(input())
    li[a]+=1

for i in range(len(li)):
    
    if li[i]:
        for j in range(0, li[i]):
            print(i)

#실패임