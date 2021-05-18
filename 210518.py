# t1 = ('a', 'b', 'con')
# print(t1)
# t1 = ('a', 'b', 'c', 1, 2, 3)
# print(t1, t1[2])

# t2 = ("hello") #하나의 값이면 뒤에 콤마 입력
# print(t2)

# t3 = "goorm", 'b', "hello", 1, 2, 3 #괄호 생략 가능
# print(t3, t3[2])

# s1 = list(set([1,2,3])) #다음에 배우게 될 집합 Mutable 타입
# t4 = ([1, 2, 3], {"사과":"apple", "포도":"grape"}, ('a', 'b', 'c'), s1) #리스트 내 어떤 값도 가능
# print(t4, t4[1])

# t4[3][2] = "edit" #중요: 튜플 요소가 Mutable하면 수정할 수 있음
# t4[1]["사과"] = "edit"
# t4[0][2] = "edit"
# # print(t4)
# s1 = {3, 2, 5, 1, 8, 4, 3} #집합으로 바로 선언 및 초기화
# print(s1, type(s1))
# str = "Hello goorm!!!"
# print(str, type(str))

# s0 = set(str) 
# print(s0, type(s0))

# l = ['a', 'a', 'c', "goorm", "hello", 10, 30, 30]
# print(l, type(l))

# s1 = set(l) 
# print(s1, type(s1))

# d = {"Anna":25, "Bob": 23}
# print(d, type(d))

# s2 = set(d)
# print(s2, type(s2))

# t = (190,)
# print(t, type(t))

# s3 = set(t)
# print(s3, type(s3))
# s1 = set([2,4,6,8,10]) 
# s2 = set([1,2,3,4,5,6,7,8])

# interset = s1 & s2 #교집합
# print(interset)
# print(s1.intersection(s2), s2.intersection(s1)) #함수 사용
# print(s1) #s1의 값이 바뀌는 것이 아님

# uniset = s1 | s2 #합집합
# print(uniset)
# print(s1.union(s2)) 
# print(s1) #s1의 값이 바뀌는 것이 아님

# difset1 = s1 - s2 #어떤 집합에서 어떤 집합을 빼느냐에 따라 다른 결괏값
# difset2 = s2 - s1
# print(difset1)
# print(difset2)
# dic = {"human":"사람", "dog" : "강아지", "carrot" : "당근"}

# oddnums = (1, 3, 5, 7, 9)
# evennums = [6, 8, 10, 22, 50]
# str = "Hello goorm!"

# for i in oddnums :
#     print(i, end = ' ')
# print()
    
# for i in evennums :
#     print(i, end = ' ')
# print()

# for i in str :
#     print(i , end = ' ')
# print()

# for ke, val in dic.items() :
#     print(ke, val, end = ' ')
# print()
# fruits = {"apple" : "red", "banana" : "yellow", "grape" : "purple", "melon" : "green"}

# for color in fruits.values():
#     print(color, end = ' ')
# print()

# for fruit in fruits.keys():
#     print(fruit, end = ' ')
# print()

# for fruit, color in fruits.items():
#     print("%s의 색은 %s" %(fruit, color), end = ', ')