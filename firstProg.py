#! python3

"""
file: firstProg.py
author: Caleb M. McLaren, original by Al Sweigart.
email: kbmclaren@gmail.com
purpose: learn automation
description: extended hello world
"""

print('Hello World!')
myName = input('What is your name: ' )

print('It is good to meet you', myName)
print('The lenth of your name is:', len(myName), 'letters long.')


#Remember that input makes everything a string. No automatic integer assignment.
myAge = input('What is your age: ')
print(f'You will be {int(myAge) + 1} in a year.')

#end firstProg.py
 
