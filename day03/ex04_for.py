# ex04_for.py

list1 = ["one","two","three"]
for i in list1:
    print(i)

for i in "green":
    print(i)
    
marks = [90,70,50,87,40]
number = 0
for stu in marks:
    number = number + 1
    if stu >= 70:
        print("%d번 학생은 합격입니다." %number)
    else :
        print("%d번 학생은 불합격입니다." %number)
        
print(list(range(3,10,3)))

# range()함수 range(stop), range(start, stop), range(start,stop, step)
sum = 0
for i in range(1,11,2):
    sum = sum + 1
print('1~10까지 더한 수는 %d이다.' %sum)

# for와 range를 사용해서 구구단 출력
# 2단에서 9단까지 출력
# 2*1=2 2*2=4 2*3=6 ..... 2*9=18
# ...
# 9*1=9 9*2=18 9*3=27 ..... 9*9=81
for i in range(2,10):
    for j in range(1,10):
        print('%d * %d = %d' %(i, j, i*j))
