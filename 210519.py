# l = [10, 20, 30, 'a', 'b', 'c', "hello"]

# if 20 in l :
#     print("요소가 존재합니다.")
# else :
#     print("요소가 존재하지 않습니다.")
    
# if "Hello" not in l :
#     print("요소가 존재하지 않습니다")
# else :
#     print("요소가 존재합니다.")
sum = 0
while 1:
    a = int(input('숫자를 입력하세요'))
    if a == 0:
        break
    elif a < 10:
        sum += a
    else:
        continue
print(sum) #조건, 반복문에서 배운 모든 구문 집합체