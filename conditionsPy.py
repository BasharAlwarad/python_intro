"""Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b"""

# ternary operator
a = 2
b = 330
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

# Pass
# The pass statement is a null operation; nothing happens when it executes.
if a > b:
    pass

# match statement
# The match statement is used to match a value against a pattern.
match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case _:
        print("a is not 1 or 2")


month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
