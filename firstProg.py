#file: firstProg.py
#author: Caleb M. McLaren
#email: kbmclaren@gmail.com
#purpose: learn automation
#description: extended hellow world.

print('Hello World!')
print('What is your name?')
myName = input()

print('It is good to meet you', myName)
print('The lenth of your name is:', len(myName), 'letters long.')

print('What is your age?')
#Remember that input makes everything a string. No automatic integer assignment.
myAge = input()
print(f'You will be {int(myAge) + 1} in a year.')

#end file
 
