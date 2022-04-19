#! python3
#file: mclip.py
#author: Caleb M. McLaren & Al Sweigart
#email: kbmclaren@gmail.com
#date: April 12, 2022
#description: chapter project - this command line tool must take in a single key word and copy the corresponding long-form to the OS clipboard.

import pyperclip
from sys import exit, argv

if( len(argv) < 2 ):
	print('Usage: python mclip.py [keyphrase]')              
	#sys.exit()
	exit()

keyphrase = argv[1] 	#first command line arg is the keyphrase

with open('myGoodLines.txt', 'r') as textFile:
	for line in textFile:
		key, val = line.strip().split('=')
		if( keyphrase == key ):
			pyperclip.copy(val)
			print("Text for " + keyphrase.upper() + " copied to clipboard.")
			exit()

print("There is no text for " + keyphrase.upper())




#TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
#	'busy': """Sorry, can we do this later this week or next week?""",
#	'upsell': """Would you consider making this a monthly get together?"""}

#if(keyphrase in TEXT):
#	pyperclip.copy(TEXT[keyphrase])
#	print("Text for " + keyphrase + " copied to clipboard.")
#else:
#	print("There is no text for " + keyphrase)
