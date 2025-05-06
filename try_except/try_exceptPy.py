# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.
raise NameError("HiThere")  # This will cause an exception
if True:
    try:
        raise NameError("HiThere")
    except NameError as e:
        print("An exception occurred:", e)
    else:
        print("No exception occurred")
    finally:
        print("Execution completed")
else:
    try:
        # print(x)
        print("No exception occurred")
    except NameError as e:
        print("An exception occurred:", e)
    else:
        print("No exception occurred")
    finally:
        print("Execution completed")
