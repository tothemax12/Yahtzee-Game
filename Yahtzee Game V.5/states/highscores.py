import pygame
from .base import BaseState #base class template
from os.path import exists
from Button import Button

class HighScores(BaseState):
    def __init__(self):
        super(HighScores, self).__init__()
        self.done = False
        self.quit = False
        self.next_state = "MENU"
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.font = pygame.font.Font(None, 24)
        self.highScoreList = ""
        self.backButton = Button(14, 31, "Back", 71, 54, "", 20, "Red", pygame.display.get_surface(), 1)

    def get_event(self, event):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

        if (event.type == pygame.MOUSEBUTTONUP):
            print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if (self.backButton.checkClicked(mouseX, mouseY)):
                self.done = True

    def startup(self, persistent):
        #note to self actually do this check when you are at the main menu because then you might be able to entirely skip this state
        #check to see if default highscore file was created
        pathExists = exists("highscores.txt")
        if (pathExists):
            #self.highScoreList = extractScores()
            highScoreFile = open("highscores.txt", "r")
            highScoreList = highScoreFile.read().splitlines()
            self.highScoreList = highScoreList
            
            highScoreFile.close()
            #print(self.highScoreList)
            #input()
        else:
            #intialize highscore list
            highScoreFile = open("highscores.txt", "w")
            highScoreFile.write("1. Jay-Z: 50\n2. Eric Cartman: 27\n3. Max: 20");
            highScoreFile.close()

    def update(self, dt):
        pass

    def draw(self, surface):
        #highscore menu screen image
        titleScreen = pygame.image.load('highscores.png')
        surface.blit(titleScreen, (0, 0))
        
        #print(self.highScoreList)
        #input()

        #display text
        textFont = pygame.font.Font(None, 40)

        y = 140
        for highScore in self.highScoreList:
            text = textFont.render(highScore, True, pygame.Color("White"))
            surface.blit(text, (130, y))
            y += 35

        self.backButton.displayButton()