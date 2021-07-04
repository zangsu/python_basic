class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class teacher(people):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
#a = teacher("Jang", 24, 3)
#print(a.name, a.age, a.grade)
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class headnode(node):
    def __init__(self, data, next):
        self.data = data
        self.next = next
class middlenode(node):
    def __init__(self, data, pre):        
        self.next = pre.next
        pre.next = self
        self.data = data
a = node(3)
b = node(4)
a.next = b
c = headnode(7, a)
d = middlenode(9, a)

print(c.next.next.data)