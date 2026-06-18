# 2) Set-ის ძირითადი განმასხვავებელი თვისებები

# • Set ინახავს მხოლოდ უნიკალურ ელემენტებს
# • დუბლიკატები ავტომატურად იშლება
# • ელემენტები არ არის დალაგებული ინდექსების მიხედვით
# • Set არის შეცვლადი (mutable)
# • Set-ში შეიძლება იყოს სხვადასხვა ტიპის მონაცემები

# 3) Set-ის ფუნქციები/მეთოდები და მაგალითები

# add() - ელემენტის დამატება
s = {1, 2, 3}
s.add(4)
print(s)

# remove() - ელემენტის წაშლა
s.remove(2)
print(s)

# clear() - სეტის გასუფთავება
s.clear()
print(s)

# union() - სეტების გაერთიანება
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))


# difference() - განსხვავებული ელემენტები
print(a.difference(b))

# len() - ელემენტების რაოდენობა
print(len(a))

# 4) Set 10 რიცხვით, სადაც 3 დუბლიკატია

numbers = {1, 2, 3, 4, 5, 5, 6, 7, 7, 8}
print(numbers)

# შედეგში დუბლიკატები აღარ გამოჩნდება

# 5) მასივის Set-ად გადაქცევა

arr = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(arr)

print(unique_numbers)

# 6) საყვარელი წიგნების/ფილმების სეტი

movies = {
    "Interstellar",
    "Inception",
    "The Dark Knight",
    "Avengers"
}

print(len(movies))

# 7) კვირის დღეების სეტი

days = {
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
}

for day in days:
    print("დღე:", day)

# 8) სპორტზე მოსიარულე უნიკალური მოსწავლეები

football_players = {'დათო', 'ნიკა', 'ლუკა', 'ლიკა'}
basketball_players = {'ანი', 'ლუკა', 'მარიამი', 'ნიკა'}

all_players = football_players.union(basketball_players)

print(all_players)
print("სულ უნიკალური მოსწავლე:", len(all_players))

# 9) სასწავლი ტექნოლოგიების პოვნა

wishlist = {
    "Python",
    "JavaScript",
    "React",
    "Django",
    "SQL"
}

learned = {
    "Python",
    "HTML",
    "CSS"
}

to_learn = wishlist.difference(learned)

print("დარჩენილი ტექნოლოგიები:", to_learn)

# 10) კალათის გასუფთავება

cart = {101, 204, 305}

cart.clear()

print(cart)