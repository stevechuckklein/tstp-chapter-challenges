#1. Define a class called Apple with four instance variables that represent four attributes of an apple.

class Apple():
	def __init__(self, color, shape, typer, number):
		self.color = color
		self.shape = shape
		self.type = typer
		self.number = number
A1 = Apple("red", "circle", "fuji", 3)
print(A1.color, A1.type)

#2. Create a Circle class with a method called area that calculates and returns its area. Then create a Circle object, call area on it, and print the result. Use Python's pi function in the built-in math module.

import math

class Circle():
	def __init__(self, r):
		self.radius = r

	def area(self):
		return (self.radius ** 2) * math.pi

circle = Circle(5)
print (circle.area())

#3. Create a Triangle class with a method called area that calculates and returns its area. Then create a Triangle ojecct, call area on it, and print the result.

class Triangle():
	def __init__(self, b, h):
		self.base = b
		self.height = h

	def area(self):
		return 0.5 * self.base * self.height

triangle = Triangle(3,4)
print(triangle.area())

#4. Make a Hexagon class with a method called calculate_perimeter that calculates and returns it perimeter. Then create a Hexagon object, call calculate_perimeter on it, and print the result.

class Hexagon():
	def __init__(self, s):
		self.side = s

	def calculate_perimeter(self):
		return self.side * 6

hexy = Hexagon(7)
print(hexy.calculate_perimeter())

#Solution: http://tinyurl.com/gpqe62e