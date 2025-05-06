# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""There are four collection data types in the Python programming language:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""

thisDict = dict(name="John", age=36, country="Norway")
# print(thisDict)
# print(thisDict["age"])
# print(thisDict.get("age"))
# print(thisDict.keys())
# print(thisDict.values())
# print(thisDict.items())

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

# print(x)  # before the change

# changing the value of a key
car["year"] = 2020
car.update({"year": 2025})

# adding a new key-value pair
# car["color"] = "red"
car.update({"color": "blue"})

# removing a key-value pair
# car.pop("model")
# car.popitem()  # removes the last inserted key-value pair
# del car["brand"]  # removes the key-value pair with the specified key
# # del car # deletes the entire dictionary
# car.clear()  # clears the dictionary but keeps the dictionary object

# for key, value in car.items():
#     print(key, value)
# print(x)  # after the change

# Dict Copy
# The copy() method returns a shallow copy of the dictionary.
# The dict() constructor also returns a copy of the dictionary.
# The copy() method does not create a copy of nested objects, only the outer dictionary.
newCar1 = car.copy()
newCar2 = dict(car)

# print(newCar1)
# print(newCar2)

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# print(myFamily["child2"]["name"])
for x, y in myFamily.items():
    for i, j in y.items():
        print(x, i, j)


#         Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
