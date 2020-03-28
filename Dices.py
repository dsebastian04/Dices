import random

def throwDices(numDices):
    '''return a list of two ints between 1 and 6'''
    return random.choices([1,2,3,4,5,6], k = numDices)

def sumDices(dices):
    '''sum a list of ints'''
    s = 0
    for dice in dices:
        s += dice
    return s

throwDicesFlag = True

while (throwDicesFlag):
    dices = throwDices(2)
    sumDice = sumDices(dices)
    print("Your dice are...\nDice 1: ", dices[0], " \nDice 2: ", dices[1], "\nBoth dice add up to: ", sumDice)
    
    inputInvalid = True
    while (inputInvalid):
        inputUser = input("Do you want to throw the dices again? yes/no\n")
        if (inputUser == "no" or inputUser == "yes" ):
            if (inputUser == "no"):
                throwDicesFlag = False
            inputInvalid = False
        else:
            print("Input invalid. Try again")
            continue
