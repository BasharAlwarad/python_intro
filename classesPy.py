class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("Mike", "Olsen")
# x.printname()


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

# for x in (car1, boat1, plane1):
#     x.move()


def myfunc1():
    x = "Jane"

    def myfunc2():
        def myfunc3():
            nonlocal x
            x = "hello"
        myfunc3()
    myfunc2()
    return x


print(myfunc1())
