#davaleba1
num1=int(input("enter yout number: "))
if num1%2==0:
    print("your number is even")
else:
    print("your number is odd")


# #davaleba2
temp=float(input("enter your temperature: "))
if temp>30:
    print("it's hot")
elif temp>15 and temp<=30:
    print("it's warm")
else:
    print("it's cold")
#davaleba3

num2=int(input("enter your number: "))
if num2>=0 and num2%2==0:
    print("positive even")
elif num2>=0 and num2%2!=0:
    print("Positive odd")
else:
    print("Negative")

#davaleba4
num3=int(input("enter your number: "))
for i in range(0,num3,2):
    print(i)
#kentebistvis
num4=int(input("enter your number: "))
for i in range(1,num4,2):
    print(i)

#davaleba5

numse=[]
for n in range(10):
    num7=int(input("enter number: "))
numse=numse+[num7]
for i in numse:
    if i>0:
        print(f"{i} aris dadebitia")
    elif i<0:
        print(f"{i} aris uaryofiti")
    else:
        print(f"{i} aris nuli")

#davaleba6
fruits = ["apple", "banana", "orange", "grape"]
fruits[1]="kiwi"
print(fruits)
#davaleba7
nums1 = [4, 8, 12, 16, 20]
jami=nums1[0]+nums1[-1]
print(jami)
#davaleba8
lists=["fortoxali","wyali","kokakola","borjomi"]
print(lists)
#davaleba9
numlist = [1,2,3,4,5,6,7,8,9,0,10,11,12]
for i in numlist:
    if i%2==0:
        print(i)
#davaleba10
total=0
numlist = [1,2,3,4,5,6,7,8,9,0,10,11,12]
for i in numlist:
    if i%2==0:
        total=total+i
print(total)
#davaleba11
numlist = [1,2,3,4,5,6,7,8,9,0,10,11,12]
for i in numlist:
    if i>6:
        print(i)
#davaleba12
word=input("input any word: ")
for i in word:
    print(i)
#davaleba13
sia=[12,"group96",17,"bmw","Goa",19]
print(sia[0],sia[1],sia[2])