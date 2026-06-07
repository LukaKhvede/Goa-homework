# 2
# Tuple Unpacking არის პროცესი, როდესაც Tuple-ის ელემენტები ცალკეულ ცვლადებში ინახება.

# მაგალითი 1 (Asterisk-ის გარეშე)
person = ("Luka", 16, "Student")
name, age, status = person

# მაგალითი 2 (Asterisk-ის გარეშე)
numbers = (10, 20, 30)
a, b, c = numbers

# მაგალითი 3 (Asterisk-ის გამოყენებით)
values = (1, 2, 3, 4, 5)
first, *rest = values


# 3) Tuple-ებზე ხელმისაწვდომი მეთოდები/ფუნქციები

# მეთოდები:
# count()
# index()

# ფუნქციები:
# len()
# max()
# min()
# sum()
# tuple()
# sorted()
# any()
# all()


# 4) Tuple-ებზე არ არის ხელმისაწვდომი შემდეგი List მეთოდები

# append()
# extend()
# insert()
# remove()
# pop()
# clear()
# sort()
# reverse()


# 5

info = ("Luka", "Khvedelidze", 16, "Nutsubidze", "26 April")

name, surname, age, address, birthday = info

print(name)
print(surname)
print(age)
print(address)
print(birthday)


# 6

numbers = (10, 2.5, 7, 3.14, 8.9, 15)

num1, *rest = numbers

print("num1 =", num1)
print("rest =", rest)


# 7

fruits = ('Apple', 'Pomegranate', 'Cherry', 'Strawberry', 'Blueberry')
*fruit1, fruit2, fruit3 = fruits

# fruit1 = ['Apple', 'Pomegranate', 'Cherry']
# fruit2 = 'Strawberry'
# fruit3 = 'Blueberry'

print(fruit1)
print(fruit2)
print(fruit3)