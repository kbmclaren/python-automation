#file: oxfordComma.py
#author: Caleb M McLaren
#email: kbmclaren@gmail.com
#date: April 7th, 2022
#description: oxfordComma must hold functions/program to take in a list value as an argument and 
#	return a string with all the items separated by a comma and a space, 
#	with an "and" inserted before the last item.
# ex: exampleList = ['apple', 'bannanna', 'orange'] => 'apple, bannanna, and orange'

from sys import exit

#name: applyCommaSeries
#input: single list
#return: single string, where input list items are comma-space separated & concatenated, 
#		with last item comma-space-and separated& concatenated. 
def applyCommaSeries( input_list ):
	return_string = ''
	
	#normal lists will have three or more items
	if (len(input_list) >= 3):
		#reverse concatenation
		input_list.reverse()

		#finish reverse concatenation
		for i in range(len(input_list)):
			if (i == 0):
				return_string = input_list[0]
			elif( i == 1 ):
				return_string = input_list[1] + ', and ' + return_string	
			else:
                		return_string = input_list[i] + ', ' + return_string

		return return_string 

	elif( len(input_list) == 2 ):
		#create string in style of "value1 and value2"
		return input_list[0] + ' and ' + input_list[1]
	else:
		#empty list or list of one
		return input_list[0]


#name: main
#input: on start up, prompt user for input until keyword 'exit'. Empty input accepted.
#output: print expected concatenated string holding all entries.
def main():

	list_to_convert = []
	user_list_value_input = input('Please input one item of your list (or input \'exit\' to stop input): ')

	while( user_list_value_input.lower() != 'exit'  ):
		#append user input to list
		list_to_convert.append(user_list_value_input)
		user_list_value_input = input('Please input one item of your list (or input \'exit\' to stop input): ')
		
	if( user_list_value_input.lower() == 'exit' and len(list_to_convert) == 0 ):
		exit()

	#list created, call for concatenation function
	print( applyCommaSeries(list_to_convert) )	

if __name__ == '__main__':
	main()
