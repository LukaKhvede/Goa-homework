# #davaleba1
# def sashualo(numbers):
#     total=0
#     count=0
#     for i in numbers:
#         total=total+i
#         count=count+1

#     if count ==0:
#         return 0
#     else:
#         return total/count

# raodenoba=int(input("sheiyvanet siis komponentebis raodenoba: "))
# nums=[]
# for i in range(raodenoba):
#     num=int(input("enter num: "))
#     nums.append(num)
# print(sashualo(nums))

# #davaleba2
# def luwebis(numbers1):
#     luwebisjami=0
#     luwebisraodenoba=0
#     for i in numbers1:
#         if i%2==0:
#             luwebisjami=luwebisjami+i
#             luwebisraodenoba=luwebisraodenoba+1
#     if luwebisraodenoba==0:
#         print("araris luwebi")
#     else:
#         return luwebisjami/luwebisraodenoba
# raodenoba1=int(input("sheiyvanet siis komponentebis raodenoba: "))
# numss=[]
# for i in range(raodenoba1):
#     num1=int(input("enter num: "))
#     numss.append(num1)
# print(luwebis(numss))
# #davaleba3
# def kentebi(number):
#     kentebisraodenoba=0
#     for i in number:
#         if i%2!=0:
#             kentebisraodenoba=kentebisraodenoba+1
#     return kentebisraodenoba

# ricxvebi=[]
# ricxvebisraodenoba=int(input("enter raodenoba: "))
# for i in range(ricxvebisraodenoba):
#     ricxvi=int(input("sheiyvane ricxvi: "))
#     ricxvebi.append(ricxvi)
# print(kentebi(ricxvebi))
#davaleba4
# def double_values(text):
#     axali_text=[]
#     for i in text:
#         axali_text.append(i)
#         axali_text.append(i)
#     return axali_text
# textisraodenoba=int(input("enter raodenoba: "))
# texts=[]
# for i in range(textisraodenoba):
#     texte=input("enter komponenti: ")
#     texts.append(texte)
# print(double_values(texts))
# #davaleba5
# def akvadrateba(numsss):
#     numss=[]
#     for i in numsss:
#         numss.append(i**2)
#     return numss
# raodenoba=int(input("raodenoba"))
# akva=[]
# for i in range(raodenoba):
#     akvaa=int(input("enter your num: "))
#     akva.append(akvaa)
# print(akvadrateba(akva))
# #davaleba6
# def sum(numberebi):
#     jami=0
#     for i in numberebi:
#         jami=jami+i
#     return jami
# numbere=[]
# for i in range(3):
#     numberi=int(input("enter num: "))
#     numbere.append(numberi)
# print(sum(numbere))
#davaleba7
# def substract(num11,num22):
#     if num11>num22:
#         return num11-num22
#     else:
#         return num22-num11
# num1_=int(input("enter num1: "))
# num2_=int(input("enter num2: "))
# print(substract(num1_,num2_))
# #davaleba8
# def multiply(num3,num4):
#     return num3*num4
# num3_=int(input("enter num:"))
# num4_=int(input("enter num:"))
# print(multiply(num3_,num4_))
# #davaleba9
# def check_age(age1):
#     if age1>=18:
#         return "Access Granted"
#     else:
#         return "Access Denied"
# age=int(input("enter your age"))
# print(check_age(age))
#davaleba10__
# def print_names(names):
#     name=[]
#     for i in names:
#         print(i)
# print_namess=[]
# raodenoba=int(input("enter raodenoba: " ))
# for i in range(raodenoba):
#     saxeli=input("enter name: ")
#     print_namess.append(saxeli)
# print(print_names(print_namess))
#davaleba11
# def odd_or_even(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# num=int(input("enter your num: "))
# print(odd_or_even(num))
#davaleba12
# def student_grade(grade):
#     if grade>100:
#         return "enter valid grade"
#     elif grade<0:
#         return "enter valid grade"
#     elif grade >=90 and grade<=100:
#         return "-A"
#     elif grade >=70 and grade<=89:
#         return "-B"
#     elif grade>=50 and grade<=69:
#         return "-C"
#     else:
#         return "-F"
# grade1=int(input("enter your grade: "))
# print(student_grade(grade1))
#davaleba13
# def user_info(name, surname, age):
#     return f"Hello,i am {name} {surname} , and im {age} years old."
# name_input = input("sheiyvanet saxeli: ")
# surname_input = input("sheiyvanet gvari: ")
# age_input = input("sheiyvanet asaki: ")
# print(user_info(name_input, surname_input, age_input))
#davaleba14__
# def arithmetic_mean(numbers):
#     if len(numbers) == 0:
#         return 0
#     mean = sum(numbers) / len(numbers)
#     return mean
# raodenoba = int(input("ramdeni ricxvis sheyvana gurs? "))
# numberss = []
# for i in range(raodenoba):
#     num = int(input("Enter number: "))
#     numberss.append(num)
# print(arithmetic_mean(numberss))
#davaleba15
# def filter_vowels_fast(text):
#     vowels_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
#     result = ""
#     for i in text:
#         if i in vowels_set:
#             result += i
#     return result
# stri=input("enter string: ")
# print(filter_vowels_fast(stri))
#davaleba16
# def unique_list(lst):
#     result = []  # უნიკალური ელემენტების სია
#     for i in lst:  # გადავუაროთ საწყის სიას
#         found = False
        
#         for j in result:  # შევამოწმოთ უკვე დამატებულებში
#             if i == j:
#                 found = True
        
#         if found == False:  # თუ არ არის სიაში
#             result.append(i)
    
#     return result
# n = int(input("raodenoba: "))
# members = []
# for i in range(n):
#     member = input("enter member: ")
#     members.append(member)
# print(unique_list(members))
#davaleba17
# def manual_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num 
#     return total
# j = int(input("raodenoba: "))
# numbers=[]
# for i in range(j):
#     num=int(input("enter num: "))
#     numbers.append(num)
# print(manual_sum(numbers))
