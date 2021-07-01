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
def pb8(stone):
    k = 0
    j = 0
    for line in stone:
        if k == 0:
            print("  ", end="")
            for k in range(9):
                print(f"0{k} ", end="")
            k = 1
            print("\n")
        else:        
            print(f"0{k} ", end="")
            k+=1
            for i in line:
                if i == 0:
                    print("x  ",end="")
                elif i == 1:
                    print("○  ",end="")
                elif i == 2:
                    print("●  ",end="")
            print("\n")
def pb9(stone):
    a = 1
    b = 1
    while(1):
        a = int(input("X축 좌표값을 입력하세요"))
        if a == -1:
            print("We are Done!")
            return
        b = int(input("Y축 좌표값을 입력하세요"))
        if stone[b-1][a-1] == 0:
            print(f"돌 없음")
        elif stone[b-1][a-1] == 1:
            print(f"흑돌")
        else:
            print(f"백돌")
def pb4_7():   
    while 1:
        pw = input("password : ")
        checkpw = input("check password : ")        
        det = 0
        if len(pw) < 10:
            print("Wrong password!")
            continue
        for i in pw:
            if i>='A' and i<='Z':
                det = 1
        if det == 0:
            print("Wrong password!")
            continue
        if pw != checkpw:
            print("password and check password are not same!")
            continue
        else:
            print("We are done!")
            return
def pb4_8():
    print()
stone = [[0,0,0,0,0,0,0,0,0],[0,1,0,1,2,1,2,1,0],[0,2,1,1,1,2,2,0,0],[0,0,2,2,2,1,0,2,0],[0,0,0,0,0,1,0,2,1],[0,0,0,2,0,1,2,1,0],[0,0,0,2,1,0,1,1,0],[0,0,0,1,1,0,0,0,0],[0,0,0,0,2,2,2,0,0]]
pb4_7()