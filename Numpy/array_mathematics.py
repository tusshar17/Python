import numpy as np

a = np.array([1, 2, 3, 4, 5], int)
b = np.array([6, 7, 8, 9, 10], int)


# additon of two arrays
print(a+b)
print(np.add(a, b))

# subtraction of two arrays
print(a-b)
print(np.subtract(a, b))

# multiplication of two arrays
print(a*b)
print(np.multiply(a, b))

#  division of two arrays
print(a//b)
print(np.divide(a, b))

# mod of two arrays
print(a % b)
print(np.mod(a, b))

# power
print(a**b)
print(np.power(a, b))
