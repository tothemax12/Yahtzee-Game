import pygame
from .base import BaseState #base class template
import yahtzeeGraphics
#import Yahtzee
import dice

class Roll(BaseState):
    def __init__(self):
        super(Roll, self).__init__()
        self.next_state = "SCORING"
        self.timeActive = 0
        self.getRoll = False

    def update(self, dt):
        self.timeActive += dt
        if self.timeActive >= 1000:
            #new roll
            self.getRoll = True

    def draw(self, surface):
        #display animation
        yahtzeeGraphics.rollAnimation(surface)

        #get new roll
        if self.getRoll:
            #reset
            self.timeActive = 0
            self.getRoll = False

            #get a new roll after animation
            #roll = dice.sortArr(dice.diceRoll(self.persist[0], self.persist[1]))
            
            roll = dice.diceRoll(self.persist[0], self.persist[1])
            #auto yahtzee for dev purposes
            #roll = [1, 1, 1, 1, 1]


            #keep the roll after animation state ends
            self.persist[0] = roll

            #finished
            self.done = True
