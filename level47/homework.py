info= lambda name, surname, age : f"Name: {name}, Surname: {surname}, Age: {age}"
print(info("Luka", "Khvedelidze", 16))

#meore
def average(numbers):
    return lambda: sum(numbers) / len(numbers)


print(average([10, 20, 30, 40])())
#mesame
def is_palindrome(string):
    return lambda: string == string[::-1]
#2jer imitom weria : rom def funqcia ushvebs lamda funqcias  

print(is_palindrome("level")())
print(is_palindrome("hello")())
#meotxe

def check_number(number):
    return lambda: "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
#tu ricxvi metia 0ze positive sxva shemtxvevashi tu ricxvi naklebia 0ze negative sxvashemtxvevashi 0

print(check_number(10)())
print(check_number(-5)())
print(check_number(0)())
#mexute
def multiply_by_two(numbers):
    return lambda: list(map(lambda number: number * 2, numbers))#list listad aqcevs map is shedegs da map miwvdeba yvela elements


print(multiply_by_two([1, 2, 3, 4])())
#meeqvse
def longer_than_five(strings):
    return lambda: [x for x in strings if len(x) > 5]


print(longer_than_five(["Hello", "Python", "World", "Programming"])())
#meshvide
def negative_numbers(numbers):
    return lambda: [x for x in numbers if x < 0]


print(negative_numbers([10, -5, 3, -8, 0, -2])())