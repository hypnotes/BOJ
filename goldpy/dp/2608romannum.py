rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}

arabic = [[1, 'I'], [5, 'V'], [10, 'X'], [50, 'L'], [100, 'C'], [500, 'D'], [1000, 'M'] ]

def romeToNum(rn):
    num = 0
    while rn:
        if len(rn) > 1 and rome[rn[0]] < rome[rn[1]]:
            num+= rome[rn[1]]-rome[rn[0]]
            rn=rn[2:]
        else:
            num += rome[rn[0]]
            rn = rn[1:]
    return num

def numTORome(num):
    rn = ''
    index = 6
    while num:
        letter = arabic[index][1]
        first = str(num)[0]
        while num < arabic[index][0]:
            index-=1
            letter = arabic[index][1]
        if first == '4' or first == '9':
            if first == '4':
                letter = arabic[index][1]+arabic[index+1][1]
                num -= (arabic[index+1][0]-arabic[index][0])
            else:
                letter = arabic[index-1][1]+arabic[index+1][1]
                num -= (arabic[index+1][0]-arabic[index-1][0])
            rn += letter 
        else:
            rn += letter * (num//arabic[index][0])
            num -= arabic[index][0] * (num//arabic[index][0])
    return rn

a = input()
b = input()
num = romeToNum(a)+romeToNum(b)
print(num)
print(numTORome(num))

    