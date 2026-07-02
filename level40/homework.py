students={
    "luka":89,
    "nika":76,
    "eka":54,
}
students["lika"]=45
filtered=[i for i in students if students[i]>=50]
print(filtered)
# meore
nums=[1,2,3,4,5,6,7,8,9]
nums1= [ i**2 for i in nums ]
nums2=[i for i in nums1 if i%2==0]
print(nums2)

# mesame

words = ["Python", "AI", "Development", "Code", "Learning", "Data"]
words1=[i for i in words if len(i)>4]
print(words1)

#meotxe

products = {
    "Bread": 2.5,
    "Milk": 4.0,
    "Eggs": 6.5,
    "Cheese": 12.0,
    "Apple": 1.8
}
products1=[i for i in products if products[i]>3]
print(products1)