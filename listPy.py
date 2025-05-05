thisList = ["apple", "banana", "cherry"]
thisList = list(("apple", "banana", "cherry"))
thisList[1:3] = list(("orange", "kiwi"))
thisList[1:3] = ["orange", "kiwi"]
if "apple" in thisList:
    print(len(thisList))

thisList.append("orange")
thisList.insert(1, "orange")

# print(thisList.count("apple"))
# print(thisList.index("orange"))
print(thisList.index("orange", 1, 5))
tropical = ["mongo", "pineapple", "papaya"]
thisList.extend(tropical)

thisList.remove("orange")
del thisList[1]
# thisList.pop(1)
# thisList.pop()
# thisList.clear()
print(thisList)
print(range(2, 6))
# [print(x) for x in thisList if x != "banana" and x != "papaya"]
newFruitList = [x for x in thisList if "a" in x]
print(sorted(newFruitList, reverse=True))
# numList = [x+1 for x in range(10) if x % 2 == 0]
# print(4*[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# numList = [[y for y in range(10)][x] for x in range(10)]
# print(numList)
thisList.sort(key=str.lower, reverse=True)
print(thisList)
copyList1 = thisList.copy()
copyList2 = thisList[:]
copyList3 = list(thisList)
