n = int(input())

li = []
di = {}

for _ in range(n):
    a = int(input())
    li.append(a)
    if a in di.keys():
        di[a] += 1
    else:
        di[a] = 1
    
li.sort()
sortedkeys = sorted(di)
newdi = {}
for i in sortedkeys:
    newdi[i] = di[i]
    
di = sorted(newdi.items(), key=lambda x: x[1], reverse=True)
      
#산술평균
print(round(sum(li)/len(li)))

#중앙값
print(li[len(li)//2])

#최빈값
if len(di) > 1 and di[0][1] == di[1][1]:    #최빈값 2개 이상
    print(di[1][0])
else:
    print(di[0][0])

#범위
start, end = li[0], li[-1]
if start < 0 and end < 0:
    print(abs(start)-abs(end))
elif start < 0:
    print(abs(start)+end)
else:
    print(end-start)