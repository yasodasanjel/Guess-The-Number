# Here is a guess game try

import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,100)   #this part of code allows the program to think one secret random number.
print("Well, " + myName + ",I am thinking of a number between 1 to 100")


while guessesTaken < 6:
	print("Take a guess.") 
	guess = input()
	guess = int(guess)

	guessesTaken = guessesTaken+1

	if guessesTaken < number:
		print("Your guess is too low")

	if guess > number:
		print("Your guess is too high")

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print("Good job, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")

if guess != number:
	number = str(number)
	print("Nope. The number I was thinking was " + number)
