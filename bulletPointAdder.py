#! python3
"""
file: bulletPointAdder.py
author: Caleb M. McLaren, original by Al Sweigart
email: kbmclaren@gmail.com
date started: April 19th, 2022
most recent update: April 19th, 2022

description: bulletPointAdder.py must take text from the clipboard (part of OS),
	add a star and space to the beginning of each line,
	and then paste this new text to the clipboard.

example: 	list of animal		->	* list of animal
		list of aquarium life	->	* list of aquarium life
"""
#
#whatever is on clipboard become text variable string when bulletPointAdder.py is called.
#
import pyperclip
text = pyperclip.paste()
#
#Separate lines and add stars
#
tempList = text.split('\n')
for i in range(len(tempList)):
    if( tempList[i] == ''):
        continue
    else:
        tempList[i] = '* ' + tempList[i].strip()

#
#Now join the tempList elements back into a single string for the clipboard.
#
text = "\n".join(tempList)

#
#The variable "text" has been modified and is ready to be returned to clipboard for pasting to target doc
#
pyperclip.copy(text)	
