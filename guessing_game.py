import sys
from random import randint

while True:
	print('Welcome to the Guessing Game!!! Choose your prefered difficulty level.')
	print('(easy - 0, 10; medium - 0, 100, hard - 0, 1000)')
	print('When you are ready try to guess the number')

	random_number = 0

	# selects the random number based on the chosen difficulty
	if(sys.argv[1].lower() == 'easy'):
		random_number = randint(0, 10)
	elif(sys.argv[1].lower() == 'medium'):
		random_number = randint(0, 100)
	elif(sys.argv[1].lower() == 'hard'):
		random_number = randint(0, 1000)

	# checks the user guess. If correct exits loop otherwise loops again
	while True:
		user_guess = input('What\'s the number: ')
		if(int(user_guess) == random_number):
			print('Yepp. You are right!')
			break
		else:
			print('You are wrong! Try again')

	# asks the user weather they want to play again
	play_again = input('Do you want to play again? (type yes or no)')
	if(play_again.lower() == 'yes'):
		continue
	else:
		break

