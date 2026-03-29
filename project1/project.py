



from turtle import *


speed(3)
color("Green")
pensize(5)


penup()
left(180)
forward(200) 
right(180)
pendown()
forward(50)
right(135)
forward(50)
right(45)
forward(60)
right(45)
forward(50)
right(45)
forward(60)
right(45)
forward(45)
right(45)
forward(70)
right(45)
forward(40)
right(45)
forward(20)
penup()
left(90)
forward(60)
pendown()
left(60)
forward(60)
right(60)
forward(55)
right(60)
forward(60)
right(30)
forward(55)
right(30)
forward(55)
right(60)
forward(62)
right(60)
forward(50)
right(30)
forward(56)
penup()
right(90)
forward(150)
right(90)
forward(100)
pendown()
right(210)
forward(170)
right(120)
forward(170)
penup()
right(120)
forward(165)
right(120)
forward(80)
right(60)
pendown()
forward(80)
hideturtle()
exitonclick()




language = input("აირჩიე ენა (ქართული/ინგლისური) /// Enter a language (Georgian/English): ")

print()

if language == "ქართული" or language == "Georgian":
    print("ხელმისაწვდომი კურსები:\n")
    py="Python Programming"
    wb="Web Development"
    gd="Game Development"
    print(f"1.{py}")
    print("   მოკლე აღწერა: საწყისი პროგრამირება Python-ში")
    print("   სიჩქარე: 1,2,3\n")

    print(f"2.{wb}")
    print("   მოკლე აღწერა: ვებსაიტების შექმნა")
    print("   სიჩქარე: 1,2,3\n")

    print(f"3.{gd}")
    print("   მოკლე აღწერა: თამაშების შექმნა")
    print('speed 1 - კვირაში ერთხელ\nspeed 2 - კვირაში ორჯერ\nspeed 3 - კვირაში სამჯერ\n')
    print("   სიჩქარე: 1,2,3\n")

    # არჩევის ციკლი

    choice = input("აირჩიე კურსი (Python Programming/Web Development/Game Development): ")

    if choice == py:
            print("\nPython Programming")
            print("ვრცელი ინფორმაცია:")
            print("ისწავლი Python-ის საფუძვლებს, ცვლადებს, ციკლებს და ფუნქციებს.")


    elif choice == wb:
            print("\nWeb Development")
            print("ვრცელი ინფორმაცია:")
            print("ისწავლი HTML, CSS და JavaScript-ს.")


    elif choice == gd:
            print("\nGame Development")
            print("ვრცელი ინფორმაცია:")
            print("ისწავლი როგორ შექმნა თამაშები Python-ით.")

    else:
            print("არასწორი არჩევანი, სცადე თავიდან ❌")

    speeds = input('შეიყვანეთ რა სიჩქარით გსურთ სწავლა (1/2/3): ')

    # N3_______________________

    age = int(input("შიყვანეთ თქვენი ასაკი :"))

    while age < 0 or age > 99:
        print("არასწორი ასაკი, შეიყვანეთ სწორი ასაკი")
        age = int(input("შიყვანეთ თქვენი ასაკი :"))

        if age >= 18 and age <=99:
            print("სრულ წლოვანი ხარ")
        elif age < 18:
            print("არასრულწლოვანი ხარ, შეიყვანე მშობლის ინფორმაცია")
            name = input("მშობლის სახელი 😊")
            surname = input("მშობლის გვარი 😊")
            phone = input("მშობლის ნომერი 😊")
            facebook = input("მშობლის Facebook ლინკი 😊")
            email = input("მშობლის Email 😊")
            found = False
            while found == False:
                for i in email:
                    if i == "@":
                        found = True

                if found == False:
                    print("არასწორი email, სცადე თავიდან")
                    email = input("შეიყვანე email: ")                        

            print("მშობლის ინფორმაცია 😊")
            print("სახელი :",name)
            print("გვარი :",surname)
            print("ნომერი :",phone)
            print("Facebook :",facebook)
            print("Email :", email)
            print("მიღებულია")

        else:
            print("მიუღებელია")


    # N4_______________________


    print('რ ე გ ი ს ტ რ ა ც ი ა')

    name = input('შეიყვანეთ თქვენი სახელი: ')
    surname = input('შეიყვანეთ თქვენი გვარი: ')
    email = input('შეიყვანეთ თქვენი Email: ')
    found = False

    while found == False:
        for i in email:
            if i == "@":
                found = True

        if found == False:
            print("არასწორი email, სცადე თავიდან")
            email = input("შეიყვანე email: ")


    phone_number = input('შეიყვანეთ თქვენი ტელეფონის ნომერი: ')
    personal_id = input('შეიყვანეთ თქვენი ID: ')
    fb_link = input('შეიყვანეთ თქვენი Facebook ლინკი: ')
    password = input('შეიყვანეთ თქვენი პაროლი: ')
    confirm_password = input('დაადასტურეთ თქვენი პაროლი: ')

    while password != confirm_password:
        print("Wrong password, try again")
        confirm_password = input('შეიყვანეთ თქვენი პაროლი: ')
    print("Access granted")

    chad_or_looser = input('მზად ხარ დაიწყო GOA-ში სწავლა დაუთმო დრო გაკვეთილებს, ივარჯიშო შესვენებაზე და გახდე ნამდვილი ჩადი? (დიახ/არა): ')
    chad = 'დიახ'
    looser = 'არა'

    if chad_or_looser == chad:
        print('გილოცავ ამ მომენტიდან შენ გახდი GOA-ს აკადემიის წევრი და ნაბიჯი გადადგი რომ გახდე ნამდვილი "Chad" ')
    elif chad_or_looser == looser:
        print('სამწუხაროდ შენ აირჩიო რომ იყო "looser" ')
    else:
        print('სცადეთ ახლიდან')



    # N5_______________________

        if age >= 18 and age <=99:
            if speeds == "1":
                print("==========განრიგი==========")
                print('თქვენ GOAში ისწავლით კვირაში ერთხელ')
                print('ყოველ ორშაბათს 21:00-23:00 საათებში')
                print("===========================")
            elif speeds == "2":
                print("==========განრიგი==========")
                print('თქვენ GOAში ისწავლით კვირაში ორჯერ')
                print('ყოველ ორშაბათს და ხუთშაბათს 21:00-23:00 საათებში')
                print("===========================")
            elif speeds == '3':
                print("==========განრიგი==========")
                print('თქვენ GOAში ისწავლით კვირაში სამჯერ')
                print("ყოველ ორშაბათს ხუთშაბათს და შაბათს 21:00-23:00 საათებში")
                print("===========================")
            else:
                print('სცადეთ ხელთავიდან')
        else:
            if speeds == "1":
                    print("==========განრიგი==========")
                    print('თქვენ შვილი GOAში ისწავლით კვირაში ერთხელ')
                    print('ყოველ ორშაბათს 21:00-23:00 საათებში')
                    print("===========================")
            elif speeds == "2":
                    print("==========განრიგი==========")
                    print('თქვენ შვილი GOAში ისწავლით კვირაში ორჯერ')
                    print('ყოველ ორშაბათს და ხუთშაბათს 21:00-23:00 საათებში')
                    print("===========================")
            elif speeds == '3':
                    print("==========განრიგი==========")
                    print('თქვენ შვილი GOAში ისწავლით კვირაში სამჯერ')
                    print("ყოველ ორშაბათს ბუთშაბათს და შაბათს 21:00-23:00 საათებში")
                    print("===========================")
            else:
                    print('სცადეთ ხელთავიდან')




    # N6_______________________



    print("---- GOA MMA ----")

    answer = input('გინდა გაიგო ინფორმაცია GOA MMA-ს შესახებ? (კი/არა): ')

    print("--------------")

    if answer == 'კი':
        print('GOA MMA მართლაც მაგარი ადგილია ვარჯიშისთვის 💪')
        print('GOA MMA-ში თქვენ შეისწავლით Boxing-ს,Kickboxing-ს და MMA-ის')
        print('---------------')
        print('ეს არის ჩვენი Instagram-ი: @goa_mma ')
        print('---------------')
        print('ეს არის ჩვენი განრიგი: ')
        print("ორშაბათი - 18:00")
        print("სამშაბათი - 18:00")
        print("ხუთშაბათი - 19:00")
        print("შაბათი - 12:00")
    else:
        print('გილოცავ! შენ დღეიდან ხარ Chad-ი რადგან დარეგისტრირდი GOA-ში 😎')

else:
    print("Available courses:\n")

    py = "Python Programming"
    wb = "Web Development"
    gd = "Game Development"

    print(f"1. {py}")
    print("   Short description: Beginner programming in Python")
    print("   Speed: 1,2,3\n")

    print(f"2. {wb}")
    print("   Short description: Creating websites")
    print("   Speed: 1,2,3\n")

    print(f"3. {gd}")
    print("   Short description: Creating games")
    print('speed 1 - once a week\nspeed 2 - twice a week\nspeed 3 - three times a week\n')
    print("   Speed: 1,2,3\n")

    choice = input("Choose a course (Python Programming/Web Development/Game Development): ")

    if choice == py:
        print("\nPython Programming")
        print("Detailed information:")
        print("You will learn Python basics, variables, loops and functions.")

    elif choice == wb:
        print("\nWeb Development")
        print("Detailed information:")
        print("You will learn HTML, CSS and JavaScript.")

    elif choice == gd:
        print("\nGame Development")
        print("Detailed information:")
        print("You will learn how to create games with Python.")

    else:
        print("Wrong choice, try again ❌")

    speeds = input("Enter the learning speed you want (1/2/3): ")


    # N3_______________________


    age = int(input("Enter your age: "))

    while age < 0 or age > 99:
        print("Invalid age. Please enter a valid age.")
        age = int(input("Enter your age: "))

        if age >= 18 and age <= 99:
            print("You are an adult")

        elif age < 18:
            print("You are underage, enter parent information")

            name = input("Parent name 😊 ")
            surname = input("Parent surname 😊 ")
            if name[0].isupper() and surname[0].isupper():
                    print("OK ✅")
            else:
                print(name.capitalize(), surname.capitalize())

            name = input("Parent name 😊 ")
            surname = input("Parent surname 😊 ")

            phone = input("Parent phone number 😊 ")
            facebook = input("Parent Facebook link 😊 ")
            email = input("Parent Email 😊 ")

            found = False

            while found == False:
                for i in email:
                    if i == "@":
                        found = True

                if found == False:
                    print("Invalid email, try again")
                    email = input("Enter email: ")

            email = input("Enter your email: ")

            found = False

            while found == False:
                for i in email:
                    if i == "@":
                        found = True

                if found == False:
                    print("Invalid email, try again")
                    email = input("Enter email: ")

            print("Parent information 😊")
            print("Name:", name)
            print("Surname:", surname)
            print("Phone:", phone)
            print("Facebook:", facebook)
            print("Email:", email)
            print("Accepted")

    else:
            print("Not accepted")


    # N4_______________________

    print("R E G I S T R A T I O N")

    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    if name[0].isupper() and surname[0].isupper():
        print("OK ✅")
    else:
        print(name.capitalize(), surname.capitalize())

    email = input("Enter your email: ")

    found = False

    while found == False:
        for i in email:
            if i == "@":
                found = True

        if found == False:
            print("Invalid email, try again")
            email = input("Enter email: ")


    phone_number = input("Enter your phone number: ")
    personal_id = input("Enter your ID: ")
    fb_link = input("Enter your Facebook: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    email = input("Enter your email: ")

# if "@" in email and ("@gmail.com" in email or "@yahoo.com" in email or "@outlook.com" in email):
#     print("Valid email ✅")
# else:
#     print("Invalid ❌")

    while password != confirm_password:
        print("Wrong password, try again")
        confirm_password = input("Enter the password again: ")

    print("Access granted")

    chad_or_looser = input("Are you ready to study at GOA, spend time on lessons and become a real Chad? (yes/no): ")

    chad = "yes"
    looser = "no"

    if chad_or_looser == chad:
        print('Congratulations! From this moment you became a member of GOA Academy and took a step to become a real "Chad"')

    elif chad_or_looser == looser:
        print('Unfortunately you chose to be a "looser"')

    else:
        print("Try again")



    # N5_______________________
    # while True:
    if age >= 18 and age <= 99:

        if speeds == "1":
            print("==========Schedule==========")
            print("You will study in GOA once a week")
            print("Every Monday 21:00-23:00")
            print("============================")

        elif speeds == "2":
            print("==========Schedule==========")
            print("You will study in GOA twice a week")
            print("Every Monday and Thursday 21:00-23:00")
            print("============================")

        elif speeds == "3":
            print("==========Schedule==========")
            print("You will study in GOA three times a week")
            print("Monday, Thursday and Saturday 21:00-23:00")
            print("============================")

        else:
            print("Try again")

    else:

            if speeds == "1":
                print("==========Schedule==========")
                print("Your child will study in GOA once a week")
                print("Every Monday 21:00-23:00")
                print("============================")

            elif speeds == "2":
                print("==========Schedule==========")
                print("Your child will study in GOA twice a week")
                print("Every Monday and Thursday 21:00-23:00")
                print("============================")

            elif speeds == "3":
                print("==========Schedule==========")
                print("Your child will study in GOA three times a week")
                print("Monday, Thursday and Saturday 21:00-23:00")
                print("============================")

            else:
                print("Try again")



  # N6_______________________

    print("---- GOA MMA ----")

    answer = input("Do you want to know information about GOA MMA? (yes/no): ")

    print("--------------")

    if answer == "yes":

        print("GOA MMA is really a great place to train 💪")
        print("In GOA MMA you will learn Boxing, Kickboxing and MMA")
        print("---------------")
        print("This is our Instagram: @goa_mma")
        print("---------------")
        print("This is our schedule:")
        print("Monday - 18:00")
        print("Tuesday - 18:00")
        print("Thursday - 19:00")
        print("Saturday - 12:00")

    else:
        print("Congratulations! From today you are a Chad because you registered in GOA 😎")