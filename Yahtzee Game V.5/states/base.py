import pygame

class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        #persist contains dice roll, index of held dice, the current roll number, the players score, and the players scorecard (I should probably convert this to a dictionary at some point...)
        #self.persist = [[0,0,0,0,0]]
        #the score card should be init to -1 because 0 is a valid score choice in Yahtzee [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        #dev scores [2, 2, 2, 2, 2, 2, 2, 2, 2, -1, 2, 2, 2]
        self.persist = [[0, 0, 0, 0, 0], [-1, -1, -1, -1, -1], 0, 0, [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
        self.font = pygame.font.Font(None, 24)

    def getScoreCard(self):
        return self.persist[4]

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass