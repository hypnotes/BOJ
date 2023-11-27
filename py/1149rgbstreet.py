n = int(input())

houses = []

past = []
for i in range(n):
    
    l = list(map(int, input().split()))
    
    if i:
        l[0] = min(past[1], past[2]) + l[0]
        l[1] = min(past[0], past[2]) + l[1]
        l[2] = min(past[0], past[1]) + l[2]
    
    past = l

print(min(past))
    