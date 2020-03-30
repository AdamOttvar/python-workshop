#!python3

# Lambda functions are small functions with only one expression
x = lambda a : a + 10
print(x(1))

# They can have multiple arguments
x = lambda a, b, c : a + b + c
print(x(1, 2, 3))

# Can be used like a generator
# This will return a function that multiplies an input
# with a certain number
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Lambda functions can be used in order to apply a function to all elements in a list
# the map function is used to apply a particular operation to every element in a sequence
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map(lambda x: x*x, sequences) 
print(list(filtered_result))

# Lambda functions might also be used for dictionaries
# and sorting a dictionary by the values
unsorted_dict = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
print(unsorted_dict.items())
sorted_dict = {key: value for key, value in sorted(unsorted_dict.items(), key=lambda item: item[1])}
print(sorted_dict)


##################
## Test yourself
##################
# Use the given data, that is temperature in Celsius and corresponding time, 
# convert Celsius to Fahrenheit and plot both Celsius and Fahrenheit
# To get the data you can execute the below code. This will give you one variable
# "temp_celsius" that is a list of temperatures in Celsius and
# "timestamp" that is a list of corresponding time for each temperature in epoch time.
with open('temperature_data.txt', 'r') as file: 
    for line in file: 
        exec(line)


# The below dictionary is the dimensions (in cm) of the boxes of some products from IKEA 
# (width, height, length)
# Sort the dictionary on the volume of the boxes, from biggest to smallest.
ikea_items = {'LINNMON': (60, 3, 100), 
              'MICKE': (76, 11, 111), 
              'PYSSLA': (13, 13, 13), 
              'ÄPPLARÖ': (45, 15, 109), 
              'IVAR': (41, 10, 87),
              'STARTTID': (33, 3, 38),
              'LUSTIGT': (17, 6, 21),
              'ALGOT': (4, 2, 85),
              'HELMER': (43, 7, 76),
              'LIXHULT': (37, 10, 38)}
