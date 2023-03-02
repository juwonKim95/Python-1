# ex06_if.py
# if 조건문:
#  수행할문장
# else :
#  수행할문장
money = 5000
if money > 10000:
    print("택시타고간다")
else :
    print("걸어간다")
print(10 == 20) #False
print(10 != 20) #True
money2 = 2000
card = True
if money >= 3000 or card :
    print("택시타고간다")
else : 
    print("걸어간다")
    
if not card : 
    print("카드가 없다")
else : 
    print("카드가 있다")
    
# score 값을 입력
# 91~100 "A"
# 81~90 "B"
# 71~80 "C"
# 70이하 "D"
score = int(input("점수를 입력하세요 : "))
if score >= 91 :
    print("A")
elif score >= 81 :
    print("B")
elif score >= 71 :
    print("C")
else : 
    print("D")
    
num1 = int(input("숫자를 입력하세요 : "))
if num1 % 2 == 0 :
    print("짝수입니다.")
else : 
    print("홀수입니다.")
    
# 조건부 표현식
# 참인경우 할당할 값 if 조건문 else 거짓인 경우 할당할 값
result = "짝수" if num1 % 2 == 0 else "홀수"
print(result)

# in / not in 리스트, 튜플 , 문자열
# in 포함하고 있으면 True, 포함하지 않으면 False
print(5 in [1,2,3,4,5])
# not in 포함하고 있지 않으면 True, 포함하고 있으면 False
print(5 not in [1,2,3,4,5])

pocket = ["paper","cellphone","card"]
if "money" in pocket:
    print("택시타고간다")
elif "card" in pocket:
    print("카드로 버스타고 간다")
else : 
    print("걸어간다")
    
#userId -> 아이디 입력, userPW -> 비밀번호 입력
# 아이디 "green" 비밀번호 "1234" 로그인이 되었습니다. 출력
# "green" 이 아닐경우 아이디가 틀렸습니다. 출력
# "1234"가 아닐경우 비밀번호가 틀렸습니다. 출력
 
userId = input("아이디를 입력해주세요 : ")
userPW = input("비밀번호를 입력해주세요 : ")
if userId == "green":
    if userPW == "1234":
        print("로그인이 되었습니다.")
    else :
        print("비밀번호가 틀렸습니다.")
else :
    print("아이디가 틀렸습니다.")
    
if userId == "green" and userPW == "1234":
    print("로그인이 되었습니다.")
elif userId == "green":
    print("비밀번호가 틀렸습니다.")
elif userPW == "1234":
    print("아이디가 틀렸습니다.")
else :
    print("둘 다 틀렸습니다.")