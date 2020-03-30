#!python3
import numpy as np

##################
## Arrays
##################
# Create an array without numpy
a1 = [1, 2, 3, 4, 5]
print('List:\n{}\n'.format(a1))

# Create an array with numpy
a2 = np.array([1, 2, 3, 4, 5])
print('Array:\n{}\n'.format(a2))


# Access array elements
print('Access elements')
print('List: a1[1]\n{}\n'.format(a1[1]))
print('Array: a2[1]\n{}\n'.format(a2[1]))


# Create an array of all zeros
a = np.zeros((2,2))
print('Zeros:\n{}\n'.format(a))

# Create an array of all ones
b = np.ones((1,2))
print(b)
print('Ones:\n{}\n'.format(b))

# Create a constant array
c = np.full((2,2), 1337)
print('Full:\n{}\n'.format(c))

# Create a 2x2 identity matrix
d = np.eye(2)
print('Eye:\n{}\n'.format(d))

# Create an array filled with random values
e = np.random.random((2,2))
print('Random:\n{}\n'.format(e))
print('Shape:\n{}\n'.format(e.shape))
print('Access:\n{}\n'.format(e.shape))
print(e[0, 0], e[0, 1], e[1, 0])

##################
## Matrix
##################
# One can create a Matrix with numpy,
# this is however not widely used and will probably be 
# depricated in the future.
# A matrix will effect how operations are performed, for example
# when element wise or dot product is used.
a_mat = np.matrix("[1 2; 3 4]")
b_mat = np.matrix("[5 6; 7 8]")
print('Matrix A:\n{}\n'.format(a_mat))
print('Matrix B:\n{}\n'.format(b_mat))

print('Multiplication: ')
print('a_mat * b_mat =\n{}\n'.format(a_mat * b_mat))
print('np.multiply(a_mat, b_mat) =\n{}\n'.format(np.multiply(a_mat, b_mat)))

##################
## Operations
##################
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print('Addition: ')
print('x + y =\n{}\n'.format(x + y))
print('np.add(x, y) =\n{}\n'.format(np.add(x, y)))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print('Subtraction: ')
print('x - y =\n{}\n'.format(x - y))
print('np.subtract(x, y) =\n{}\n'.format(np.subtract(x, y)))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print('Multiplication: ')
print('x * y =\n{}\n'.format(x * y))
print('np.multiply(x, y) =\n{}\n'.format(np.multiply(x, y)))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print('Division: ')
print('x / y =\n{}\n'.format(x / y))
print('np.divide(x, y) =\n{}\n'.format(np.divide(x, y)))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print('Square root: ')
print('np.sqrt(x) =\n{}\n'.format(np.sqrt(x)))


##################
## Matrix operations
##################
print('Dot product: ')
print('x @ y =\n{}\n'.format(x @ y))
print('x.dot(y) =\n{}\n'.format(x.dot(y)))
print('np.dot(x, y) =\n{}\n'.format(np.dot(x, y)))


##################
## Computational speed
##################
# We will compare the computational speed of doing dot product
# using lists and numpy arrays
import time
list1 = [i for i in range(1000000)]
list2 = [i for i in range(1000000)]

dot_product_list = 0
start_time_list = time.time()
for i,j in zip(list1, list2):
    dot_product_list += i*j
end_time_list = time.time()
print('Time for list: {}'.format(end_time_list - start_time_list))

array1 = np.array(list1)
array2 = np.array(list2)
start_time_array = time.time()
dot_product_array = np.dot(array1, array2)
end_time_array = time.time()
print('Time for array: {}'.format(end_time_array - start_time_array))
