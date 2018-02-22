#1. Print each item in the following list: ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"].

chal1 = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for i in chal1:
	print(i)

#2. Print all the numbers from 25 to 50.

for i in range(25,51):
	print(i)

#3. Print each item in the list from the first challenge and their indexes.

i=0
for entry in chal1:
	print(entry, i)
	i += 1

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, show in enumerate(shows):
    print(index)
    print(show)

#4. Write a program with an inifinite loop (with the option to type q to quit) and a list of numbers. Each time through the loop ask the user to guess a number on the list and tell them whether or not they guessed correctly.

# lister = [4,5,7,9]
# while True:
# 	print("Type q to quit")
# 	ans = input("Guess a number in the list.")
# 	if ans == "q":
# 		break
# 	elif ans in lister:
# 		print("Good guess, you got it.")
# 	else:
# 		print("Wrong, try again")

#5. Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in the list [9, 1, 33, 83], and append each result to a third list.

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
result = []

for num1 in list1:
	for num2 in list2:
		result.append(num1 * num2)
print(result)


#Solutions: http://tinyurl.com/z2m2ll5