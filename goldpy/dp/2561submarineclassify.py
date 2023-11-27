import re
a = input()
b = re.compile('(100+1+|01)+')
c = "SUBMARINE" if b.fullmatch(a) else "NOISE"
print(c)