# ex01_while.py

# while조건문
#   수행 할 문장

treeHit = 0
while treeHit < 10:
    print("나무를 %d번 찍었습니다." %treeHit)
    treeHit += 1
    
number = 0
while number != 4 :
    print("4가 아닙니다.")
    number = int(input())
    
fruits = ["사과","오렌지"]
fruits.append("딸기")
fruits.insert(1,"수박")
print(fruits)

# while문을 사용하여 1~10까지 숫자중 홀수만 리스트에 넣어주세요
numlist = []
wnumber = 1
while wnumber <= 10:
    if wnumber % 2 == 1:
        numlist.append(wnumber)
    wnumber+=1
print(numlist)