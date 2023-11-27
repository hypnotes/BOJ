import re

a = input()
b = input()

ans = re.sub(r'[0-9]+', '', a)

print(int(b in ans))
             

