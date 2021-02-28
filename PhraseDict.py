#### This script makes a GUI that outputs happy phrases for Jane

## To make exacutabe:
## https://datatofish.com/executable-pyinstaller/

#--------------------------------------------------------------------------#

## Generates Phrases

import os
os.system('clear')

import random as rand

Dictionary = {

    "1":"I love you! Hope you have a great day!",
    "2":"You are my best friend!",
    "3":"Have a great day today!",
    "4":"Give Charwie and Donni a big kiss from me!",
    "5":"Enjoy your day!"

}

lower_range = 1
upper_range = len(Dictionary)

index = str(rand.randint(lower_range,upper_range))

PHRASE = Dictionary[index]

print(PHRASE)

#--------------------------------------------------------------------------#