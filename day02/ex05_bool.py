# True, False만 나타내는 자료형
# 자료형의 참과 거짓 구분하기
# 문자열 --> 빈문자열 : 거짓, "a" : 참
# 리스트, 딕셔너리, 튜플 --> 비어져있으면 : 거짓,
# 요소가 았으면 참
# 숫자 0이 아닌 숫자 : 참 , 0 : 거짓
# None : 거짓
# 문자열, 리스트, 딕셔너리, 튜플 값이 비어있으면 거짓
# bool(value) --> 불타입으로 변환
print(bool(0)) #False
print(bool(-1)) #True
print(bool("")) #False
print(bool(" ")) #True
print(bool("aaa")) #True
print(bool([])) #False
print(bool({})) #False
print(bool(())) #False
