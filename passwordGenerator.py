import numpy as np
from random import randrange
from termcolor import colored, cprint

print("Enter number of characters...")
numChars = int(input())
print()

def generatePassword():
    password = ""
    cprint("Generating Password", 'cyan')
    for i in range(numChars):
        chanceForNum = randrange(5)
        if chanceForNum == 1:
            password += str(randrange(10))
        else:
            password += str(chr(randrange(33, 127)))

    cprint(password, 'green')

generatePassword()
