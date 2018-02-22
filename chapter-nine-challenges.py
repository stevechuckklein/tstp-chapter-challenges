#1. Find a file on your computer and print its contents using Python. 

filer = open("dummy.txt", "r")
print(filer.read())
filer.close()

#2. Write a program that asks a user a question, and saves their answer to a file.

answer = input("Hello?")

with open("ch9-two.txt","w") as f:
	f.write(answer)

#3. Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] and write them to a CSV file. The data from each list should be a row in the file, with each item in the list separated by a comma.

import csv

lister = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movie.csv", "w", newline=",") as f:
	w = csv.writer(f, delimiter=",")
	for movies in lister:
		w.writewrow(movies)

#Solutions: http://tinyurl.com/hll6t3q