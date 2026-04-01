# #davaleba1
# num1=float(input("enter your number: "))
# num2=float(input("enter your number: "))
# num3=float(input("enter your number: "))
# num4=float(input("enter your number: "))
# num5=float(input("enter your number: "))
# numbers=[num1,num2,num3,num4,num5]
# print(sum(numbers)/5)
# #davaleba2

# semtence=input("enter any sentence: ")
# print(len(semtence))
# #davaleba3
# password=input("enter your password: ")

# if password.find("1") != -1:
#     print("პაროლი შეიცავს '1'-ს")
# else:
#     print("პაროლი არ შეიცავს '1'-ს")

    #davaleba4

fruits=["banana","apple","strawberry","pinaple"]
fruits.append("cherry")
fruits.pop(3)
fruits.insert(3,"blueberry")
print(fruits)
#davaleba5
word=input("enter word: ")
if word[0]==word[0].upper():
    print("Perfect")
else:
    print("Your word should be capitalized!")

#davaleba6
first_name = input("შეიყვანეთ სახელი: ")
last_name = input("შეიყვანეთ გვარი: ")

print("Uppercase:", first_name.upper(), last_name.upper())
print("Lowercase:", first_name.lower(), last_name.lower())

#davaleba7
myname="luka"
yourname=input("enter yourname: ")
if myname==yourname.lower():
    print("our names are similar!")
else:
    print("We have different names")
#davaleba8
gg="hidroeleqtrosadguri"
print(gg.find("e"))
#davaleba9
# lists=["luka","giorgi","nika","andria"]
# for i in lists:
#     lists[i]==lists[i].capitalize()
# print(lists)
#davaleba10
sia=[]
sia1=input("enter word:")
sia2=input("enter word:")
sia3=input("enter word:")
sia.append(sia1)
sia.append(sia2)
sia.append(sia3)
print(sia)
#davaleba11
fruits1=["apple","pinapple","durian","strawberry"]
fruit=input("enter your fruit: ")
fruits1.insert(2,fruit)
print(fruits1)