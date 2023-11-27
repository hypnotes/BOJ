n, k = map(int, input().split())

li = []
for i in range(2, n+1):
    li.append(i)
    
count = 0
retval = 0
while True:
    delval = li[0]
    for i in li:
        if i%delval == 0:
            count+=1
            retval = i
            li.remove(i)
        if count == k:
            break
    if count == k:
        break
        
print(retval)