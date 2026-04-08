#1
def misalmeba(name):
    return f"Hello {name}"
print(misalmeba(input("enter your name: ")))
#2

# შექმენით ფუნქცია,
#  რომელიც პარამეტრად მიიღებს ორ რიცხვს და დააბრუნებს მათ ჯამს
def jami(num1,num2):
    return num1+num2
number=int(input("enter num1: "))
number_=int(input("enter num2: "))
print(jami(number,number_))
#davaleba3
def luwia(num4):
    if num4%2 ==0:
        return "luwia"
    else:
        return "kentia"
number4=int(input("enter num:"))
print(luwia(number4))
#davaleba4
def xarisxi(x,y):
    return x**y
xx=int(input("enter x: "))
yy=int(input("enter y: "))
print(xarisxi(xx,yy))
#davaleba5
def sigrdze(sityva):
    return len(sityva)
sityvaa=input("enter sityva: ")
print(sigrdze(sityvaa))
#davaleba6
