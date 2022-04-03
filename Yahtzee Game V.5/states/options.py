import pygame
from .base import BaseState #base class template
from Button import Button

def getCurrentVol(x, dist):
    maxVol = 100
    return (((maxVol/dist)*x)*(10**-2))#formula for current volume level

class Options(BaseState):
    def __init__(self):
        super(Options, self).__init__()
        #top left 110 451 b.r 181 494
        self.backButton = Button(110, 451, "Back", 71, 43, "", 20, "Red", pygame.display.get_surface(), 1)
        self.next_state = "MENU"
        self.xCord = 240

    def get_event(self, event):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONUP:
            #print(mouseX, mouseY)
            if self.backButton.checkClicked(mouseX, mouseY):
                self.done = True
        print(mouseX, mouseY)
        if (pygame.mouse.get_pressed(num_buttons=3)[0]):
            self.xCord = mouseX
            #print("current pos on slider ", (self.xCord-138) )
            #print("current volume! : ", getCurrentVol((self.xCord-138), 208))
            pygame.mixer.music.set_volume(getCurrentVol((self.xCord-138), 208))
            
    def startup(self, persistent):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        #highscore menu screen image
        titleScreen = pygame.image.load('options-menu.png')
        surface.blit(titleScreen, (0, 0))
        self.backButton.displayButton();

        #volume slider
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(self.xCord, 214, 10, 40))
        
        #line start and end x val 138-346

        #138 - 0
        #346 - 208
