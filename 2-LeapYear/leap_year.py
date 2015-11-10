# -*- coding: utf-8 -*-

in_process = True

while in_process:
	year = raw_input("Type a year: \n")

	try:
		year = int(year) 
	except ValueError:
		print("Please type a valid year...")
		continue

	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
		print(str(year) + " is a leap year! :)") 
	else: 
		print(str(year) + " is not a leap year :(") 
			
	again = raw_input("Retry? (y/n)") 
	if again == "n" or again == "N": 
		in_process = False
		print("See you soon!")
	else: 
		continue 


