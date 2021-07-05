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
def addmail(list, name, Email):#이메일 사전순으로 정렬
    now = list
    while now.next != None:
        now = now.next
    now.next = Mail(name, Email)
    return list
list3()