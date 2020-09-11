# importing numpy module

import numpy as np


# creating a basic array

# This section covers np.array(), np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace(), dtype

a = np.array([1, 2, 3])
print(a)

b = np.zeros(2)
print(b)
print(b.astype(int))

c = np.ones(2)
print(c)
print(c.astype(int))


# Create an empty array with 2 elements
d = np.empty(2)
print(d)


# create an array with a range of elements:
e = np.arange(4)
print(e)

#  use np.linspace() to create an array with
# values that are spaced linearly in a specified interval:

f = np.linspace(0, 10, num=5)
print(f)


# Specifying your data type

g = np.ones(2, dtype=np.int64)
print(g)


# =============================


# Adding, removing, and sorting elements¶

#  sorting
h = np.array([5, 2, 8, 64, 2])
print(np.sort(h))


# concatenate()

i = np.arange(5)
j = np.arange(6, 10)
print(np.concatenate((i, j), axis=0))
print()

k = np.array([[1, 2, 3], [4, 5, 6]])
l = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate((k, l), axis=0))
print(np.concatenate((k, l), axis=1))
print()

# How do you know the shape and size of an array
print("dimension ->")
print(k.ndim)
print()
print("size ->")
print(k.size)
print()
print("shape ->")
print(k.shape)
print()

# Can you reshape an array?

a = np.arange(6)
print(a)
print()

b = a.reshape(2, 3)
print("reshaped array ->", b, sep="\n")
print()


# With np.reshape, you can specify a few optional parameters:
c = np.reshape(a, newshape=(3, 2), order="C")
print(c)


# How to convert a 1D array into a 2D array (how to add a new axis to an array)
