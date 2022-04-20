#! python3

"""
file: magicEightBall.py
author: Caleb M. McLaren, original by Al Sweigart
email: kbmclaren@gmail.com
date: April 6th, 2022
description: Magic eight ball program for command line execution.
"""


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
#return: string, random answer out of eight possible answers.
def shakeEightBall():
	for i in range(3):
		time.sleep(0.5)
		#Python is linebuffered by default. 
		#Print output is collected in the buffer until a newline is seen, then dumped.
		#Forcefully flush buffer to see this for loop print a dot, wait, print a dot, wait, etc.
		print('.', end='', flush=True)

	time.sleep(0.5)
	print('.', end='', flush=True)
	print(messages[random.randint(0, len(messages) - 1)])
	return

#name: main
#input: none
#return: none
#description: Request user input, handle user input, call main(), call shakeEightBall(), call sys.exit()
def main():
	user_input = ''
	while( user_input != 'n' ):
		user_input = input('Will you shake the magic 8 ball? (y/n): ')
		if( user_input == 'y' ):
			shakeEightBall()
	
	sys.exit(0)


if __name__ == "__main__":
	main()


# end magicEightBall.py
