# list = [1, 2, True]
# list2 = [3, 4, False]
# list3 = list + list2
# print(list)
# print(list2)
# print(list3)

# for i in list3:
#     print(list3[i])
# for i in list3:
# #     print(i)

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(number)
# number[0:2] = [7,6,5,4,3]
# print(number)
# number[1] = [0, 1, 2, 3]
# print(number)

# number[3] = ''
# number[6:7] = []#한 객체만 슬라이싱 하면 del과 같은 역할
# del number[1]

# print(number)
# number[0:2] = []#두 객체 이상을 슬라이싱 하면 인덱싱과 같은 역할
# print(number)numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
# numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
# print(numbers)

# numbers.insert(3, [11, 12, 13])
# print(numbers)

# #append와 extend의 차이
# numbers.extend(['a', 'b', 'c'])
# print(numbers)
# numbers.append(['a', 'b', 'c'])
# print(numbers)
dic1 ={"apple":"사과", "banana":"바나나", "strawberry":"딸기"}
dic2 ={"apple":"사과", "banana":"사과", "strawberry":"딸기"} #중복인value, key 값은 하나로 취급 
dic3 ={"apple":"사과", "banana":"사과", "apple":"딸기"} #key 값이 중복이어도 에러가 나진 않음, 하지만 가장 뒤에 선언된 key값을 반환
print(dic1["apple"])
print(dic3["apple"])
list = dic1.keys()
print(list)
list2 = dic3.keys()
print(list2)