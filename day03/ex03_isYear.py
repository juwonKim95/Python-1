# ex03_isYear.py
# 년도를 입력받아 윤년인지 평년인지 출력하세요
# 4로 나누어 떨어지면 윤년
# 그 중 100으로 나누어 떨어지면 평년
# 그 중 400으로 나누어 떨어지면 윤년

year = int(input("년도를 입력하세요 :"))
if year % 4 == 0:
    if year % 100 == 0:
        yearText = "평년"
        # print("평년입니다.")
        if year % 400 == 0:
            print("윤년입니다.")
        yearText = "윤년" if year % 400 == 0 else "평년"
    else :
        yearText = "평년"
        # print("윤년입니다.")
else :
    yearText = "평년"
    # print("평년입니다.")
print(yearText)