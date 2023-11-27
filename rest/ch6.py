#Problem 2

def calculateString(myInput):
 
    myDict = {}
    
    for i in range(len(myInput)):
        currentLetter = myInput[i] #그냥 읽기 편하게
        if currentLetter != ' ': #space가 아니라면
            if currentLetter in myDict.keys(): #dictinoary에 이미 있다면 
                myDict[currentLetter] += 1
            else:
                myDict[currentLetter] = 1   #dict에 없으면 새로 count 올리기
                            
    return myDict

#여기부터 main (여기부터 시작함)

myInput = input('Enter string: ')
newDict = calculateString(myInput.lower()) #소문자로 변환된ㄷ걸 보내줌

if newDict: #존재라도 하면
    for letters, count in newDict.items(): #dictionary 순서대로 보는 방법이란다
        print("The letter %s occurs %d times" %(letters, count))
else: #존재마저 안하면ㅋ
    print("No Data!")


# import random
# fp_w = open("200220373_in_num.txt", "w") #open this file 근데 없으면 만들어버리기

# for i in range(1, 16): #1-15 돌기 
#     print("%.2f" %(random.uniform(1.00, 2.00)), file=fp_w, end = ' ') #end 뜻: 배 숫자마다 새로운 줄 만들지 말고 space로만 구분하기
#           #round (---), 2 = 2자리수까지
#     if (i) % 5 == 0 : #만약 5의 배수면 (5번쨰 숫자 후 new line, 10번쨰 후 new line)
#         print("\n", file = fp_w, end="")

# fp_w.close()

# fp_r = open("200220373_in_num.txt", "r") 
# fp_w = open("20220373_out_num.txt", "w")

# print("*********** output file ***********", file=fp_w)

# for i in range(3):
#     currentLine = fp_r.readline()
#     a,b,c,d,e = map(float, currentLine.split()) #5개의 변수에 나눠서 저장 (문자열 형태)
#     total = int(a+b+c+d+e) #int가 round가 아니라 뒤 소숫점 걍 버림
#     print(total, file = fp_w)
#     #LINE 20, 21 합칠 수 있긴 함 : print(int(a+b+c+d+e), file=fp_w ) 이렇게

# fp_r.close()
# fp_w.close()


