# def subNum(*t):
#     print(t, type(t))
#     total = 0
    
#     for i in t:
#         total += i
       
#     return total

# print(subNum(1,2,3,4,5))
# print(subNum(3,4,9))

# def ch(**key):
#     cal = input('"+"와 "-"중 하나를 입력하세요')
#     a= input('숫자 두개를 입력하세요')
#     if(key[cal]=="+"):
#         return a+a
#     elif(key[cal=="-"]):
#         return a-a
#     else:
#         return 0


# reslut = ch( one ='+', two ='-')
# print(reslut)
# def calculator(a, b) :
#     sum = a + b
#     sub = a - b
#     mul = a * b
#     div = a / b
#     return sum, sub, mul, div

# reslist = calculator(10, 2)
# print(reslist, type(reslist))
# def func(a) :
#     return a + 1

# nums = [1,2,3,4,5]	# 집합인자(튜플, 리스트, 문자열) 모두 가능
# nums = list(map(func, nums)) # map(함수, 집합인자, ..) 형태
# print(nums)
f = open('input.txt', 'r')
while 1:
    line = f.readline()
    if not line:
        break
    print(line)
f.close() #한글은 못 읽나 봄