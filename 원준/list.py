from random import *
from math import *
def list1():
    list=[('다현', 200), ('정연',150), ('쯔위', 90), ('사나', 30), ('지효',15)]
    print(list)
    while 1:
        newname = input("추가할 친구--> ")
        newtimes = int(input("카톡 횟수--> "))
        list = append_frined(list, newname, newtimes)
        print(list)
def append_frined(list, name, times):
    i = 0
    for friend in list:
        if friend[1] <= times:
            break
        i += 1
    list1 = list[:i]
    list2 = list[i:]
    list1.append((name, times))
    list1 = list1 + list2
    return list1
def list2():
    print()
    #뭘 원하는거지?
class pol:
    def __init__(self,t, p ):
        self.t = t
        self.p = p
class Mail:
    def __init__(self, name, Email):
        self.list = [name, Email]
        self.next = None
def list3():
    a = Mail("","")
    while 1:
        name = input("이름--> ")    
        if name == '':
            break
        e_mail = input("이메일--> ")
        if a.list[0] == "":
            a = Mail(name, e_mail)
        else:
            a = addmail(a, name, e_mail)
        printM(a)
def printM(A):
    while A != None:
        print(A.list, end="")
        A = A.next
    print()
def addmail(list, name, Email):#이메일 사전순으로 정렬a
    now = list
    while now.next != None and now.next.list[1]<Email:
        now = now.next
    new =  Mail(name, Email)
    temp = now.next
    now.next = new
    new.next = temp

    return list
class node:
    def __init__(self, num):
        self.num = num
        self.next = None    
def list4():#뽑은 순서대로 라고 해서 그대로 뒀음
    for i in range(6):
        if i == 0:
            a = node(randint(0,46))
        else:
            while(1):
                temp = randint(0,46)
                now = a
                while now.next != None and now.next.num != temp:
                    now = now.next
                if now.next == None:
                    now.next = node(temp)
                    break
                else:
                    continue
    while a != None:
        print(a.num, end=" ")
        a = a.next
def list5():#일단 생성까진 했으ㅁ
    list = []
    for i in range(10):
        list.append(store(chr(ord('A')+i)))
    min = 0
    for i in range(1, 10):
        if list[i].len < list[min].len:
            min = i
    head = headdep(list[min])
    now = head
    del list[min]
    while len(list) != 0:
        min = 0
        for i in range(len(list)):
            if list[i].len < list[min].len:
                min = i
        now.next = dep(head, list[min])
        now = now.next
        del list[min]
    now = now.next
    while 1:
        print(f"{now.data.data[0]} 편의점, 거리 : {now.data.len}")
        now = now.next
        if now == head:
            break
class dep:
    def __init__(self, a, data):
        self.next = a
        self.data = data
class headdep(dep):
    def __init__(self, data):
        self.next = self
        self.data = data
def pow(a, b):
    if b == 1:
        return a
    else:
        return a * pow(a, b-1)
def findlen(store):
     return sqrt(pow(store.data[1],2)+pow(store.data[2],2))
class store:
    def __init__(self, name):
        x = randint(1, 101)
        y= randint(1, 101)
        self.data = (name, x, y)
        self.len = findlen(self)
def list6():
    temp = 0
    a = headnode('다현')
    b = bside('정연', a)
    c = bside('쯔위', b)
    d = bside('사나', c)
    e = bside('지효', d)
    a.prev = e
    e.next = a
    head = a
    print("정방향 --> ", end="")
    while 1:
        print(a.name, end=" ")
        a = a.next
        if a == head:
            break
    print()
    print("역방향 --> ", end="")
    while 1:
        print(a.prev.name, end=" ")
        a = a.prev
        if a == head:
            break
class bside:
    def __init__(self, name, prev):
        self.prev = prev
        self.name = name
        self.next = None
        self.prev.next = self
class headnode(bside):
    def __init__(self, name):
        self.name = name
        self.next = self
        self.prev = self
list1()
