#! python3

"""
file: exitExample.py
author: Caleb M McLaren, original by Al Sweigart
date: April 4th, 2022
purpose: see the use of system.exit()
"""


#'import sys' over 'from sys import *' so we still have to write 'sys.exit()' vs 'exit()' 
import sys

while True:
	response = input("Type /'exit/' to exit program: "); 
	if( response == 'exit'):
		sys.exit()
	print(f'You typed "{response}".')

# end exitExample.py
