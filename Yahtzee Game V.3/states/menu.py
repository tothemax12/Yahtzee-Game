import pygame
from .base import BaseState
from Button import Button

class Menu(BaseState):
    def __init__(self):
        super(Menu, self).__init__()
        self.active_index = 0
        self.next_state = "GAMEPLAY"

        #initialize menu buttons
        self.startButton = Button(157, 144, "GAMEPLAY", 188, 69, "", 50, "Blue", pygame.display.get_surface(), 2)
        self.quitButton = Button(156, 219, "QUIT", 187, 70, "", 50, "Blue", pygame.display.get_surface(), 2)
        self.highScoresButton = Button(158, 371, "HIGHSCORES", 186, 67, "", 50, "Blue", pygame.display.get_surface(), 2)

    def render_text(self, index):
        #if the index is the one you are on, display red otherwise make the font color white
        color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self, state):
        if (state == "QUIT"):
            self.quit = True
        else:
            self.next_state = state
            self.done = True
   
    def get_event(self, event):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

        if event.type == pygame.QUIT:
            self.quit = True

        #checking mouse click
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse cords ", pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

            #handle if a button is clicked
            clickableButtonsOnMenu = [self.startButton.checkClicked(mouseX, mouseY), 
                                      self.quitButton.checkClicked(mouseX, mouseY), 
                                      self.highScoresButton.checkClicked(mouseX, mouseY)]

            for clicked in clickableButtonsOnMenu:
                if clicked:
                    print("BUTTON WAS CLICKED!")
                    self.handle_action(clicked)

        if event.type == pygame.MOUSEMOTION:
            self.startButton.onHover(mouseX, mouseY, (0, 0, 255))

    def draw(self, surface):  
        #title screen image
        titleScreen = pygame.image.load('yahtzee_title.png')
        surface.blit(titleScreen, (0, 0))

        #(self, xCord, yCord, action, width, height, buttonText, textSize, color, surface)         
        self.startButton.displayButton()
        self.quitButton.displayButton()
        self.highScoresButton.displayButton()