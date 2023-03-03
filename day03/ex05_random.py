# ex05_random.py
# import 모듈 불러오기
import random
# random() 0.0~1.0 사이의 난수 값을 반환
num = random.random()
print(num)
# randint(start,end) start ~ end 정수 랜덤 값을 반환
num2 = random.randint(1,5)
print(num2)

# 01.평균구하기 실습
# [70,60,55,75,85,95,100]
# for문을 사용하여 A학급의 평균 점수를 구해보자.
# len(리스트) ---> 리스트 길이
listA = [70,60,55,75,85,95,100]
total = 0
for i in listA:
    total += i
ave = total / len(listA)
print(ave)

# 02.*출력(별표찍기;)
# *
# **
# ***
# ****
# *****
for i in range(5):
    print("*"*i)
    
# 03.가위바위보 게임 만들기
# 사용자로부터 가위,바위,보 중 하나를 입력받고 
# 가위,바위,보 가 아니면 잘못입력하셨습니다.
# 가위,바위,보를 입력했을때 컴퓨터도 가위,바위,보 중 하나를
# 랜덤으로 지정
# 각각 비교

rps = input("가위,바위,보 중 하나를 입력하세요 : ")
if rps != '가위' and rps != '바위' and rps != '보':
    print("잘못입력하셨습니다.")
else :
    print("%s를 입력하셨습니다." %rps)
    rpsnum = random.randint(1,3)
    comrps = "가위" if rpsnum == 1 else "바위" if rpsnum == 2 else "보"
    print("컴퓨터는 %s를 냈습니다." %comrps)
    if rps == comrps : 
        print('비겼습니다.')
    elif (rps=="가위" and comrps =="보" 
    or rps=="바위" and comrps =="바위"
    or rps=="보" and comrps == "바위"):
        print('당신이 이겼습니다.')
    else :
        print('컴퓨터가 이겼습니다.')
        
# 04.로또번호 출력
# 1~45 ---> 겹치지 않게 랜덤한 숫자로 6개 출력.
# 1~45
lottolist = []
resultlist = []
