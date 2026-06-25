# Dictionary არის მონაცემთა ტიპი Python-ში,
# რომელიც ინახავს მონაცემებს key:value  წყვილებად.

# მაგალითად:
person = {
    "name": "Luka",
    "age": 18
}

footballer = {
    "name": "Cristiano Ronaldo",
    "country": "Portugal",
    "goals_count": 938
}

print(footballer)

foods = {
    "foods": ["ხინკალი", "მწვადი", "ქაბაბი"]
}

print(foods["foods"][1])

movie = {
    "title": "Avatar",
    "year": 2009
}

movie["year"] = 2025

print(movie)


student = {
    "name": "Luka",
    "age": 18
}

student.pop("age")

print(student)