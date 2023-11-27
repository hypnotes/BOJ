import sys
n = int(sys.stdin.readline())

q = []

def consecutive(l, c):

    l = l.replace(" ", "")
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    temp = ''
    for i in range(len(l)):
        if l[i] in vowels:
            temp += '1'
        else:
            temp += '0'
    print(l)
    print(temp)

            
for _ in range(n):
    if len(q) == 10:
        q.pop(0)
        
    l = sys.stdin.readline()
    consecutive(l.lower(), 5)
    #change l to lower
    
    
    #append when 'l' passed
