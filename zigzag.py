#file: zigzag.py
#author: Caleb M. McLaren
#email: kbmclaren@gmail.com
#date-started: April 5th, 2022
#purpose: A program to print out a group of stars in a zig-zag pattern on the command line.

#need sys.exit(), and 
import time, sys 
indent = 0 			#Spaces to indent
indentIncreasing = True 	#Whether the indentation is increasing or not.

try:
	while( True ): 		#The main program loop
		print( ' ' * indent, end='' )
		print( '********' )
		time.sleep( 0.1 )

		if( indentIncreasing ):
			#Increase the number of spaces
			indent += 1
			if( indent == 20 ):
				#Change direction
				indentIncreasing = False

		else:
			#Decrease the number of spaces
			indent -= 1
			if( indent == 0 ):
				#Change direction
				indentIncreasing = True
except KeyboardInterrupt:
	sys.exit()

#end zigzag.py
