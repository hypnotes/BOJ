n = int(input())

li = []
for i in range(n):
    a, b = map(int, input().split())
    li.append((b, a))   #(종료시간, 시작시간)

#Sort by ending time
li.sort()   #종료시간순으로 정렬

endtime = li[0][0]  #가장 최근 종료시간
count = 1
for i in range(1,len(li)):
    if li[i][0] >= endtime and li[i][1] >= endtime:   #
        endtime = li[i][0]  #new 종료시간
        count+=1

print(count)