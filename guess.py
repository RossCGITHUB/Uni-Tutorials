print "welcome to guess the number"
number = 10
guess = int(raw_input("Enter a Guess"));

if guess == number:
	print "You have guessed correctly my son"

elif guess > number:
	print "the number is too big"

elif guess < number:
	print "the number is too low"

else: 
	print "you have not entered a number"