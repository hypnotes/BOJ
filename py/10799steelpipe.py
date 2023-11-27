import sys

n = sys.stdin.readline()
nlen = len(n)

cur = 0
pipe = 0
for i in range(nlen):
    if i != nlen and n[i] == '(' and n[i+1] == ')':
        pipe += cur
    elif n[i] == ')' and n[i-1] == '(':
        pass
    elif n[i] == '(':
        cur += 1
    else:
        cur -= 1
        pipe += 1

print(pipe-1)