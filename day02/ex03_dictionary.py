# 딕셔너리 자료형
# 리스트나 튜플처럼 순차적으로 요솟값을 구하지 않고
# key를 통해 value에 접근한다.
# {key1: value1, key2: value2, key3: value3}
# key는 중복안됨
dic = {'name':'green','phone':'01012341234','age':30}
dic2 = {1:"a",2:"b",3:"c"}
# 속성 추가하기
dic["isJob"] = True
print(dic)
# value 값 접근
print(dic['name'])
# 요소 삭제하기
del dic['phone']
print(dic)
dic2[4] = "d"
print(dic2)
dic3 = { 'name': "G", 'age':30, 'name':"b"}
print(dic3)

# key리스트 만들기
dic3key = dic3.keys()
print(type(dic3key))
# 리스트 타입으로 변환 list()
dic3keylist = list(dic3key)
print(dic3keylist)
# value리스트 만들기 values()
dic3value = dic3.values()
print(list(dic3value))
# key.value 쌍 얻기 items()
dic3item = dic3.items()
print(dic3item)
print(list(dic3item))
# key.value 쌍 모두 지우기 clear()
dic3.clear()
print(dic3)
# key로 value값 얻기 get(key)
# 없는 key로 호출시 None반환
# 디폴트 지정하기 get(key,default값)
dic4 = {'name':'구름','age':3, 'color':'white'}
print(dic4.get('name'))
print(dic4.get('age'))
print(dic4.get('a'))
# 대괄호로 하면 에러가 발생한다!
# print(dic4.get['a'])
# 해당 key가 있는지 in  key in 딕셔너리
print('name' in dic4)
print('a' in dic4)