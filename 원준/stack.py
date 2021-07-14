top = -1
def stack1():
    path = ['주황', '초록', '파랑', '보라', '빨강', '노랑']
    top = len(path)-1
    print('과자집에 가는길 : ', end="")
    for i in range(top+1):
        print(f"{path[i]} --> ", end ="")
    print('과자집')
    for i in range(top):
        print(f"{path[top-1]} -->", end="")
        path = pop(path, top)
        #vsc작동 문제! 오류 찾아내기
def push(list, top, data):
    list.append(data)
    top += 1
    return list
def pop(list, top):
    print(list[top])
    top -= 1
    del list[top]
    return list

stack1()