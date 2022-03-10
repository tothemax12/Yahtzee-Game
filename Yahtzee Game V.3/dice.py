#Dice functions for Yahtzee game
import random
import yahtzeeGraphics

#this function is to handle when the user actually clicks on dice to hold them
def clickingDiceToHoldThemFunctionality(heldArray, diceClickedIndex):
    flag = False

    for i in range(len(heldArray)):
        if heldArray[i] == diceClickedIndex:
            flag = True
            
            #if they click the same dice again remove it from the array
            #this way by clicking it they can toggle if they want to hold a certain dice
            heldArray[i] = -1

            #print("Dice already being held!")
            #input()
    if not flag:
        heldArray[diceClickedIndex] = diceClickedIndex
    #print(heldArray)
    #input()

def holdDice(dice, keepIndexs):
     #reroll the ones they are not keeping
        for i in range(5):

            dontRoll = False
            for j in range(len(keepIndexs)):
                if keepIndexs[j] == i:#if current dice being rolled (i) is equal to a dice being held, don't roll it
                    dontRoll = True

            if dontRoll:
                continue

            dice[i] = random.randrange(1, 7)

        return dice #return modified previous roll containing held dice

#previous roll is an array of the dice last rolled
#keepIndexs are the indexs of the dice in the previous roll that the player wants to keep (not change)
#rollCount
def diceRoll(previousRoll, keepIndexs):
    #if they are rolling all the dice (keeping 0)
    if keepIndexs == [-1, -1, -1, -1, -1]:
        dice = []
        for i in range(5):
            dice += [random.randrange(1, 7)]
        print("Your roll was ", dice)
        return dice
    else:
       rerollNonHeld = holdDice(previousRoll, keepIndexs)
       return rerollNonHeld

def diceHold(diceArr):
    print("What dice would you like to hold? (type dice numbers or N for none)")
    diceHeld = []
    choice = 0
    while (choice != "N" or choice != "n"):
     choice = input()
     if (choice == "N"):
        break
     else:
        diceHeld += [int(choice)]

    print(diceHeld)
    return diceHeld

def sortArr(arr):

    #don't modify the original
    arrCopy = arr[:]

    #sort arr from smallest to largest (bubble sort)
    for i in range(len(arrCopy)-1):
        for j in range(len(arrCopy)-i-1):
            #perform swap
            if (arrCopy[j] > arrCopy[j+1]):
                temp = arrCopy[j]
                arrCopy[j] = arrCopy[j+1]
                arrCopy[j+1] = temp
    return arrCopy