#! python3

"""
file: characterCount.py
author: Caleb M McLaren
email: kbmclaren@gmail.com
date: April 8th, 2022
description: use built in setdefault() of python dictionaries to implement 
	simple incident count of characters seen in message. 
"""

import pprint

message = input('Please input a simple message: ')
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] += 1

pprint.pprint(count)

#end characterCount.py
