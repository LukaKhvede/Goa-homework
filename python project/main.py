
class BankAccount:
    def __init__(self, username, account_id, pin):
        # Angarishis monacemebis shenaxva
        self.username = username
        self.account_id = account_id

        # Level 2 data hiding
        self.__pin = pin
        self.__balance = 0
        self.__debt = 0
        self.__savings = 0

        # Level 1 data hiding
        self._history = []

    def check_pin(self, pin):
        # PIN-kodis shemowmeba
        return self.__pin == pin

    def deposit(self, amount):
        # Angarishze tanxis shetana
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        else:
            self.__balance += amount
            self._history.append("თანხის შეტანა: " + str(amount) + " GEL")
            print("თანხა წარმატებით დაემატა ანგარიშს!")

    def withdraw(self, amount):
        # Angarishidan tanxis gamotana
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        elif amount > self.__balance:
            print("ბალანსზე არასაკმარისი თანხაა!")
        else:
            self.__balance -= amount
            self._history.append("თანხის გამოტანა: " + str(amount) + " GEL")
            print("თანხა წარმატებით გაიტანე!")

    def transfer(self, other_account, amount):
        # Tanxis sxva angarishze gadaricxva
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        elif amount > self.__balance:
            print("ბალანსზე არასაკმარისი თანხაა!")
        else:
            # Gamgzavnis balansidan tanxis gamokleba
            self.__balance -= amount

            # Mimgebis balansze tanxis damateba
            other_account.__balance += amount

            # Tranzaqciis istoriashi damateba
            self._history.append(
                "გადარიცხვა " + other_account.username + "-თან: "
                + str(amount) + " GEL"
            )

            other_account._history.append(
                "ჩარიცხვა " + self.username + "-ისგან: "
                + str(amount) + " GEL"
            )

            print("თანხა წარმატებით ჩაერიცხა " + other_account.username + "-ს!")
            print("მიმღების ID: " + other_account.account_id)

    def pay_utility(self, utility_name, amount):
        # Komunaluri gadasaxadis gadaxda
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        elif amount > self.__balance:
            print("ბალანსზე არასაკმარისი თანხაა!")
        else:
            self.__balance -= amount
            self._history.append(
                utility_name + "-ის გადახდა: " + str(amount) + " GEL"
            )
            print("გადასახადი წარმატებით გადაიხადე!")

    def add_debt(self, amount):
        # Valis damateba
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        else:
            self.__debt += amount
            self._history.append("ვალის დამატება: " + str(amount) + " GEL")
            print("ვალი წარმატებით დაემატა!")

    def pay_debt(self, amount):
        # Valis gadaxda
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        elif amount > self.__debt:
            print("ამ ოდენობის ვალი არ გაქვს!")
        elif amount > self.__balance:
            print("ბალანსზე არასაკმარისი თანხაა!")
        else:
            self.__balance -= amount
            self.__debt -= amount
            self._history.append("ვალის გადახდა: " + str(amount) + " GEL")
            print("ვალი წარმატებით გადაიხადე!")

    def convert_currency(self, amount, currency):
        # Laris sxva valutashi konvertacia
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        elif amount > self.__balance:
            print("ბალანსზე არასაკმარისი თანხაა!")
        elif currency == "USD":
            # Demo kursi: 1 USD = 2.7 GEL
            converted = amount / 2.7
            self.__balance -= amount
            self._history.append(
                "ვალუტის კონვერტაცია USD-ში: " + str(amount) + " GEL"
            )
            print("კონვერტაცია წარმატებულია!")
            print("მიიღე დოლარში: " + str(round(converted, 2)) + " USD")
        elif currency == "EUR":
            # Demo kursi: 1 EUR = 3 GEL
            converted = amount / 3
            self.__balance -= amount
            self._history.append(
                "ვალუტის კონვერტაცია EUR-ში: " + str(amount) + " GEL"
            )
            print("კონვერტაცია წარმატებულია!")
            print("მიიღე ევროში: " + str(round(converted, 2)) + " EUR")
        else:
            print("ასეთი ვალუტა არ არის ხელმისაწვდომი!")

    def game_topup(self, game_name, amount):
        # Tamashis balansis shevseba
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        elif amount > self.__balance:
            print("ბალანსზე არასაკმარისი თანხაა!")
        else:
            self.__balance -= amount
            self._history.append(
                game_name + "-ის შევსება: " + str(amount) + " GEL"
            )
            print("თამაშის ბალანსი წარმატებით შეივსო!")

    def add_savings(self, amount):
        # Tanxis yulabashi gadatana
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        elif amount > self.__balance:
            print("ბალანსზე არასაკმარისი თანხაა!")
        else:
            self.__balance -= amount
            self.__savings += amount
            self._history.append("ყულაბაში დამატება: " + str(amount) + " GEL")
            print("თანხა წარმატებით გადაიტანე ყულაბაში!")

    def withdraw_savings(self, amount):
        # Yulabidan tanxis angarishze dabruneba
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        elif amount > self.__savings:
            print("ყულაბაში ამდენი თანხა არ გაქვს!")
        else:
            self.__savings -= amount
            self.__balance += amount
            self._history.append("ყულაბიდან გამოტანა: " + str(amount) + " GEL")
            print("თანხა წარმატებით დაბრუნდა ანგარიშზე!")

    def phone_topup(self, phone, amount):
        # Telefonis balansis shevseba
        if amount <= 0:
            print("თანხა უნდა იყოს 0-ზე მეტი!")
        elif amount > self.__balance:
            print("ბალანსზე არასაკმარისი თანხაა!")
        else:
            self.__balance -= amount
            self._history.append(
                "ტელეფონის შევსება " + phone + ": " + str(amount) + " GEL"
            )
            print("ტელეფონის ბალანსი წარმატებით შეივსო!")

    def show_balance(self):
        # Angarishis informaciis gamotana
        print("მომხმარებელი: " + self.username)
        print("ანგარიშის ID: " + self.account_id)
        print("ბალანსი: " + str(self.__balance) + " GEL")
        print("ვალი: " + str(self.__debt) + " GEL")
        print("ყულაბა: " + str(self.__savings) + " GEL")

    def show_history(self):
        # Tranzaqciebis istoriis gamotana
        print("\n--- ტრანზაქციების ისტორია ---")

        if len(self._history) == 0:
            print("ისტორია ჯერ ცარიელია.")
        else:
            for item in self._history:
                print(item)


class Bank:
    def __init__(self, name):
        # Bankis monacemebis shenaxva
        self.name = name
        self.accounts = []

    def create_account(self, username, account_id, pin):
        # Axali angarishis sheqmna
        for account in self.accounts:
            if account.account_id == account_id:
                print("ეს ID უკვე გამოყენებულია!")
                return None

        new_account = BankAccount(username, account_id, pin)
        self.accounts.append(new_account)

        print("ანგარიში წარმატებით შეიქმნა!")
        print("შენი ანგარიშის ID: " + account_id)

        return new_account

    def find_account(self, account_id):
        # Angarishis modzebna ID-it
        for account in self.accounts:
            if account.account_id == account_id:
                return account

        return None

    def login(self, account_id, pin):
        # Angarishshi shesvlis shemowmeba
        account = self.find_account(account_id)

        if account is None:
            print("ასეთი ანგარიში არ არსებობს!")
            return None
        elif account.check_pin(pin):
            print("ანგარიშში წარმატებით შეხვედი!")
            return account
        else:
            print("PIN-კოდი არასწორია!")
            return None


# Bankis obieqtis sheqmna
bank = Bank("GOA BANK")


def account_menu(account):
    # Piradi angarishis meniu
    while True:
        print("\n--- პირადი ანგარიში ---")
        print("1. ტრანზაქციების ისტორია")
        print("2. თანხის გადარიცხვა")
        print("3. კომუნალური გადასახადები")
        print("4. ვალის გადახდა")
        print("5. ვალუტის კონვერტაცია")
        print("6. ანგარიშის ინფორმაცია")
        print("7. თამაშის ბალანსის შევსება")
        print("8. ყულაბა")
        print("9. ტელეფონის ბალანსის შევსება")
        print("10. ანგარიშზე თანხის შეტანა")
        print("11. ანგარიშიდან თანხის გამოტანა")
        print("12. ვალის დამატება")
        print("0. გასვლა")

        action = input("აირჩიე მოქმედება: ")

        if action == "1":
            # Istoriis naxva
            account.show_history()

        elif action == "2":
            # Mimgebis ID-is da saxelis shemowmeba
            receiver_id = input("შეიყვანე მიმღების ანგარიშის ID: ")
            receiver_name = input("შეიყვანე მიმღების სახელი: ")

            receiver = bank.find_account(receiver_id)

            if receiver is None:
                print("ასეთი ანგარიში არ არსებობს!")
            elif receiver.username != receiver_name:
                print("მიმღების სახელი და ID ერთმანეთს არ ემთხვევა!")
            elif receiver.account_id == account.account_id:
                print("საკუთარ ანგარიშზე თანხას ვერ გადარიცხავ!")
            else:
                # Tanxis sheyvanisa da gadaricxvis shemowmeba
                try:
                    amount = float(input("შეიყვანე გადასარიცხი თანხა: "))
                    account.transfer(receiver, amount)
                except ValueError:
                    print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "3":
            # Komunaluri gadasaxadis archeva
            print("1. ელექტროენერგია")
            print("2. წყალი")
            print("3. გაზი")

            utility_choice = input("აირჩიე გადასახადი: ")

            if utility_choice == "1":
                utility_name = "ელექტროენერგია"
            elif utility_choice == "2":
                utility_name = "წყალი"
            elif utility_choice == "3":
                utility_name = "გაზი"
            else:
                print("არასწორი არჩევანია!")
                continue

            try:
                amount = float(input("შეიყვანე გადასახდელი თანხა: "))
                account.pay_utility(utility_name, amount)
            except ValueError:
                print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "4":
            # Valis gadaxda
            try:
                amount = float(input("შეიყვანე გადასახდელი ვალის თანხა: "))
                account.pay_debt(amount)
            except ValueError:
                print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "5":
            # Valutis archeva
            print("1. დოლარი (USD)")
            print("2. ევრო (EUR)")

            currency_choice = input("აირჩიე ვალუტა: ")

            if currency_choice == "1":
                currency = "USD"
            elif currency_choice == "2":
                currency = "EUR"
            else:
                print("არასწორი არჩევანია!")
                continue

            try:
                amount = float(input("შეიყვანე ლარის თანხა: "))
                account.convert_currency(amount, currency)
            except ValueError:
                print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "6":
            # Angarishis informaciis naxva
            account.show_balance()

        elif action == "7":
            # Tamashis archeva
            print("1. Fortnite")
            print("2. Roblox")
            print("3. PlayStation")

            game_choice = input("აირჩიე თამაში: ")

            if game_choice == "1":
                game_name = "Fortnite"
            elif game_choice == "2":
                game_name = "Roblox"
            elif game_choice == "3":
                game_name = "PlayStation"
            else:
                print("არასწორი არჩევანია!")
                continue

            try:
                amount = float(input("შეიყვანე შესავსები თანხა: "))
                account.game_topup(game_name, amount)
            except ValueError:
                print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "8":
            # Yulabis meniu
            print("1. ყულაბაში თანხის დამატება")
            print("2. ყულაბიდან თანხის გამოტანა")

            savings_choice = input("აირჩიე მოქმედება: ")

            try:
                amount = float(input("შეიყვანე თანხა: "))

                if savings_choice == "1":
                    account.add_savings(amount)
                elif savings_choice == "2":
                    account.withdraw_savings(amount)
                else:
                    print("არასწორი არჩევანია!")
            except ValueError:
                print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "9":
            # Telefonis nomris shemowmeba
            phone = input("შეიყვანე ტელეფონის ნომერი: ")

            if len(phone) < 9 or not phone.isdigit():
                print("ნომერი უნდა შეიცავდეს მინიმუმ 9 ციფრს!")
            else:
                try:
                    amount = float(input("შესავსები თანხა: "))
                    account.phone_topup(phone, amount)
                except ValueError:
                    print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "10":
            # Angarishze tanxis shetana
            try:
                amount = float(input("შეიყვანე შესატანი თანხა: "))
                account.deposit(amount)
            except ValueError:
                print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "11":
            # Angarishidan tanxis gamotana
            try:
                amount = float(input("შეიყვანე გამოსატანი თანხა: "))
                account.withdraw(amount)
            except ValueError:
                print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "12":
            # Valis damateba
            try:
                amount = float(input("შეიყვანე ვალის თანხა: "))
                account.add_debt(amount)
            except ValueError:
                print("შეიყვანე თანხა რიცხვის სახით!")

        elif action == "0":
            # Angarishidan gamosvla
            print("ანგარიშიდან გამოხვედი.")
            break

        else:
            # Araswori archeva
            print("არასწორი არჩევანია!")


# Programis mtavari meniu
while True:
    print("\n========== GOA BANK ==========")
    print("1. ანგარიშის შექმნა")
    print("2. ანგარიშში შესვლა")
    print("0. პროგრამიდან გასვლა")

    choice = input("აირჩიე მოქმედება: ")

    if choice == "1":
        # Axali angarishis monacemebis sheyvana
        username = input("შეიყვანე სახელი: ")
        account_id = input("შექმენი ანგარიშის ID (მაგ. GOA123): ")
        pin = input("შექმენი PIN-კოდი: ")

        if username == "" or account_id == "" or pin == "":
            print("ყველა ველი უნდა შეავსო!")
        else:
            bank.create_account(username, account_id, pin)

    elif choice == "2":
        # Angarishshi shesvla
        account_id = input("შეიყვანე ანგარიშის ID: ")
        pin = input("შეიყვანე PIN-კოდი: ")

        account = bank.login(account_id, pin)

        if account is not None:
            account_menu(account)

    elif choice == "0":
        # Programis dasruleba
        print("GOA BANK-იდან გამოსვლა.")
        break

    else:
        # Araswori archeva
        print("არასწორი არჩევანია!")
