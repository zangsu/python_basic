def pb1():
    i = 0
    while i<4:
        print("* * * * * * * * * *")
        i+= 1
def pb2():
    num = int(input("N 값을 입력하세요 : "))
    print(f"N의 값 : {num}")
    result = 0
    i = 1
    while i<=num:
        p = pow(2*i, 2*i - 1)
        result = result + p
        i+= 1
    print(f"합계 : {result}")
def pb3():
    print()

pb2()