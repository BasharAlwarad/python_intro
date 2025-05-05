def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

# Positional-Only Arguments
# In Python, you can define a function that accepts positional-only arguments by using a slash (/) in the function definition.
# This means that the arguments before the slash must be passed positionally and cannot be passed as keyword arguments.


def my_function(x, /):
    print(x)


my_function(3)
