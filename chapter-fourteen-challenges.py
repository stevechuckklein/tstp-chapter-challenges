#1. Add a square_list variable to a class called Square so that every time you create a new Square object, the new object gets added to the list.

# class Square():
# 	square_list = []

# 	def __init__(self, side):
# 		self.side = side
# 		self.square_list.append(self)

# sq1 = Square(5)
# sq2 = Square(10)
# print(Square.square_list)

#2. Change the Square class so that when you print a Square object, a message prints telling you the len of each of the four sides of the shape. For example, if you create a square with Square(29) and print it, Python should print 29 by 29 by 29 by 29.

class Square():
	square_list = []

	def __init__(self, side):
		self.side = side
		self.square_list.append(self)

	def __repr__(self):
		return "{} by {} by {} by {}".format(self.side,self.side,self.side,self.side)

print(Square(5))

#3. Write a function that takes two objects as parameters and returns True if they are same object, and False if not.

def obj_compare(object1, object2):
	return object1 is object2

obj1 = Square(5)
obj2 = obj1
obj3 = Square(3)
obj4 = Square(5)

print(obj_compare(obj1, obj2))
print(obj_compare(obj1, obj3))
print(obj_compare(obj1, obj4))

#Solutions: http://tinyurl.com/j9qjnep