# Variables (We can use characters, numbers and underscore to a label of a variable)

# _some = 5
# _some_value = 10
# value2 = 5
# some = 2
# value_2 = 3
# HEIGHT = 8
# Height = "String"

# Expressions and statements

# Expressions return a value
# 1+1
# "smth"

# Statements do some operations with a value
# number = 1
# print(number)
# name = "John"; print(name)
# Space (Indentation) and tabulations have a spacial meaning in Python
 
# Data types

# String
# name = "Clark"
# print(type(name)) # <class 'str'>
# type() is a function to feagure out what type has a value
# print(type(name) == str)
# isinstance(value, type that we want to compare to)
# print(isinstance(name, str)) # True

# Integer
# age = 2 
# print(isinstance(age, int))

# Float (Decimal number)
# float_number = 4.56
# print(isinstance(float_number, float))

# Convert from one type to anoter
# number = float(2)
# print(isinstance(number, float)) # True

# number = "5"
# string_number = int(number) # Casting from integer to string
# print(isinstance(string_number, int)) # True

# Types in Python:
# int for integers
# str for strings
# float for decimal numbers
# comlex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets

# Operators

#Arithmetic Operators
1 + 1 #2 Addition
2 - 1 #1 Subtraction
2 * 2 #4 Multiplication
4 / 2 #2 Division
4 % 3 #1 Remainder
4 ** 2 #16 Exponentiation
4 // 2 #2 Floor division rounds down 
# In Python, we can perform floor division (also sometimes known as integer division) using the // operator. This operator will divide the first argument by the second and round the result down to the nearest whole number, making it equivalent to the math. floor() function
1 + -1 #0

# print("Champ " + "is a good boy " + str(5))

# age = 8 
# age += 8 # 16

# Comparison Operators

# a = 1
# b = 2

# a == b # False
# a != b # True
# a > b # False
# a <= b # True

# Boolean Operators

condition1 = True
condition2 = False

not condition1 # False
condition1 and condition2 # False
condition1 or condition2 # True

# or returns first value that is not False, otherwise it returns a last operand
# print(0 or 1) ## 1
# print(False or 'hey') ## 'hey'
# print('hi' or 'hey') ## 'hi'
# print([] or False) ## 'False'
# print(False or []) ## '[]'

# and returns first value that is False, otherwise it returns a last operand
# print(0 and 1) ## 0
# print(1 and 0) ## 0
# print(False and 'hey') ## False
# print('hi' and 'hey') ## 'hey'
# print([] and False) ## []
# print(False and []) ## False

# Bitwise Operators

# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation (an invertion)
# << shift left operation
# >> shift right operation

# is & in Operators

# is - an identity operator (is used to compare 2 objects and returns True if both are the same object)
# in - a membership operator (is a value contains in a list or another sequence)

# Ternary Operator

# Without the Ternary Operator
def is_adult(age):
	if age > 18:
		return True
	else:
		return False

# Using the Ternary Operator
def is_adult2(age):
	return True if age > 18 else False

# Strings

# "Ham"
# 'Ham'
# name = "Peter"
# sentence = "Peter" + " is my name."
# sentence2 = name + " is my name."
# name += " is my name." # the same as the previous line
# age = str(39)

# A multiline string
# print("""Peter is
# 
# 18
# 		
# years old
# """)

# String Methods

# print("peter".upper()) # PETER
# print("PETER".lower()) # peter
# print("pETer person".title()) # Peter Person (Capitalizes all words in a sentence)
# print("Peter".islower()) # False
# print("PETER".isupper()) # True

# isalpha() to check if a string contains only characters and is not empty
# isalnum() to check if a string contains characters or digits and is not empty
# isdecimal() to check if a string contains digits and is not empty
# lower() to get a lowercase version of a string
# islower() to check if a string is lowercase
# upper() to get an uppercase version of a sting
# isupper() to check if a string is uppercase
# title() to get a capitalized version of a string
# startswith() to check if the string starts with a specific substring
# endswith() to check if the string ends with a specific substring
# replace() to replace a part of a string
# split() to split a string on a specific character separator
# strip() to trim the whitespace from start and finish of a string
# join() to append new letters to a string
# find() to find the position of a substring

