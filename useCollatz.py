#file:useCollatz.py
#author: Caleb M. McLaren w/input from "Automate the Boring Stuff W/Python" 2nd Edition by Al Sweigart
#email: kbmclaren@gmail.com
#date: April 5th, 2022
#purpose: define a collatz function and encapsulate in program requesting user input of initial value. Proceed to print out results of collatz function. 

import time

#name: collatz
#input: string
#return: string
def collatz( number ):
	number_int = int( number )
	if( number_int == 1 ): 
		return str(number_int)

	elif( (number_int % 2) == 0 ):
		print(f'{ number_int // 2 }')
		time.sleep(0.1)
		return( str(number_int // 2) )
	else:
		print(f'{ (number_int * 3) + 1 }' )
		time.sleep(0.1)
		return( str((number_int * 3) + 1) )
#name: main
#input: none
#return: none
def main():
	#string type input
	user_number_input = input("Enter number: ")
	
	#keep calling collatz till return is 1.
	while( user_number_input != '1' ):
		user_number_input = collatz( user_number_input ) 

if __name__ == "__main__":
	main()
