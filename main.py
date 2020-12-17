import random

guessesTaken = 0

myName = input("Hello! What is your name? \n")

topNum = int(input("How many numbers to choose from? "))

numGuesses = int(input("How many guesses do you want? "))

number = random.randint(1, topNum)

print("Well, " + myName + ", I am thinking of a number between 1 and " + str(topNum) + ".")

while guessesTaken < numGuesses:

	guess = int( input("Take a guess. \n") )
	guessesTaken += 1

	if guess < number:
		print("Your guess is too low.") 

	if guess > number:
		print("Your guess is too high.")

	if guess == number:
		break

if guess == number:
	print("Good job, " + myName + "! You guessed my number in " + str(guessesTaken) + " guesses!")

if guess != number:
	print("Nope. The number I was thinking of was " + str(number) ) 