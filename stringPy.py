a = "Hello world"

print(a[0])  # H

for i in range(len(a)):
    print(a[i])  # H e l l o   w o r l d

print(len(a))  # 11


print("Hello" in a)  # True

if "world" in a:
    print("Yes, 'world' is present.")  # Yes, 'world' is present.

if not "world" in a:
    print("No, 'world' is not present.")  # No, 'world' is not present.

# String Slicing
print(a[0:5])  # Hello
print(a[:5])  # Hello
print(a[:-1])  # Hello worl
print(a[-5:-1])  # worl
print(a[0:5:2])  # Hlo
print(a[0:-1:2])  # Hlowr
print(a[0:5:-1])  # empty string
print(a[6:])  # world


# Modify Strings
print(a.upper())  # HELLO WORLD
print(a.lower())  # hello world
print(a.strip())  # Hello world
print(a.lstrip())  # Hello world
print(a.rstrip())  # Hello world
print(a.replace("H", "J"))  # Jello world
print(a.split(" "))  # ['Hello', 'world']
print(a.split(","))  # ['Hello world']
print(a.split())  # ['Hello', 'world']


# String Concatenation
b = "Python"
print(a + " " + b)  # Hello world Python
print(a + " Python")  # Hello world Python
print(a + b)  # Hello worldPython

# Format - Strings
age = 36
price = 50
txt = f"My name is John, I am {age}"
txt = f"The price is {price:.2f} dollars"
txt = f"The price is {(price * age):.2f} dollars"
print(txt)

# Escape Characters
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
octalTxt = "\110\145\154\154\157"
print(octalTxt)  # \ooo	Octal value
hexTxt = "\x48\x65\x6c\x6c\x6f"
print(hexTxt)  # \xhh	Hex value
