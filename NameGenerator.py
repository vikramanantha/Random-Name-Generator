import random
import os

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
cons = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'y', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
real_name = ''

def one(real_name):
	fir = random.choice(vowels)
	real_name += fir.upper()	
	input("Your randomized name 1 letter name is " + real_name + ".")
	main()

def two(real_name):
	fir = random.choice(cons)
	real_name += fir.upper()
	sec = random.choice(vowels)
	real_name += sec	
	input("Your randomized name 2 letter name is " + real_name + ".")
	main()

def three(real_name):
	fir = random.choice(cons)
	real_name += fir.upper()
	sec = random.choice(vowels)
	real_name += sec
	thir = random.choice(cons)
	real_name += thir	
	input("Your randomized name 3 letter name is " + real_name + ".")
	main()

def four(real_name):
	fir = random.choice(cons)
	real_name += fir.upper()
	sec = random.choice(vowels)
	real_name += sec
	thir = random.choice(cons)
	real_name += thir	
	four = random.choice(vowels)
	real_name += four
	input("Your randomized name 4 letter name is " + real_name + ".")
	main()

def five(real_name):
	fir = random.choice(cons)
	real_name += fir.upper()
	sec = random.choice(vowels)
	real_name += sec
	thir = random.choice(cons)
	real_name += thir	
	four = random.choice(vowels)
	real_name += four
	fif = random.choice(cons)
	real_name += fif
	input("Your randomized name 5 letter name is " + real_name + ".")
	main()

def six(real_name):
	fir = random.choice(cons)
	real_name += fir.upper()
	sec = random.choice(vowels)
	real_name += sec
	thir = random.choice(cons)
	real_name += thir	
	four = random.choice(cons)
	real_name += four
	fif = random.choice(vowels)
	real_name += fif
	six = random.choice(cons)
	real_name += six
	input("Your randomized name 6 letter name is " + real_name + ".")
	main()

def seven(real_name):
	fir = random.choice(cons)
	real_name += fir.upper()
	sec = random.choice(vowels)
	real_name += sec
	thir = random.choice(cons)
	real_name += thir	
	four = random.choice(cons)
	real_name += four
	fif = random.choice(vowels)
	real_name += fif
	six = random.choice(cons)
	real_name += six
	sev = random.choice(cons)
	real_name += sev
	input("Your randomized name 7 letter name is " + real_name + ".")
	main()

def eight(real_name):
	fir = random.choice(vowels)
	real_name += fir.upper()
	sec = random.choice(cons)
	real_name += sec
	thir = random.choice(cons)
	real_name += thir	
	four = random.choice(vowels)
	real_name += four
	fif = random.choice(cons)
	real_name += fif
	six = random.choice(vowels)
	real_name += six
	sev = random.choice(cons)
	real_name += sev
	eit = random.choice(vowels)
	real_name += eit
	input("Your randomized name 8 letter name is " + real_name + ".")
	main()

def nine(real_name):
	fir = random.choice(cons)
	real_name += fir.upper()
	sec = random.choice(vowels)
	real_name += sec
	thir = random.choice(vowels)
	real_name += thir	
	four = random.choice(cons)
	real_name += four
	fif = random.choice(cons)
	real_name += fif
	six = random.choice(vowels)
	real_name += six
	sev = random.choice(cons)
	real_name += sev
	eit = random.choice(vowels)
	real_name += eit
	nin = random.choice(cons)
	real_name += nin
	input("Your randomized name 9 letter name is " + real_name + ".")
	main()

def ten(real_name):
	fir = random.choice(cons)
	real_name += fir.upper()
	sec = random.choice(vowels)
	real_name += sec
	thir = random.choice(cons)
	real_name += thir	
	four = random.choice(cons)
	real_name += four
	fif = random.choice(vowels)
	real_name += fif
	six = random.choice(vowels)
	real_name += six
	sev = random.choice(cons)
	real_name += sev
	eit = random.choice(vowels)
	real_name += eit
	nin = random.choice(cons)
	real_name += nin
	ten = random.choice(vowels)
	real_name += ten
	input("Your randomized name 10 letter name is " + real_name + ".")
	main()

def main():
	os.system('cls')
	print("This is a name generator! It will randomly generate a name.")
	namenum = input("Type any number for the number of letters you want the name to be. 10 is the limit for the number of letters you can have the name be. \nType 'Q' to quit \nHit 'Enter' for a random number. \n")

	if namenum == '1':
		one(real_name)

	elif namenum == '2':
		two(real_name)

	elif namenum == '3':
		three(real_name);

	elif namenum == '4':
		four(real_name);

	elif namenum == '5':
		five(real_name);

	elif namenum == '6':
		six(real_name); 

	elif namenum == '7':
		seven(real_name);

	elif namenum == '8':
		eight(real_name);

	elif namenum == '9':
		nine(real_name);

	elif namenum == '10':
		ten(real_name);

	elif namenum == 'q' or namenum == 'Q':
		quit()

	else:
		rannum = random.randrange(3, 11)

		if rannum == 3:
			three(real_name)

		elif rannum == 4:
			four(real_name)

		elif rannum == 5:
			five(real_name)

		elif rannum == 6:
			six(real_name)

		elif rannum == 7:
			seven(real_name)

		elif rannum == 8:
			eight(real_name)

		elif rannum == 9:
			nine(real_name)

		elif rannum == 10:
			ten(real_name)

main()

