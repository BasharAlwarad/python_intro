import json

# x = [
#     "name",
#     "age",
#     "city"]

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x, indent=0, sort_keys=True, separators=("", "= "))
# y = json.load(x)

# the result is a JSON string:
print(type(y))
print(y)
