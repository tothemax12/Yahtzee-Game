import pygame
from .base import BaseState
from os.path import exists
from Button import Button

def writeHighScores(listOfScores):
        highScoresFile = open("highscores.txt", "w") #don't forget to close!
        highScoresFile.write("\n".join(listOfScores))
        highScoresFile.close()

def sort(intList, stringScores):
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(intList) - 1):
            if intList[i] < intList[i+1]:
                # Swap
                intList[i], intList[i+1] = intList[i+1], intList[i]
                #also swap the strings to the correct spot!
                stringScores[i], stringScores[i+1] = stringScores[i+1], stringScores[i]

                has_swapped = True
    
    #put correct number at the beginning
    for i in range(0, len(stringScores)):
        currentString = list(stringScores[i])
        currentString[0] = str(i+1)

        #don't leave a 0 hanging around if it goes from a ten to a single digit number
        if ((i < 10) and currentString[1].isdigit()):
            currentString.remove("0")

        correctedString = "".join(currentString)
        stringScores[i] = correctedString

    print(stringScores)
    return stringScores

def reverseStringArr(strArr):
    revString = []
    for i in range(len(strArr)-1, -1, -1):
        revString += [strArr[i]]
    return revString

def readInScores():
        scoreStrings = []
        scoreInts = []

        #read in all scores
        highScoresFile = open("highscores.txt", "r") #don't forget to close!
        scoresStrings = highScoresFile.read().splitlines();

        for i in range(0, len(scoresStrings)):
            #go through each string and read backwards until the score is read in 
            currentScore = []
            lenOfCurrentString = len(scoresStrings[i])

            #start at end and go backwards because it's faster
            for j in range(lenOfCurrentString-1 , 1, -1):
                currentChar = scoresStrings[i][j]
                if(currentChar.isdigit()):
                    currentScore += [currentChar]

            #reverse the backwards read in score to make it correct
            currentScore = reverseStringArr(currentScore)

            #after you have the score, turn it to an int
            currentScore = int("".join(currentScore))
            scoreInts += [currentScore]
        
        return [scoresStrings, scoreInts]

def addNewScoreToFile(name, score):
    #put all the current scores into an array of strings
    #get all the scores as ints from array of strings and put the new score in the correct place
    #make a string with the player entered name and new score
    #add the string to the correct spot based on the score
    #if there are more than 10 highscores delete the lowest score in the file (do this before you over write the file so it is not the players newest score who gets deleted if it happens to be the lowest)

    arr = readInScores()
    scoreStrings = arr[0]
    scoreInts = arr[1]
    
    #only keep 10 scores, toss the rest
    if (len(scoreStrings)+1 > 10):
        scoreStrings.pop(len(scoreStrings)-1)
        scoreInts.pop(len(scoreInts)-1)
    
    #add the new scores to the end of arrays
    scoreInts += [score]
    newScoreString = [(str(len(scoreStrings)+1) + ". " + name + " " + str(score))]
    scoreStrings += newScoreString

    #put the new score/scoreString in the correct index
    scoreStrings = sort(scoreInts, scoreStrings)
    
    #over write old highscore list with new one
    writeHighScores(scoreStrings)

class GameOver(BaseState):
    def __init__(self):
        super(GameOver, self).__init__()
        self.lowestScore = ""
        self.persist = []
        self.highScore = False
        self.name = ""
        self.nameEntered = False
        self.mainMButton = Button(162, 263, "MENU", 141, 81, "", 20, "Black", pygame.display.get_surface(), 1)
        self.highScoreAchieved = False

    def resetGame(self):
        self.lowestScore = ""

        #reset player
        self.persist = [[0, 0, 0, 0, 0], [-1, -1, -1, -1, -1], 0, 0, [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
        
        self.highScore = False
        self.name = ""
        self.nameEntered = False
        self.highScoreAchieved = False

    def getName(self, keyPressed):
        #get input and add it to a string, no numbers, if backspace is pressed 
        if (self.highScore):#only if the players score was a new highscore`
            #backspace 8
            #enter 13
            #no numbers allowed 0-9 and the name can't be already finished
            if ((not self.nameEntered) and ((keyPressed >= 97 and keyPressed <= 122) or (keyPressed == 13 or keyPressed == 8))):
                #if they hit enter they are done
                if (keyPressed == 13):
                    self.nameEntered = True
                    return
                #if they hit backspace remove a char
                if (keyPressed == 8):
                    self.name = self.name[:len(self.name)-1]
                    print(self.name)
                    return

                #add valid key to the name
                self.name += pygame.key.name(keyPressed)
                print(self.name)

    def startup(self, persistent):
        pathExists = exists("highscores.txt")
        self.persist = persistent

        #if the highscore file doesn't exist yet, initialize text file
        if (not pathExists):
            highScoreFile = open("highscores.txt", "w")
            highScoreFile.write("1. Jay-Z: 50\n2. Eric Cartman: 27\n3. Max: 20");
            highScoreFile.close()

        #get highest score
        highScoresFile = open("highscores.txt", "r")
        scores = highScoresFile.read().splitlines();

        lengthOfLastScore = len(scores[len(scores)-1])
        for i in range(1, lengthOfLastScore):
            currentChar = scores[len(scores)-1][i]
            if(currentChar.isdigit() and i != 0):
                self.lowestScore += scores[len(scores)-1][i]
        
        #after you have the score, turn it to an int
        self.lowestScore = int(self.lowestScore)
        

    def get_event(self, event):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONUP:
            if self.mainMButton.checkClicked(mouseX, mouseY) and (not self.highScoreAchieved):

                GameOver.resetGame(self)

                self.next_state = self.mainMButton.action
                self.done = True
                

        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            self.getName(event.key)
            
            if event.key == pygame.K_RETURN:
                addNewScoreToFile(self.name, self.persist[3])

                GameOver.resetGame(self)

                self.next_state = "MENU"
                self.done = True
            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        textFont = pygame.font.Font(None, 30)

        #if new highscore was achieved
        if (self.persist[3] > self.lowestScore):
            self.highScoreAchieved = True

            #title screen image (No highscore achieved)
            titleScreen = pygame.image.load('yahtzee-gameover-screen-highscore.png')
            surface.blit(titleScreen, (0, 0))

            self.highScore = True
            highScoreText = textFont.render("New Highscore! Please enter your name!", True, pygame.Color("Blue"))
            surface.blit(highScoreText, (65, 180))
            instructions = textFont.render("(Press Enter to submit)", True, pygame.Color("Blue"))
            surface.blit(instructions, (146, 200))
            
            nameText = textFont.render(self.name, True, pygame.Color("Blue"))
            surface.blit(nameText, (64, 270))

            nameField = textFont.render("___________________________________", True, (0))
            surface.blit(nameField, (64, 270))
        else:
            #title screen image (No highscore achieved)
            titleScreen = pygame.image.load('yahtzee-gameover-screen-no-highscore.png')
            surface.blit(titleScreen, (0, 0))

            self.mainMButton.displayButton()


        
        #display text
        text = textFont.render(("Game over, you scored: " + str(self.persist[3])), True, pygame.Color("White"))
        surface.blit(text, (120, 150))