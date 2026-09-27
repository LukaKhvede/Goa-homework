#1

#Class Inheritance არის მექანიზმი, რომლის საშუალებითაც ერთი კლასი იღებს სხვა კლასის თვისებებსა და მეთოდებს.

#2

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


manager1 = Manager("Luka", 3000, "IT")

print(manager1.name)
print(manager1.salary)
print(manager1.department)


#3

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Admin(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role


admin1 = Admin("Luka123", "luka@gmail.com", "Admin")

print(admin1.username)
print(admin1.email)
print(admin1.role)

#4

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


book1 = EBook("Harry Potter", "J.K. Rowling", 25)

print(book1.title)
print(book1.author)
print(book1.file_size)

#5

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        print(self.salary)


class Manager(Employee):
    def bonus_salary(self):
        self.salary = self.salary * 1.20
        print(self.salary)


manager1 = Manager("Luka", 3000)

manager1.get_salary()
manager1.bonus_salary()

#6


class Vehicle:
    def __init__(self, brand, year, color, horsePower):
        self.brand = brand
        self.year = year
        self.color = color
        self.horsePower = horsePower

    def drive(self):
        print(self.color, self.brand, "is going")

    def stop(self):
        print(self.color, self.brand, "is stopping")


class Car(Vehicle):
    def honk(self):
        print("Beep beep!")


class Motorcycle(Vehicle):
    def wheelie(self):
        print("Motorcycle is doing a wheelie!")


class Bike(Vehicle):
    def ring_bell(self):
        print("Ring ring!")


car1 = Car("Mercedes", 2015, "Black", 170)

motorcycle1 = Motorcycle("Yamaha", 2022, "Blue", 120)

bike1 = Bike("Trek", 2023, "Red", 0)


car1.drive()
car1.stop()
car1.honk()

motorcycle1.drive()
motorcycle1.stop()
motorcycle1.wheelie()

bike1.drive()
bike1.stop()
bike1.ring_bell()

