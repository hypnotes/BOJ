n = int(input())

li = [ [1] * 9]
onezero = [1, 1]

for i in range(n-1):
    newline = [0] * 9
    
    for j in range(9):
        if j == 0:  #1
            newline[j] = onezero[-2] + li[0][1]   #0, 2
            onezero.append(newline[j])
        elif j == 8:
            newline[j] = li[0][j-1]
        else:
            newline[j] = li[0][j-1] + li[0][j+1]
    del li[0]
    li.append(newline)

print(sum(li[0])%1000000000)
