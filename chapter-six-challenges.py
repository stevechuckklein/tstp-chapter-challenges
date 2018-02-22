#1. Print every character in the string "Camus".

for let in "Camus":
	print(let)

#2. Write a program that collects two strings from a user, inserts them into the string "Yesterday I wrote a [response_one]. I sent it to [response_two]!" and prints a new string.

# orig = "Yesterday I wrote a [response_one]. I sent it to [response_two]!"
# print(orig)
# first = input("What would you like to replace [response_one] with? ")
# second = input("What would you like to replace [response_two] with? ")
# orig = "Yesterday I worte {}. I sent it to {}!".format(first, second)
# print(orig)

#3. Use a method to make the string "aldous Huxley was born in 1894." grammatically correct by capitalizing the first letter in the sentence.

thre = "aldous Huxley was born in 1894."
print(thre.capitalize())

#4. Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like: ["Where now?", "Who now?", "When now?"].

# This is his answer (not what he actually asked for...)
lst = "Where now? Who now? When now?".split("?")
print(lst)

#This is what he actually asked for
senten = "Where now? Who now? When now?"
stringer = ""
result = []
for let in senten:
	stringer = stringer + let
	if let == "?":
		if stringer[0] == " ":
			result.append(stringer[1:])
		else:
			result.append(stringer)
		stringer = ""
print(result)

#5. Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn into a grammatically correct string. There should be a space between each word, but no space between the word fence and the period that follows it. (Don't forget, you learned a method that turns a list of strings into a single string.)

fiv = ["The", "fox", "jumped", "over", "the", "fence", "."]
fiv = " ".join(fiv[:6]) + fiv[6]
print(fiv)

#6. Replace every instance of "S" in "A screaming comes across the sky." with a dollar sing.

chal6 = "A screaming comes across the sky."
chal6 = chal6.replace("s", "$")
print(chal6)

#7. Use a methodto find the first index of the character "m" in the string "Hemingway".

chal7 = "Hemingway"
print(chal7.index("m"))

#8. Find dialogue in your favorite book (containing quotes) and turn it into a string.

chal8 = "\"Wow!\" she said. \"This is a stupid challenge\" Kurt interrupted."
print(chal8)

#9. Create the string "three three three" using concatenation, and then again using multiplicaton.

chal9a = "three " + "three " + "three"
print(chal9a)
chal9b = "three " * 3
print(chal9b[:-1])

#10. Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to only include the charcters before the comma.

chal10 = "It was a bright cold day in April, and the cocks were striking thirteen."
comma = chal10.index(",")
chal10 = chal10[:comma]
print(chal10)

#Solutions: http://tinyurl.com/hapm4dx