class Student:
    total_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1


student1 = Student("Giorgi", 16)
student2 = Student("Nika", 17)
student3 = Student("Luka", 16)

print(Student.total_students)  

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def from_string(cls, text):
        title, author, year = text.split(" - ")
        return cls(title, author, int(year))


book1 = Book.from_string("1984 - George Orwell - 1949")

print(book1.title)
print(book1.author)
print(book1.year)

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)


temp1 = Temperature.from_fahrenheit(98.6)

print(temp1.celsius)

class Product:
    discount_rate = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def set_discount_rate(cls, new_rate):
        cls.discount_rate = new_rate

    def get_discounted_price(self):
        return self.price * (1 - self.discount_rate)


product1 = Product("Laptop", 2000)
product2 = Product("Phone", 1000)

Product.set_discount_rate(0.20)

print(product1.get_discounted_price())  # 1600.0
print(product2.get_discounted_price())  # 800.0

class MathUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def factorial(n):
        result = 1

        for i in range(1, n + 1):
            result *= i

        return result


print(MathUtils.is_even(4))  # True
print(MathUtils.is_even(7))  # False

print(MathUtils.factorial(5))  # 120

class Validator:
    @staticmethod
    def is_valid_email(email):
        return email != "" and "@" in email and "." in email


print(Validator.is_valid_email("test@gmail.com"))  # True
print(Validator.is_valid_email("testgmailcom"))    # False
print(Validator.is_valid_email(""))                # False

class DateHelper:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


print(DateHelper.is_leap_year(2024))  # True
print(DateHelper.is_leap_year(2023))  # False
print(DateHelper.is_leap_year(1900))  # False
print(DateHelper.is_leap_year(2000))  # True

class SecurityUtils:
    @staticmethod
    def check_password_strength(password):
        has_letter = False
        has_digit = False

        for char in password:
            if char.isalpha():
                has_letter = True

            if char.isdigit():
                has_digit = True

        if len(password) >= 8 and has_letter and has_digit:
            return "Strong"
        else:
            return "Weak"


print(SecurityUtils.check_password_strength("abc12345"))  # Strong
print(SecurityUtils.check_password_strength("abcdefgh"))  # Weak
print(SecurityUtils.check_password_strength("12345678"))  # Weak
print(SecurityUtils.check_password_strength("abc123"))    # Weak

