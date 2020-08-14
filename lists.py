# List is the most basic Data Structure in python. 
# List is a mutable data structure i.e items can be
#  added to list later after the list creation. 
# It’s like you are going to shop at the local market
#  and made a list of some items and later on you can
#  add more and more items to the list.
# append() function is used to add data to the list.

nums = []

nums.append("hi")
nums.append("hello")
nums.append("tushar")

print(nums)


#Removes all the elements from the list
nums.clear()
print(nums)

#Returns a copy of the list
x = [1,2,3,4,5]
y = x.copy()

print(y)


#Returns the 
#number of elements with the specified value
lst = ["tushar","karan","tushar","ram"]

print(lst.count("tushar"))


# Add the elements of a list (or any iterable), to the end of the current list

cars = ["duster","audi","alto"]
bikes = ["ktm","yanaha","ninja"]

print(cars)
print(bikes)
cars.extend(bikes)
print(cars)


# Returns the index of the first element with the specified value
print(cars.index("audi"))

# Adds an element at the specified position
cars.insert(0,"jeep")
print(cars)


# Removes the element at the specified position
cars.pop(0)
print(cars)

# Removes the first item with the specified value
cars.remove("audi")
print(cars)


# Reverses the order of the list
cars.reverse()
print(cars)


# Sorts the list
cars.sort()
print(cars)

cars.sort(reverse=1)
print(cars)