from random import randint

def crerand(i, rand):
    if i == 0:
        rand = [randint(1, 45)]
        return rand
    else:
        j = 0
        new = randint(1, 45)
        while j < i:     
            if new == rand[j]:
                break
            j+= 1
            

        if j == i:
            rand.append(new)  
            return rand
        else:
            return crerand(i, rand)
def sort(rand):
    for number in range(6):
        smallest = number
        for list in range(number, 6):
            if rand[smallest] > rand[list]:
                smallest = list
        if smallest == number:
            continue
        else:
            temp = rand[smallest]
            rand[smallest] = rand[number]
            rand[number] = temp
    return rand

def pb2_1():
    print("**로또 번호 생성을 시작합니다.")
    num = int(input("몇 번을 뽑을까요? "))
    
    rand = [0]
    for a in range(num):
        for k in range(6):
            rand = crerand(k, rand)
        rand = sort(rand)
        print("auto number --> ",end="")
        for index in rand:
            print(index, end=" ")
        print()
def pb2_2():
    line = []
    line.append("나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리우리다")
    line.append("양변에 약산 진달래꽃 아름 따다 가실 길에 뿌리우리다")
    line.append("가시는 걸음 걸음 놓인 그 꽃을 사뿐히 즈려밟고 가시옵소서")
    line.append("나 보기가 역겨워 가실 때에는 죽어도 아니 눈물 흘리우리다")

    string = ""
    
    for lines in line:
        string += lines
    string = string.replace(" ", "")
    for ch in string:
        cnt = string.count(ch)
        if cnt >= 4:
            print(f"{ch}-->{cnt}")
        string = string.replace(ch, "")
pb2_2()