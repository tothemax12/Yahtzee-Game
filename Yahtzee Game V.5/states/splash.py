import pygame
from .base import BaseState

class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        self.next_state = "MENU"
        self.time_active = 0
        self.alpha = 255

    def update(self, dt):
        #fade in
        if self.time_active < 4000:
            self.alpha -= 5
            self.time_active += dt
        if self.time_active >= 4000:
            #fade back to black
            self.alpha += 5
            if (self.alpha == 255):
                self.done = True

    def draw(self, surface):
        #title screen image
        logoImage = pygame.image.load('logo-screen.png')
        surface.blit(logoImage, (0, 0))

        fadeSquare = pygame.Surface((500, 500))
        fadeSquare.fill((0,0,0))
        fadeSquare.set_alpha(self.alpha)
        surface.blit(fadeSquare, (0,0))