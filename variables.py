myvar = "John Doe"
myvar1 = "John Doe"
MyVar = "John Doe"  # Pascal case
myVar = "John Doe"  # Camel case
my_var = "John Doe"  # Snake case

# Illegal variable names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

x, y, z = 1, 2, 3  # Multiple assignment
x, y, z = [1, 2, 3]  # Multiple assignment
x = y = z = 1  # Multiple assignment with same value

print(x, y, z)  # Output: 1 2 3
print(x+y-z)  # Output: 0


# error
print(my_var+x)  # Output: TypeError: can only concatenate str (not "int") to str


def my_function():
    myvar = "John Doe"  # Local variable
    print("Hello " + myvar)


my_function()  # Output: Hello John Doe


def my_function1():
    global myvar1  # Declare myvar1 as global
    myvar1 = "John Doe"  # Global variable
    print("Hello " + myvar1)


my_function1()  # Output: Hello John Doe
