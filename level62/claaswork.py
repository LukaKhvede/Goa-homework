class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade=grade

Student1=Student("luka",16,11)
print(Student1.name)
print(Student1.age)
print(Student1.grade)
#2
