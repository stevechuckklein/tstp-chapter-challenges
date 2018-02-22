#1. Create Rectangle and Square classes with a method called calculate_perimeter that calculates the perimeter of the shapes they represent. Create Rectangle and Square objects and call the method on both of them.

# class Rectangle():
# 	def __init__(self, l, w):
# 		self.width = w
# 		self.length = l

# 	def calculate_perimeter(self):
# 		return (self.width*2) + (self.length*2)

# class Square():
# 	def __init__(self, s):
# 		self.side = s

# 	def calculate_perimeter(self):
# 		return self.side * 4

# my_rec = Rectangle(10, 5)
# print(my_rec.calculate_perimeter())
# my_squ = Square(2)
# print(my_squ.calculate_perimeter())


#2. Define a method in you Square class called change_size that allows you to pass in a number that increases or decreases (if the number is negative) each side of a Square object by that number.

# class Rectangle():
# 	def __init__(self, l, w):
# 		self.width = w
# 		self.length = l

# 	def calculate_perimeter(self):
# 		return (self.width*2) + (self.length*2)

# class Square():
# 	def __init__(self, s):
# 		self.side = s

# 	def calculate_perimeter(self):
# 		return self.side * 4

# 	def change_size(self, num):
# 		self.side = self.side + num

# my_square = Square(5)
# print(my_square.side)
# my_square.change_size(-2)
# print(my_square.side)

#3. Create a class called Shape. Define a method in it called what_am_i that prints "I  am a shape" when called. Change your Square and Rectangle classes from the previous challenges to inherit from Shape, create Square and Rectangle objects, and call the new method on both of them.

class Shape():
	def what_am_i(self):
		return "I am a shape"

class Rectangle(Shape):
	def __init__(self, l, w):
		self.width = w
		self.length = l

	def calculate_perimeter(self):
		return (self.width*2) + (self.length*2)

class Square(Shape):
	def __init__(self, s):
		self.side = s

	def calculate_perimeter(self):
		return self.side * 4

	def change_size(self, num):
		self.side = self.side + num

i_rec = Rectangle(10, 15)
i_squ = Square(4)
print(i_rec.what_am_i(), i_squ.what_am_i())

#4. Create a class called Horse and a class called Rider. Use composition to model a horse that has a rider.

class Horse():
	def __init__(self, name, owner):
		self.name = name
		self.owner = owner

class Rider():
	def __init__(self, name):
		self.name = name

cowboy = Rider("cowboy")
horsy = Horse("horsy", cowboy)
print(horsy.owner.name)

#Solutions: http://tinyurl.com/hz9qdh3