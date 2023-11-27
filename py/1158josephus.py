from collections import deque

n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])

print("<", end="")
while len(d)!= 1:
    for j in range(k-1):
        d.append(d.popleft())               #k 번째 전 항목들을 일단 pop해서 덱 끝에 push해주기
    print("%d, " % d.popleft(), end='')     #k 번째 항목이 나오면 pop해주고 출력해주기
    
print("%d>" % d.popleft())  #마지막 항목 pop 후 출력

#https://velog.io/@delicate1290/%EB%B0%B1%EC%A4%80-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4-%EB%AC%B8%EC%A0%9C-1158%EB%B2%88
# 이 분 알고리즘 참고했습니다. 
    
# li = [ i for i in range(1, n+1)]

# newli = []
# i = k-1

# while li:
#     if i >= len(li):
#         i %= len(li)
#     newli.append(li[i])
#     print(i+1)
#     del li[i]
#     i+= k-1
    
   
# for i in range(n):
#     if i == 0:
#         print("<%d, " %newli[i], end="" )
#     elif i == n-1:
#         print("%d>" %newli[i], end="" )
#     else:
#         print("%d, " %newli[i], end="")    
