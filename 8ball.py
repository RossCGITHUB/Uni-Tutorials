import sys 
import random

ans = True

while ans:
	question = raw_input("ask the magic 8 ball a question: (enter quit to quit)")

	answers = random.randint(1,10)

	if question == "quit":
		sys.exit()

	elif question == "am I a numpty":
		print "Aye"

	elif answers == 1:
		print "Nae Vay!"

	elif answers == 2:
		print "Outlook Worrying"

	elif answers == 3:
		print "You will not pass!"

	elif answers == 4:
		print "Dont ask again"

	elif answers == 5:
		print "Concentrate and squeeze it out"

	elif answers == 6:
		print "You will be hit by a car soon"

	elif answers == 7:
		print "Leave home you're in danger"

	elif answers == 8:
		print "Ayee it's gonna happen buddy"


	elif answers == 9:
		print "Hodor"

	elif answers == 10:
		print "Your dog has tits"