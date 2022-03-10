import pygame
from .base import BaseState #base class template
import yahtzeeGraphics
#import Yahtzee
import scoreCheck
import dice
import os

class Scoring(BaseState):
    def __init__(self):
        super(Scoring, self).__init__()
        self.next_state = "ROLL"
        self.timeActive = 0
    
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse cords ", pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            
            #roll button functionality
            if yahtzeeGraphics.rollButton(0, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]): 

                #roll number increases (if it is not their last roll)
                if (self.persist[2] < 3):
                    self.persist[2] += 1

                    self.next_state = "ROLL" #declare what the next game state is
                    self.done = True #end current state

            #see if dice were clicked
            diceClicked = yahtzeeGraphics.checkIfDiceClicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if (diceClicked):
                if (diceClicked == -1):
                    diceClicked = 0
                dice.clickingDiceToHoldThemFunctionality(self.persist[1], diceClicked)
                #print(self.persist[1])
                #input()

            #if scoreOptionClicked
            #reset
            #add to total score

            #see if any score was clicked
            scoreClicked = yahtzeeGraphics.displayPossibleScores(scoreCheck.getCalculatedScores(scoreCheck.getChoices(self.persist[0]), self.persist[0]), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], True, self.persist[4])
            print(scoreClicked)
            if (scoreClicked != -1):

                #check to see if the score was already picked (yahtzees being the only exception and after the first they give a bonus of 100)
                clickedYahtzee = (scoreClicked[1] == 9)
                if (not scoreCheck.checkIfScoreWasPickedAlready((self.persist[4][scoreClicked[1]]), clickedYahtzee)):
                    #reset the held indeces
                    self.persist[1] = [-1, -1, -1, -1, -1]

                    #don't reset the counter if player clicks a zero score like a little cheapskate (update I found out 0 is a valid and important score in Yahtzee.)
                    #if (scoreClicked[0] == -1):
                        #reset roll counter
                    self.persist[2] = 0

                    #add score to total score
                    self.persist[3] += scoreClicked[0]

                    #mark scoreCard (for checking later if they already have marked that spot) Note: don't mark yahtzees on score card, you can get unlimited yahtzees
                    if not clickedYahtzee:
                        self.persist[4][scoreClicked[1]] = scoreClicked[0]

                    #check if all the scores have been picked (this means the game is over)
                    gameOver = scoreCheck.gameOverCheck(self.persist[4])

                    if (not gameOver):
                        self.next_state = "GAMEPLAY" #declare what the next game state is
                        self.done = True #end current state
                    elif (gameOver):
                        self.next_state = "GAMEOVER" #declare what the next game state is
                        self.done = True #end current state

    def draw(self, surface):
        surface.fill(pygame.Color("white"))
        print(self.persist);
        yahtzeeGraphics.displayRoll(surface, self.persist[0], self.persist[1])
        
        #show the scores that are valid based on current roll
        validScores = scoreCheck.getCalculatedScores(scoreCheck.getChoices(self.persist[0]), self.persist[0])
        #print(validScores)
        #print("self.persist -> ", self.persist)
        #input()

        #get possible scores from roll and display them
        yahtzeeGraphics.displayPossibleScores(validScores, 0, 0, False, self.persist[4])
        #yahtzeeGraphics.displayScoreCard(surface)

        #display the current roll number
        yahtzeeGraphics.displayRollNumber(self.persist[2])

        #display players score
        yahtzeeGraphics.displayPlayersScore(self.persist[3])

        #display roll button (if it's not their last roll)
        if(self.persist[2] < 3):
            yahtzeeGraphics.rollButton(surface, 0, 0)

        