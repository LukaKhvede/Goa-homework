# .split() მეთოდი გამოიყენება სტრინგის (string) ნაწილებად დასაყოფად.
# ის აბრუნებს სიას (list).
# ძირითადად ყოფს ტექსტს space-ებით, მაგრამ შეგვიძლია სხვა სიმბოლოც მივუთითოთ.

# მაგალითი 1
text = "Hello World Python"
result = text.split()

print(result)
# ['Hello', 'World', 'Python']


# მაგალითი 2
fruits = "apple,banana,orange"
result2 = fruits.split(",")

print(result2)
# ['apple', 'banana', 'orange']



# .join() მეთოდი გამოიყენება სიის (list) ელემენტების ერთ სტრინგად გასაერთიანებლად.
# join()-ში ვწერთ რა სიმბოლოთი უნდა გაერთიანდეს ელემენტები.

# მაგალითი 1
words = ["Hello", "World"]
sentence = " ".join(words)

print(sentence)
# Hello World


# მაგალითი 2
numbers = ["1", "2", "3", "4"]
result3 = "-".join(numbers)

print(result3)
# 1-2-3-4