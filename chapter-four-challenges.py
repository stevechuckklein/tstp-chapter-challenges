#1. Write a function that takes a number as an input and returns that number squared.

def sqsquared(x):
	"""
	Returns x squared.
	:param x: int.
	:return: int of x squared.
	"""
	return x ** 2

#2. Create a function that accepts a string as a parameter and prints it.

def print_string(stringy):
	"""
	Check if input is string, convert if not, then print the string.
	:param stringy: str.
	"""
	if isinstance(stringy, str) == True:
		print(stringy)
	else:
		print(str(stringy))

#3. Write a function that takes three requred parameters and two optional parameters.

def sum_param(x,y,z,a=2,b=3):
	"""
	Takes 3 required params and 2 optional params then returns their sum.
	:param x: int.
	:param y: int.
	:param z: int.
	:param a: int.
	:param b: int.
	:return: int of the sum of params.
	"""
	return x+y+z+a+b

#4. Write a program with two functions. The first function should take an integer as a parameter and return the result of the integer divided by 2. The second function should take an integer as a parameter and return the result of the integer multiplied by 4. Call the first function, save the result as a variable, and pass it as a parameter to the second function.

def divid(x):
	"""
	Returns half of x.
	:param x: int.
	:return: int half of x.
	"""
	return x / 2

def mult4(y):
	"""
	Returns 4 times y.
	:param y: int.
	:return: int of y multiplied by 4.
	"""
	return y * 4

first = divid(3)
print(mult4(first))

#5. Write a function that converts a string to a float and returns the result. Use exception handling to catch the exception that could occur.

def floatem(stringer):
	"""
	Converts a string to a float or prints an error message.
	:param stringer: str.
	:return: string converted to float.
	"""
	try:
		return float(stringer)
	except(ValueError):
		print("Invalid input.")

print(floatem("200"))
print(floatem("2.234"))
floatem("this")

#6 Add a docstring to all of the functions you wrote in challenges 1-5.

# Solutions: http://tinyurl.com/hkzgqrv.