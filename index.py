# | Bit Position | 7   | 6  | 5  | 4  | 3 | 2 | 1 | 0 |
# | ------------ | --- | -- | -- | -- | - | - | - | - |
# | Power of 2   | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 80])
# ypoints = np.array([0, 50])

# plt.plot(xpoints, ypoints)
# plt.show()


# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels=mylabels, startangle=90)
# plt.show()
# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# def create_phone_number(n):
#     def format_number(n):
#         x = ""
#         for i in n:
#             x += str(i)
#         return x
#     return f"({format_number(n[:3])}) {format_number(n[3:6])}-{format_number(n[6:])}"

# def create_phone_number(n):
#     n = list(map(str, n))
#     print(n)
#     return "({}) {}-{}".format("".join(n[:3]), "".join(n[3:6]), "".join(n[6:]))
#     # return f"({''.join(map(str, n[:3]))}) {''.join(map(str, n[3:6]))}-{''.join(map(str, n[6:]))}"
def create_phone_number(n):
    x = "".join(map(str, n))
    return f"({x[:3]}) {x[3:6]}-{x[6:]}"
    # return "({}) {{{}}}-{{{}}}".format(x[:3], x[3:6], x[6:])


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# print("Start", end="-->")
# print("End")
# a = 2 ** 3 ** 2
# b = (2 ** 3) ** 2
# print(a, b)


# for i in range(5, 0, -1):
#     print(i)
#     if i == 2:
#         break
# else:
#     print("Finished")

# my_list = [0, 2, 4, 6, 8]
# my_list[::2] = [10, 20, 30]
# print(my_list)

# my_tuple = 10,
# another_tuple = my_tuple * 2
# another_tuple += 5,
# print(another_tuple)

# my_list = ["apple", "banana", "cherry"]
# new_list = my_list[:]
# del my_list[1]
# print(my_list)


# def mystery(x, y=[]):
#     y.append(x)
#     return y


# print(mystery(1))
# print(mystery(2, []))
# print(mystery(3))


print(result=2 + 3 * 5 ** 2 // 4 - 6)
