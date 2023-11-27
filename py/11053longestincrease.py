#https://velog.io/@hozero/BOJ-11053%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4
# velog님의 블로그 참고

n = int(input())

a = list(map(int, input().split()))
temp = [1] * n  #저장할 리스트 생성

for i in range(1, n):
    for j in range(0, i):   #크기 저장해둔 리스트 순환
        if a[i] > a[j]:
            temp[i] = max(temp[i], temp[j]+1)   #새 크기 저장

print(max(temp)) 