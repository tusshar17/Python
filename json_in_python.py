# Python JSON


# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.


# JSON in Python

# Python has a built-in package called json, which can be
# used to work with JSON data.

# import json module

import json

# Parse JSON - Convert from JSON to Python

# If you have a JSON string, you can parse it by using the
# json.loads() method.
# The result will be a Python dictionary.

x = '{"name":"john", "age":30, "city":"New York"}'

y = json.loads(x)

print(y)
print(y["age"])


# Convert from Python to JSON

# If you have a Python object, you can convert it into a
# JSON string by using the json.dumps() method.

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:


# Python	    JSON
# dict	        Object
# list	        Array
# tuple	        Array
# str	        String
# int	        Number
# float	        Number
# True	        true
# False	        false
# None	        null


# Example

# Convert a Python object containing all the legal data types:

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print("======== Without indent =====")
print(json.dumps(x))


# ---------- Format the Result -------------

# The example above prints a JSON string, but it is not very
# easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier
# to read the result:

# Use the indent parameter to define the numbers of indents:
print("====== with indent ========")
print(json.dumps(x, indent=4))

# You can also define the separators, default value is
# (", ", ": "), which means using a comma and a space to
# separate each object,
# and a colon and a space to separate keys from values:
print("======== with indent and [. and ,] seperated =========")
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Order the Result

# The json.dumps() method has parameters to order the keys
# in the result:

# Use the sort_keys parameter to specify if the result
# should be sorted or not:
print("======== sorted ========")
print(json.dumps(x, indent=4, sort_keys=True))

print("hello")