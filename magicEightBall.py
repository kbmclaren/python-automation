#file: magicEightBall.py
#author: Caleb M. McLaren
#email: kbmclaren@gmail.com
#date: April 6th, 2022
#description: Magic eight ball program for command line execution.
#future: convert main from recursive to while loop

import sys, random, time

messages = ['It is certain',
		'It is decidedly so',
		'Yes definitely', 
		'Reply hazy try again',
		'Ask again later',
		'Concentrate and ask again',
		'My reply is no',
		'Outlook no so good',
		'Very doubtful']

#name: shakeEightBall
#input: none
#return: random answer out of eight possible answers.
def shakeEightBall():
	for i in range(3):
		#print('.', end='')
		time.sleep(0.5)
		print('.', end='')

	print(messages[random.randint(0, len(messages) - 1)])
	return

#name: main
#input: none
#return: none
#description: Request user input, handle user input, call main(), call shakeEightBall(), call sys.exit()
def main():
	user_input = input('Will you shake the magic 8 ball? (y/n): ')
	
	#no input
	if( user_input == '' ):
		main()
	elif( user_input == 'n'):
		sys.exit(0)
	else:
		shakeEightBall()
		main()

if __name__ == "__main__":
	main()

