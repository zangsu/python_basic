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
def pb6(stone):
    white = 0
    black = 0
    for line in stone:
        for j in line:
            if j == 1:
                black += 1
            elif j == 2:
                white += 1
    print(f"흑돌의 개수 : {black}\n백돌의 개수 : {white}")
    return black, white
def pb7(stone):
    for line in stone:
        for i in line:
            if i == 0:
                print("x ",end="")
            elif i == 1:
                print("○ ",end="")
            elif i == 2:
                print("● ",end="")
        print("\n")

stone = [[0,0,0,0,0,0,0,0,0],[0,1,0,1,2,1,2,1,0],[0,2,1,1,1,2,2,0,0],[0,0,2,2,2,1,0,2,0],[0,0,0,0,0,1,0,2,1],[0,0,0,2,0,1,2,1,0],[0,0,0,2,1,0,1,1,0],[0,0,0,1,1,0,0,0,0],[0,0,0,0,2,2,2,0,0]]
pb7(stone)