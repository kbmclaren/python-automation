#file: characterCount.py
#author: Caleb M McLaren
#email: kbmclaren@gmail.com
#date: April 8th, 2022
#description: use built in setdefault() of python dictionaries to implement 
#	simple counting sort/incident count 

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] += 1

pprint.pprint(count)

#end characterCount.py
