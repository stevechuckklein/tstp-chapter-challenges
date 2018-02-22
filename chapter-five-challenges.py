#1. Create a list of your favorite musicians.

fav_music = ["k-dot", "Fall out boy", "Bruce Springsteen"]

#2. Create a list of tuples, with each tuple containing the longitude and latitude of somewhere you've lived or visited.

lived_in = [(41.8781, 87.6298), (36.1627, 86.7816)] #Chicago , Nashville

#3. Create a dictionary that contains different attributes about you: height, favorite color, favorite author, etc...

attributies = {"height": "6ft",
							 "favorite color": "blue",
							 "favorite author": "Brandon Sanderson"}

#4. Write a program that lets the user ask your height, favorite color, or favorite author, and returns the result from the dictionary you created in the previous challenge.

response = input("What would you like to know about me? My height, my favorite color, or my favorite author?? ")

if response in attributies:
    print(attributies[response])
else:
    print("You did not choose one of the options.")

#5. Create a dictionary mapping your favorite musicians to a list of your favorite songs by them.

songs = {"k-dot": "humble",
				 "Fall out boy": "Sugar we're goin' down",
				 "Bruce Springsteen": "Dancing in the dark"}

#6. Lists, tuples, and dictionaries are just a few of the containers built into Python. Research Python sets (a type of container). When would you use set?

ans_six = "use set when you want to link everything in a mutable together."
#a longer, better answer: https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set

#Solutions: http://tinyurl.com/z54w9cb