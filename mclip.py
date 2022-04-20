#! python3


"""
file: mclip.py
author: Caleb M. McLaren, original by Al Sweigart
email: kbmclaren@gmail.com
date: April 12, 2022
description: mclip.py must take in a single key word and copy the corresponding long-form (from the file myGoodLines.txt) to the OS clipboard.
"""


import pyperclip
from sys import exit, argv

if( len(argv) < 2 ):
	print('Usage: python mclip.py [keyphrase]')              
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

# end mclip.py
