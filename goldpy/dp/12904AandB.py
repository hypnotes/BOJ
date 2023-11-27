s = input()
t = input()
slen = len(s)

while True:
    if s == t:
        print(1)
        break
    if slen == len(t):
        print(0)
        break
    if t[-1] == 'A':
        t = t[:-1] 
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
