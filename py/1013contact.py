import re
n = int(input())

for _ in range(n):
    m = re.fullmatch('(100+1+|01)+', input())
    print('YES') if m else print("NO")