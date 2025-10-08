"""
a tuple is:
Ordered (we access elements by index)
Unchangeable (immutable) - we cannot add/remove or change values
Allows duplicates
Faster than a list
"""

#tuples user ()
fruits = ("apple", "bannana", "dragon fruit")
print(fruits)
print(len(fruits))
print(fruits[1])


#see if values is in tuple
print("apple" in fruits)
print ("orange" in fruits)

#count items in fruit
print(fruits.count("apple")) #2

#find index of element:
print(fruits.index("bannana")) #1
print(fruits.index("car")) #throws ValueError - if element is not in the tuple

#Loop through a tuple:
#with a while loop
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

for fruit in fruits:
    print(fruit)