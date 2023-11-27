n = int(input())

classes = [] #각 줄의 첫번째 수는 총 과목 수 (len 안 쓰게)
for i in range(n):
    temp = list(map(int, input().split()))
    del temp[0]
    classes.append(set(temp))

m = int(input())

for i in range(m):
    ans = 0
    stu = list(map(int, input().split()))
    del stu[0]
    stu = set(stu)
    for j in range(n):
        ans += classes[j].issubset(stu)

    print(ans)
