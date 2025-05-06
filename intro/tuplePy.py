thisTuple = ("apple", "banana", "cherry")
thisTuple = tuple(("apple", "banana", "cherry"))
thisTuple = tuple(("apple", "banana", "cherry", "orange"))
print(thisTuple.count("apple"))
print(thisTuple.index("banana", 1, 5))
print(thisTuple[1:3])
print(thisTuple[1:3] + thisTuple[2:4])
print(thisTuple[1:3] * 2)
print(len(thisTuple))

tuple1 = ("apple")  # this is not a tuple, it's a string
tuple1 = ("apple",)  # thisTuple = tuple1 + thisTuple[2:4]


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Since tuples are immutable, they do not have a built-in append() or extend() method.
# However, you can concatenate tuples to create a new tuple with the desired elements.
# For example:
x = (1, 2, 3)
y = (4, 5, 6)
z = x + y  # Concatenate tuples
# unpacking a tuple
a, b, c, *e = z  # Unpacking a tuple into variables
print(a, b, c)  # Output: 1 2 3
print(e)  # Output: 1 2 3
q, *w, r = z
print(q, w, r)  # Output: 1 2 3

# for i in z:
#     print(i, end="\n ")  # Output: 1 2 3 4 5 6

i = 0
while i < len(z):
    print(z[i], end="\n ")  # Output: 1 2 3 4 5 6
    i += 1
