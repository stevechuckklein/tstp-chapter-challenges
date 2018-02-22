#1) Print three different strings.

print("This is string one.")
print("This is string 2.")
print("This is string 3.")

#2) Write a program that prints a message if a variable is less than 10, and different message if the variable is greater than or equal to 10

x = 11
if x < 10:
	print("This number is less than 10.")
else:
	print("This number is greater than 10.")

#3) Write a program that prints a message if a variable is less than or equal to 10, another message if the variable is greater than 10 but less than or equal to 25, and another message if the variable is greater than 25

x = 10
if x <= 10:
	print("This number is less then or equal to 10.")
elif x > 10 and x <= 25:
	print("This number is inbetween 10 and 25.")
else:
	print("This number is greater than 25.")

#4) Create a program that divides two variables and prints the remainder.

x = 38
y = 14
print(x % y)

#5) Create a program that takes two variables, divides them, and prints the quotient.

print(x // y)

#6) Write a program with a variable "age" assigned to an integer that prints different strings depending on what integer "age" is.

age = 25
if age >= 25:
	print("You're still young.")
else:
	print("You're old as fuck.")

# Solutions: http://tinyurl.com/zx7o2v9