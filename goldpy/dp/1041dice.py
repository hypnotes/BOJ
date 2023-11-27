import sys 

input = sys.stdin.readline 

n = int(input())
tot = n*n*n
flag = 1 if n != 1 else 0
li = list(map(int, input().split()))

ab, ae, fb, fe = li[0]+li[1], li[0]+li[4], li[5]+li[1], li[5]+li[4]
threeli = [ab+li[2], ab+li[3], ae+li[2], ae+li[3], fb+li[2], fb+li[3], fe+li[2], fe+li[3]] 

twoli = []

for i in range(6):
    for j in range(i+1, 6):
        if i+j != 5:
            twoli.append(li[i]+li[j])

if flag: 
    three = 4 
    two = (2*(2*(n-1)+(n-2))+2*(n-2)) 
    zero = (n-1)*(n-2)*(n-2)
    one = tot-three-two-zero 
    print(three*min(threeli)+two*min(twoli)+one*min(li))
else: 
    print(sum(li)-max(li))