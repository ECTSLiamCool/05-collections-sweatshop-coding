name = "Joey" #stores a single value in a variable
print(name[0:2])

age = 15
#a collection is going to allow us to store multiple values under one name

#A list - use []
#Lists can be changed, can have duplicates, have positions (ordered)
games = ["dead space", "hollow knight", "elden ring", "oneshot"]
#this above is a better way of doing this:
#games1 = "dead space"
#games 2 = "hollow knight"


print(games)
#accessing items in the list:
print(games[1]) #lists are Zero indexed - the first element is index 0
#subset of the list:
print(games[0:2])
#you can also use the step function
print(games[0:4:2])
#this is the same as
print(games[::2])

#but you can crash!
#IndexError:list index out of range
print(games[0])


#You can know how long a list is
print(len(games))
#get the last element
print(games[-1]) #the python way
print(games[len(games)-1]) #common in other languages

#looping through a list
for elem in games:
    print(elem)

#find available methods 
print(dir(games))
games.reverse()
print(help(list))
games.sort(reverse=True)
print(games)

#see if an item is in the list:
print(f"is eldenring in our list: {"eldenring" in games}")
print(f"is mario in our list: {"mario" in games}")


#change an element in the list:
games[0] = "mario"
print(games)

elden_index = games.index("eldenring")
games[elden_index] = "ultrakill"
print(games)

#empty a list:
games.clear()
print(games)


#add element to the end of a list:
games.append("fortnite")
print(games)
#insert an element into a list
games.insert(1, "donkey kong")
print(games)
#remove element from listL
games.remove("hollow knight")
print(games)

#for the rest of the class:
#write a program that will continuously ask the user for their favorite foods
#take the input and add it to a list.
#when the user types Q, print the list