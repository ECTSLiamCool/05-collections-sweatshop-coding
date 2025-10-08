"""
Sets are also collections
They are NOT ordered - meaning they don't have a fixed position - can't access by index
You CANNOT change existing items, but you can add/remove them
Advantage: DOES NOT ALLOW DUPLICATES
"""
#notice sets use curly braces{ }
trees = {"evergreen", "maple", "hickory", "oak"}
print(trees) #prints in a random order
#You cannot accesss elements by index - because it's unordered
#print(trees[0]) #CRASH - TypeError: 'set' object is not subscriptable

#add amd remove from list:
trees.add("palm") #note: this is ADD not append (lists use append)
print(trees)
trees.remove("evergreen")
print(trees)
#sets do not allow duplicates:
trees.add("palm")
print(trees) #palm was not added a second time

#quick trick to get clean lists (remove duplicates) - if order doesn't matter.
my_list = ["Bennett", "Bennett", "Bennett", "Draven", "Levi", "Liam(Awesome)"]
my_set = set(my_list)
my_list = list(my_set)
print(my_list)