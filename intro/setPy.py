thisSet = {"apple", "banana", "cherry", "apple"}
thisSet = set(("apple", "banana", "cherry", "apple", 1, True, 0, False))
tropical = {"mango": "1", "pineapple": "2", "papaya": 3}
thisSet.add("orange")
thisSet.update(["kiwi", "mango"])
thisSet.update(tropical)
# print(thisSet)
# print(len(thisSet))
for i in thisSet:
    print(i, end="\n ")  # Output: apple banana cherry 1 True 0 False

# print("apple" in thisSet)  # Output: True
# print(True in thisSet)  # Output: True

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# Note: If the item to remove does not exist, remove() will raise an error.
# discard() will not raise an error.
# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The clear() method empties the set:
# The del keyword will delete the set completely:

# Join Sets
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
# set2 = (1, 2, 3)
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

# mySet = set1 | set2 | set3 | set4
mySet = set1.union(set2, set3, set4)
print(mySet)
