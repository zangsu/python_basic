class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class teacher(people):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
a = teacher("Jang", 24, 3)
print(a.name, a.age, a.grade)