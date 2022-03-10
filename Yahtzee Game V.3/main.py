import sys
import pygame
from states.splash import Splash
from states.menu import Menu
from states.gameplay import Gameplay
from states.roll import Roll
from states.scoring import Scoring
from states.gameover import GameOver
from states.highscores import HighScores
 
from game import Game

pygame.init()

screen = pygame.display.set_mode([500, 500])

states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": Gameplay(),
    "ROLL": Roll(),
    "SCORING": Scoring(),
    "GAMEOVER": GameOver(),
    "HIGHSCORES": HighScores()
}

iconImage = pygame.image.load("icon.png")

#init stuff
pygame.display.set_icon(iconImage)
pygame.display.set_caption("Dice Yaht!")
pygame.mixer.music.load('Bike Rides - The Green Orbs.mp3')
pygame.mixer.music.play()

game = Game(screen, states, "SPLASH")
game.run()
pygame.quit()