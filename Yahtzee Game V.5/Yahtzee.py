#Yahtzee Program
#Max Anderson 2021
import random
import scoreCheck
import dice
import player
import yahtzeeGraphics
#from states.base import BaseState

def markPlayersScoreCard(player, validScoreChoices):
    validChoice = False
    while not validChoice: 
        scoreChoice = int(input("what score index?"))
        if (player.scoreCard[scoreChoice] == 0):#make sure it's not already marked
            #they picked a score
            #mark players scorecard with selection
            player.scoreCard[scoreChoice] = validScoreChoices[scoreChoice]
            print("player score card -> ", player.scoreCard)
            validChoice = True
        else:
            print("pick a non marked score!")

def gameLoop():
    #initialize player
    player1 = player.Player()

    #initialize roll
    roll = dice.diceRoll([0, 0, 0, 0, 0], 0)
    
    gameOver = False
    while not gameOver:

        #reset after every round
        rollNum = 0
        held = 0
        roundOver = False

        while not roundOver:
            #player rolls dice
            roll = dice.diceRoll(roll, held)
            
            #testing stuff
            #roll = dice.sortArr(dice.diceRoll([2, 2, 5, 6, 6], [0, 1, 3, 4]))
            #roll = dice.sortArr(dice.diceRoll([5, 5, 5, 5, 5], [0, 2, 4]))

            rollNum += 1
            print("current roll:", roll)

            #show the scores that are valid based on current roll
            validScores = scoreCheck.getChoices(roll)
            print(validScores)

            choice = int(input("hold dice (1) or pick score (2)?"))
            if choice == 1:
               heldIndexs = []
               diceToHold = input("what dice? (what index of dice in the current roll (e.g 014 is the first dice (0) the second dice (1) and the fifth dice (5) in current roll)")

               for i in range(len(diceToHold)):
                   heldIndexs += [int(diceToHold[i])]
               
               held = heldIndexs

               #diceHeld = diceToHold
            if choice == 2:
               #mark the players scorecard
               markPlayersScoreCard(player1, validScores)
               roundOver = True
        

gameLoop()
#if you hold a dice then you are going to roll again
#if you score you are done for that "round"

#1 "round" of yahtzee is at max, a 3 roll sequence where a player holds the dice and rolls again or picks a valid score based on the current faces of the dice

#roll# = 0
#diceHeld = 0
#roundOver = False

#while roundOver is false 
#1.roll
#add 1 to roll #
#show player all valid scores based on roll
#score or hold dice?
#if score, mark score card, reset held and dice roll number to 0, this round is over
#if held chose and dice roll # is <= 3, pick dice being held and roll again
#go back to 1.