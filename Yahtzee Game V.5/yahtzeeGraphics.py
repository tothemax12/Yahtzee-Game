#Yahtzee Graphics
# Simple pygame program
import random
import pygame

clicked = False

def displayText(x, y, string):
        #display text
        surface = pygame.display.get_surface()
        textFont = pygame.font.Font(None, 50)
        text = textFont.render(string, True, pygame.Color("black"))
        surface.blit(text, (x, y))

def checkIfDiceClicked(mouseX, mouseY):
    y = 50 #constant height of dice
    sideLen = 60 #dice are square
    
    #see what dice was clicked
    if mouseX >= 10 and mouseX <= 10+sideLen and mouseY >= y and mouseY <= y + sideLen:
        #print("Clicked 1")
        #input()
        #(index) 0 returns false so this is my work around
        return -1
    if mouseX >= 80 and mouseX <= 80+sideLen and mouseY >= y and mouseY <= y + sideLen:
        #print("Clicked 2")
        #input()
        return 1
    if mouseX >= 150 and mouseX <= 150+sideLen and mouseY >= y and mouseY <= y + sideLen:
        #print("Clicked 3") 
        #input()
        return 2
    if mouseX >= 220 and mouseX <= 220+sideLen and mouseY >= y and mouseY <= y + sideLen:
        #print("Clicked 4")
        #input()
        return 3
    if mouseX >= 290 and mouseX <= 290+sideLen and mouseY >= y and mouseY <= y + sideLen:
        #print("Clicked 5")
        #input()
        return 4
    return False

def rollButton(screen, mouseX, mouseY):
    x = 100
    y = 300
    width = 80
    height = 60
    
    if screen != 0: #if it's 0 just check if they clicked on the button
        #display button
        pygame.draw.rect(screen, (0), pygame.Rect(x, y, width, height), 2)

        #display text
        displayText(x, y, "Roll")

    if mouseX >= x and mouseX <= x+width and mouseY >= y and mouseY <= y + height:
        print("Clicked")
        return True
    else:
        return False



def displayRoll(screen, roll, heldArray):
    x = 10
    y = 50
    for i in range(5):
        face = roll[i]
        if (heldArray[i] == -1):
            drawDice(screen, x, y, face, False)
        else:
            drawDice(screen, x, y, face, True)

        x += 70
    

def drawDice(screen, x, y, face, held):
    
    if held:    
        #red dice (to mark the dice being held)
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 60, 60))
    
    else:
        #white dice (to mark the dice normal dice)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 60, 60))

        #black dice
        pygame.draw.rect(screen, (0), pygame.Rect(x, y, 60, 60), 2)
   
    #possible sides of dice
    #displaying the dice depends on the roll
    if face == 1:
        pygame.draw.circle(screen, (0), (x+30, y+30), 10)
    if face == 2:
        pygame.draw.circle(screen, (0), (x+15, y+15), 10)
        pygame.draw.circle(screen, (0), (x+40, y+40), 10)
    if face == 3:
        pygame.draw.circle(screen, (0), (x+15, y+15), 10)
        pygame.draw.circle(screen, (0), (x+30, y+30), 10)
        pygame.draw.circle(screen, (0), (x+45, y+45), 10)
    if face == 4:
        pygame.draw.circle(screen, (0), (x+15, y+15), 10)
        pygame.draw.circle(screen, (0), (x+15, y+45), 10)
        pygame.draw.circle(screen, (0), (x+45, y+15), 10)
        pygame.draw.circle(screen, (0), (x+45, y+45), 10)
    if face == 5:
        pygame.draw.circle(screen, (0), (x+15, y+15), 10)
        pygame.draw.circle(screen, (0), (x+15, y+45), 10)
        pygame.draw.circle(screen, (0), (x+30, y+30), 10)
        pygame.draw.circle(screen, (0), (x+45, y+15), 10)
        pygame.draw.circle(screen, (0), (x+45, y+45), 10)    
    if face == 6:
        pygame.draw.circle(screen, (0), (x+15, y+15), 8)
        pygame.draw.circle(screen, (0), (x+15, y+45), 8)
        pygame.draw.circle(screen, (0), (x+15, y+30), 8)
        pygame.draw.circle(screen, (0), (x+45, y+30), 8)
        pygame.draw.circle(screen, (0), (x+45, y+15), 8)
        pygame.draw.circle(screen, (0), (x+45, y+45), 8)
    
def rollAnimation(drawingSurface):
    #clear screen after displaying each roll
    #drawingSurface.fill(pygame.Color("white"))
    #display background
    backGroundImage = pygame.image.load('green-velvet-background.png')
    drawingSurface.blit(backGroundImage, (0, 0))

    #displays a random roll
    x = 10
    y = 50
    for i in range(5):
        face = random.randrange(1, 6)
        drawDice(drawingSurface, x, y, face, False)
        x += 70

def displayScoreCard(surface):
    scoreCard = pygame.image.load("yahtzee-scorecard.jpg")
    scoreCard = pygame.transform.scale(scoreCard, (350, 400))
    surface.blit(scoreCard, (315, 120))

def displayPlayersScore(score):
    surface = pygame.display.get_surface()
    score_font = pygame.font.Font(None, 35)
    x = 320
    y = 10
    
    numberFont = score_font.render(("Score: " + str(score)), True, pygame.Color("black"))

    surface.blit(numberFont, (x, y))


def displayRollNumber(rollNumber):
    surface = pygame.display.get_surface()
    title_font = pygame.font.Font(None, 35)
    x = 10
    y = 10
    
    numberFont = title_font.render(("Roll (" + str(rollNumber) + "/3)"), True, pygame.Color("black"))

    surface.blit(numberFont, (x, y))

def displayPossibleScores(scoreStringArr, mouseX, mouseY, clickCheck, scoreBoard):
    surface = pygame.display.get_surface()

    #display a white rectangle behind the scores so you can read them
    buttonY = 115
    for i in range(13):
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(320, buttonY, 170, 25), 0)
        buttonY += 30


    #if your just displaying the button clickCheck is False
    if (clickCheck != True):
        title_font = pygame.font.Font(None, 25)
        scoringNames = ["Ones: ", "Twos: ", "Threes: ", "Fours: ", "Fives: ", "Sixes: ", "Three of a kind: ", "Four of a kind: ", "Full House: ", "Yahtzee: ", "Small Straight: ", "Large Straight: ", "Chance: "]

        print(scoreStringArr)

        x = 320
        y = 115
        for i in range(len(scoreStringArr)):
            title = title_font.render((scoringNames[i] + str(scoreStringArr[i])), True, pygame.Color("black"))
            surface.blit(title, (x, y))
            y += 30
    
    ###BUTTON FUNCTIONALITY###
    #display buttons on possible scores
    buttonX = 320
    buttonY = 115
    buttonWidth = 170
    buttonHeight = 25

    #display buttons
    for i in range(13):
        #if the score was clicked make the box red
        if scoreBoard[i] != -1:
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(buttonX, buttonY, buttonWidth, buttonHeight), 0)
            

        pygame.draw.rect(surface, (0), pygame.Rect(buttonX, buttonY, buttonWidth, buttonHeight), 2)
        buttonY += 30

    #if input is from event check see if a button was clicked (clickCheck was True)
    if (mouseX != 0 and mouseY != 0):
        #if a button was not clicked
        buttonClicked = -1

        #check if click was between a constant x value and constant width
        clickInWidth = False
        if (mouseX >= buttonX and mouseX <= buttonX + buttonWidth):
            clickInWidth = True
            
        #check each button to see if mouseY was in height
        currentButtonsY = 115
        for i in range(13):
            #print(currentButtonsY, mouseY)
            #input()
            if ((mouseY >= currentButtonsY and mouseY <= currentButtonsY+buttonHeight) and clickInWidth):
                buttonClicked = i%30

                #displayText(50, 50, "button: " + str(i%30) + " clicked!")
                #print("CLICK WAS ON A SCORE!")
                #print("button: " + str(i%30) + " clicked!")
                #input()
            #check next button
            currentButtonsY += 30

        if buttonClicked != -1:
            #return the actual score for their selection and the button clicked (this is essentially the index on scorecard)
            return [scoreStringArr[buttonClicked], buttonClicked]
        else:
            #show that a score was not chosen
            return buttonClicked