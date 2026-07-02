mydict = {
    'name':"luka",
    "surname":"Khvedelidze",
    "age":16
}
print(mydict.items())


#meore
numbers = [1, 2, 3, 4, 5]
numbers1=[x*2 for x in numbers]
print(numbers1)

#mesame

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers3=[x for x in numbers2 if x%2 ]
print(numbers3)