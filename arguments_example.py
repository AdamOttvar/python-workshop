#!python3

##################
## Annotations
##################

# When you write your function you might want to have arguments to that function
# These can be handled in different ways.
# The straight forward way is that you specify what arguments that are needed
def first_function_w_args(first_arg, second_arg, third_arg):
    result_of_args = first_arg + second_arg + third_arg
    return result_of_args

print(first_function_w_args(1, 2, 3))

# Nothing fancy here, but if we take a look at the function we could use it in
# another way

print(first_function_w_args('Does', ' this', ' work?'))

# Python is not keen on declaring types, but there is a way to guide the 
# person who should use the function to what type of inputs are desired.

def second_function_w_args(first_arg: str, second_arg: str, third_arg: str) -> str:
    result_of_args = first_arg + second_arg + third_arg
    return result_of_args

# This will not be enforced by the intrepreter, but can be used to make things more
# clear for a user. Both cases from before will still work

print(second_function_w_args(1, 2, 3))
print(second_function_w_args('Does', ' this', ' work?'))


##################
## Named arguments
##################

# There are ways to make some arguments optional and is often solved by
# so called "named arguments"
def third_function_w_args(number, string='Default'):
    print('Number: {}'.format(number))
    print('String: ' + string)

third_function_w_args(3, 'Given string')
third_function_w_args(3)
try:
    third_function_w_args()
except Exception as e:
    print('ERROR!!')


##################
## Variable length arguments *args
## "non-keyworded" 
##################
# Sometimes it can be usefull to have variable amount of input arguments
# This can be handled in different ways. When using *args the function will
# expect a variable length of "non-keyworded" list of arguemnts
# Python program to illustrate 
# *args for variable number of arguments 
def forth_function_w_args(*argv):
    for arg in argv:
        print (arg)

forth_function_w_args('List', 'of', 'input', 'arguments')

# It can be used in combination with "normal" arguments
def fifth_function_w_args(first_arg, *argv):
    print('First argument: {}'.format(first_arg))
    for arg in argv:
        print (arg)

fifth_function_w_args('List', 'of', 'input', 'arguments')
fifth_function_w_args('Only one')

##################
## Variable length arguments **kwargs
## "keyworded" 
##################
def sixth_function_w_args(**kwargs):
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 

sixth_function_w_args(first='first', second='second', third='third')

# It can be used in combination with "normal" arguments
def seventh_function_w_args(first_arg, **kwargs):
    print('First argument: {}'.format(first_arg))
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value))

seventh_function_w_args(first_arg='first', second='second', third='third')
seventh_function_w_args('Only one')

##################
## Command Line Arguments
##################
# A python script is often run from the command line, or somewhere else
# and by others than the one that created it. It can therefore be useful
# to give a little help to what arguments that are available

# This line is to decide what happens when the script is run from outside.
# It can be used when you have created a Class and used for giving some examples on
# how the class can be used. A very usefull module for this is argparse.
import argparse

def return_absoulte_value(value):
    return abs(value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example for input arguments. Returns the value or its absolute value.')
    parser.add_argument('first_arg', type=int,
                        help='an integer example argument')
    parser.add_argument('--absolute', action='store_true',
                        help='return the absolute value')

    args = parser.parse_args()
    if args.absolute:
        print(return_absoulte_value(args.first_arg))
    else:
        print(args.first_arg)



##################
## Test yourself
##################
# Create two functions
