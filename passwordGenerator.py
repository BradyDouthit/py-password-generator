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
            # randomly add numbers to password
            password += str(randrange(10))
        else:
            # generate random number based on ASCII table values
            # convert to character and append to password
            password += str(chr(randrange(33, 127)))

    cprint(password, 'green')

generatePassword()
