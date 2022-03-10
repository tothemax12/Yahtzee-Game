import pygame

class Button(object):
    def __init__(self, xCord, yCord, action, width, height, buttonText, textSize, color, surface, borderThickness):
        self.xCord = xCord
        self.yCord = yCord
        self.action = action
        self.width = width
        self.height = height
        self.buttonText = buttonText
        self.textSize = textSize
        self.color = color
        self.surface = surface
        self.borderThickness = borderThickness

    def displayButton(self):
        pygame.draw.rect(self.surface, (0), pygame.Rect(self.xCord, self.yCord, self.width, self.height), self.borderThickness)
        
        #display text
        textFont = pygame.font.Font(None, self.textSize)
        text = textFont.render(self.buttonText, True, pygame.Color(self.color))
        self.surface.blit(text, (self.xCord, self.yCord))

    def onHover(self, mouseX, mouseY, color):
        #see if we're on the button
        if self.checkClicked(mouseX, mouseY):
            print("HOVERING ON BUTTON")
            #color is an rgb value, like this (0, 0, 0)
            pygame.draw.rect(self.surface, color, pygame.Rect(self.xCord, self.yCord, self.width, self.height))

    def checkClicked(self, mouseX, mouseY):
        if mouseX >= self.xCord and mouseX <= (self.xCord + self.width) and mouseY >= self.yCord and mouseY <= (self.yCord + self.height):
            return self.action
        return False
    