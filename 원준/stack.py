def stack1():
    path = ['주황', '초록', '파랑', '보라', '빨강', '노랑']
    top = len(path)-1
    print('과자집에 가는길 : ', end="")
    for i in range(top+1):
        print(f"{path[i]} --> ", end ="")
    print('과자집')
    print('우리집에 가는길 : ', end ="")
    for i in range(top+1):
        print(f"{path[top]} --> ", end="")
        top -=1
    print('우리집')
def push(list, top, data):
    list.append(data)
    top += 1
    return list
def stack2():
    top = -1
    script = []
    script.append('진달래꽃')
    top += 1
    script.append('나 보기가 역겨워')
    top += 1
    script.append('가실 때에는')
    top += 1
    script.append('말없이 고이 보내드리오리다.')
    top += 1

    print('----- 원본 -----')
    for i in range(top+1):
        print(script[i])
    print('----- 거꾸로 처리된 결과-----')
    for i in range(top+1):
        linetop = len(script[top])-1
        for j in range(len(script[top])):
            print(script[top][linetop], end = "")
            linetop -= 1
        top -= 1
        print()
def queue1():
    line = ['정국', '뷔', '지민', '진', '슈가']
    rear = 0
    top = len(line)
    li = []
    print(li[0])
    # while rear != top:
    #     print(top)
    #     print(f"대기 줄 상태 : [ ", end="")
    #     for i in range(top):
    #         print(f"'{line[i]}'", end="")
    #         if i != top:
    #             print(",",end="")
    #     print("]")
    #     print(f"{line[rear]} 님 식당에 들어감")
    #     del line[rear]
queue1()