# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

"""
# Open the file in append mode to add content to the file
file = open("demo.txt", "a")
file.write("Hello World\n")  # Write to the file
file.close()  # Close the file after writing

# Reopen the file in read mode to read its content
file = open("demo.txt", "r")
print(file.read())  # Read and print the file content
file.close()  # Close the file after reading
"""

import os
if os.path.exists("demo.txt"):
    with open("demo.txt", "r") as file:
        for line in file:
            print(line.strip())
    # print(file.readline(4))  # Read a single line from the file
    # print(file.readlines())  # Read and print the file content

    os.remove("demo.txt")  # Remove the file after reading
else:
    os.rmdir("demo")  # Remove the file after reading
    os.mkdir("demo")  # Create a directory named demo.txt
    with open("demo.txt", "x") as file:
        file.write("Hello World\n")  # Write to the file
    # with open("demo.txt", "a") as file:
    #     file.write("Hello World\n")  # Write to the file
