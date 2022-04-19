#file: exitExample.py
#author: Caleb M McLaren
#date: April 4th, 2022
#purpose: see the use of system.exit()

#'import sys' over 'from sys import *' so we still have to write 'sys.exit()' vs 'exit()' 
import sys

while True:
	print("Type /'exit/' to exit program.")
	response = input(); 
	if( response == 'exit'):
		sys.exit()
	print(f'You typed {response} .')
