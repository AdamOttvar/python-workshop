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


# Test yourself
# Använda map för att ta en lista från Fahrenheit till Celsius
# Ge en krångligare dict som ska sorteras på ett visst värde
# Varor med olika priser som ska sorteras