import pygame
from .base import BaseState
#import Yahtzee
import yahtzeeGraphics

class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.persist = []

    def startup(self, persistent):
        self.persist = persistent
        
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse cords ", pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if yahtzeeGraphics.rollButton(0, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                
                #roll number increases
                self.persist[2] += 1

                #pygame.mixer.music.load('(Free) Dice Roll Sound Effect 1.mp3')
                #pygame.mixer.music.play(0)

                self.next_state = "ROLL" #declare what the next game state is
                self.done = True #end current state
            

    def update(self, dt):
        self.done = False

    def draw(self, surface):
        #Yahtzee.turn()
        #make the screen white
        #surface.fill(pygame.Color("white"))

        #display background
        backGroundImage = pygame.image.load('green-velvet-background.png')
        surface.blit(backGroundImage, (0, 0))

        yahtzeeGraphics.displayRoll(surface, [6, 2, 3, 4, 5], self.persist[1])
        print("in draw")

        #display roll button
        pygame.draw.rect(surface, "White", pygame.Rect(100, 300, 80, 60))
        yahtzeeGraphics.rollButton(surface, 0, 0)