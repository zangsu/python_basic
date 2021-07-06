from random import *
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
list4()