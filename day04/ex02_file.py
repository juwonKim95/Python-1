# ex08_file.py

f = open("test.txt", "w", encoding="utf-8")
students = ["송혜교","주지훈","강하늘","윤박"]
scores = [90,55,70,85]
for i in range(4):
    data = "%s님은 %s점입니다. \n" %(students[i], scores[i])
    f.write(data)
f.close()
d = open("test.txt", "r", encoding="utf-8")
readData = d.readlines()
for i in readData:
    print(i)
    
d.close()