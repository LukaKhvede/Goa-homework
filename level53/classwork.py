#2
def say_hello(func):
    def wrapper():
        print("funqcia aq iwyeba")
        func()
        print("funqcia aq mtavrdeba")
    return wrapper

@say_hello
def hello():
    print("hello")

hello()

#3
#?

#4
def start_finish(func1):
    def wrap():
        print("starting")
        func1()
        print("ending")
    return wrap

@start_finish
def hola():
    print("Hola")

hola()

#5

def welcome(func2):
    def wrapper1():
        print("welcome")
        func2()
    return wrapper1

@welcome
def gamarjoba():
    print("hello")

gamarjoba()

#6

def line(func3):
    def wrapper2():
        print("-----------------------")
        func3()
        print("-----------------------")
    return wrapper2

@line
def goa():
    print("Goa")

goa()