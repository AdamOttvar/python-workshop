#!python3
import numpy as np


##################
## Arrays
##################
# Create an array without numpy
a1 = [1, 2, 3, 4, 5]
print(a1)

# Create an array with numpy
a2 = np.array([1, 2, 3, 4, 5])
print(a2)

# Access array elements
print(a1[1])
print(a2[1])

# Create an array of all zeros
a = np.zeros((2,2))
print(a)

# Create an array of all ones
b = np.ones((1,2))
print(b)

# Create a constant array
c = np.full((2,2), 7)
print(c)

# Create a 2x2 identity matrix
d = np.eye(2)
print(d)

# Create an array filled with random values
e = np.random.random((2,2))
print(e)
print(e.shape)
print(e[0, 0], e[0, 1], e[1, 0])

##################
## Matrix
##################
a_mat = np.matrix("[1 2 3; 4 5 6]")
print(a_mat)


##################
## Operations
##################
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print('Addition: ')
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print('Subtraction: ')
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print('Multiplication: ')
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print('Division: ')
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print('Square root: ')
print(np.sqrt(x))


##################
## Matrix / Element wise
##################
print('Multiplication: ')
print(x @ y)
print(np.dot(x, y))