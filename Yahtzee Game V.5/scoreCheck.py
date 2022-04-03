import dice

#functions to check scores in yahtzee
def amountOfSameDice(dice):
    #see what amount of a certain dice they got was
    amounts = [0, 0, 0, 0, 0, 0]
    for i in range(len(dice)):
        amounts[dice[i]-1] += 1
    return amounts

def ofAKindCheck(dice):
    twoOfKind = False
    threeOfKind = False
    fourOfKind = False
    yahtzee = False

    diceCount = amountOfSameDice(dice)
    
    for i in range(len(diceCount)):
        if diceCount[i] == 2:
            twoOfKind = True
        if diceCount[i] == 3:
            threeOfKind = True
        if diceCount[i] == 4:
            threeOfKind = True#if there is 4 of a kind then there is three of a kind
            fourOfKind = True
        if diceCount[i] == 5:#yahtzee is just a 5 of a kind (all dice faces are the same number)
            yahtzee = True
    
    ofAKinds = [twoOfKind, threeOfKind, fourOfKind, yahtzee]
    return ofAKinds

def fullHouseCheck(twoOfKind, threeOfKind):
    #A full house is a two of a kind and a three of a kind
    if twoOfKind and threeOfKind:
        return True
    else:
        return False

def checkIfScoreWasPickedAlready(score, clickedYahtzee):
    #if it's a -1 it is not taken
    if score == -1 or clickedYahtzee:
        return False
    else:
        return True

def gameOverCheck(scoreCard):
    for i in range(0, len(scoreCard)):
        #Since you can score multiple yahtzees, let the user keep clicking it and therefore end the game ever if it's not "checked"
        #like the other scores. This has potential for the player to abuse it as you can just take a zero in the Yahtzee box to
        #essentially reset your roll counter and dice if they are not getting lucky.
        if scoreCard[i] == -1 and (i != 9):
            return False
    #all the score cards are -1 therefore the game has ended
    return True

def yahtzeeCounter(yahtzeeCount):
    if (yahtzeeCount < 1):
        return 50
    else: 
        return 100


def getCalculatedScores(validScores, dice, yahtzeeCount):
    #takes in -> [ones, twos, threes, fours, fives, sixes, threeOfKind, fourOfKind, fullHouse, yahtzee, smallStraight, largeStraight, chance]

    #replace "true"s (valid scores) with actual calculated score
    if (validScores[6]):
        threeOfKindScore = tallyRoll(dice)
        validScores[6] = threeOfKindScore
    if (validScores[7]):
        fourOfKindScore = tallyRoll(dice)
        validScores[7] = fourOfKindScore
    if (validScores[8]):
        fullHouseScore = 25
        validScores[8] = fullHouseScore
    if (validScores[9]):
        #if you score more than one yahtzee you get a 100 point bonus
        yahtzeeScore = yahtzeeCounter(yahtzeeCount)
        validScores[9] = yahtzeeScore
    if (validScores[10]):
        smallStraightScore = 30
        validScores[10] = smallStraightScore
    if (validScores[11]):
        largeStraightScore = 40
        validScores[11] = largeStraightScore
    #pre calculated chance score

    #finally replace the remaining "false"s in the validScores array with 0 for the user to see
    for i in range(len(validScores)):
        if(not validScores[i]):
            validScores[i] = 0

    print(validScores)
    return validScores


def checkPossibleScores(dice):
    ofAKinds = ofAKindCheck(dice)
    twoOfKind = ofAKinds[0]#two of a kind is not on the score sheet but you need it for a full house
    threeOfKind = ofAKinds[1]
    fourOfKind = ofAKinds[2]
    yahtzee = ofAKinds[3] #a yahtzee is just when all the dice are the same number (5 of a kind)
    
    fullHouse = fullHouseCheck(twoOfKind, threeOfKind)

    #these are the scores if you add the faces up (ones is all the ones in the roll added up, twos is all the twos summed and so on)
    totals = checkTotals(dice)
    ones = totals[0]
    twos = totals[1]
    threes = totals[2]
    fours = totals[3]
    fives = totals[4]
    sixes = totals[5]

    straights = checkForStraights(dice)
    smallStraight = straights[0]
    largeStraight = straights[1]

    chance = tallyRoll(dice)


    print("in possible scores function -> ", [twoOfKind, threeOfKind, fourOfKind, fullHouse, yahtzee, smallStraight, largeStraight, chance])

    return [ones, twos, threes, fours, fives, sixes, threeOfKind, fourOfKind, fullHouse, yahtzee, smallStraight, largeStraight, chance]

def checkForStraights(dice):
    streak = 0
    highestStreak = 0

    #index 0 is a small straight index 1 is a large straight
    straights = [False, False]

    for i in range(len(dice)-1):
        if (dice[i] == dice[i+1]-1):
            streak += 1
            if (streak > highestStreak):
                highestStreak = streak
        else:
            streak = 0
        #print("i: ", i, "current streak: ", streak+1, "highest streak: ", highestStreak+1)
            
    if highestStreak > 0:
       highestStreak += 1

    #print(highestStreak)
    if (highestStreak == 4):
        straights[0] = True
    if (highestStreak == 5):
        straights[0] = True
        straights[1] = True

    return straights

#tallyRoll sums all the dice in the roll (useful for when you get a "of a kind" because you count all 5 dice)
def tallyRoll(dice):
    sum = 0
    for i in range(len(dice)):
        sum += dice[i]

    return sum

def checkTotals(dice):
    roll = amountOfSameDice(dice)
    print(roll)
    scoresPerNumber = [0, 0, 0, 0, 0, 0] #this is the tally of each number rolled (4, 6's rolled is 24 points)

    for i in range(len(dice)+1):
        scoresPerNumber[i] = roll[i] * (i+1) #take number of each dice roll and multiply that by the number (E.g 5 fours = 20 points)
    return scoresPerNumber

def getChoices(diceArr):
    #sorting the dice for the user swaps around the dice at the indexs that
    #are intended to be held which screws it up. Considering this, just sort
    #here to utilize the functions based on sorted dice.
    sortedDice = dice.sortArr(diceArr);

    print(checkPossibleScores(sortedDice))
    results = checkPossibleScores(sortedDice) #this function returns an array of valid scoring options (that are true based on the roll)
    resultStrings = []
    
    #show the dice scores
    print("Ones: ", results[0])
    print("Twos: ", results[1])
    print("Threes: ", results[2])
    print("Fours: ", results[3])
    print("Fives: ", results[4])
    print("Sixes: ", results[5])

    if (results[6]):
        print("Three of a kind!")
        #resultStrings += ["Three of a kind"]
    if (results[7]):
        print("Four of a kind!")
        #resultStrings += ["Four of a kind"]
    if (results[8]):
        print("Full House!")
        #resultStrings += ["Full House"]
    if results[9]:
        print("Yahtzee!")
        #resultStrings += ["Yahtzee"]
    if results[10]:
        print("Small Straight!")
    if results[11]:
        print("Large Straight!")
    print("Chance: ", results[12])

    scoresForEachNumber = checkTotals(sortedDice)
    print("scores for each number rolled = ", scoresForEachNumber)
    return results

