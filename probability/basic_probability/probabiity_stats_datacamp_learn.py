import math
import random


# Sample space
cards = 52

# Outcomes
aces = 4

# Divide possible outcomes by the sample set
ace_probability = aces / cards

# Print probability rounded to two decimal places
#print(ace_probability)
print(round(ace_probability, 2))


# Ace probability precent code
ace_probability_percent = ace_probability * 100

# Print probability percent rounded to one decimal place
print(str(round(ace_probability_percent, 0)) + "%")


## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------

print("-------------------------------------------------------")
print("-------------------------------------------------------")

# Create function that returns probability percent rounded to one decimal place
def eventProbability(eventOutcomes, sampleSpace):
    probability = (eventOutcomes / sampleSpace) * 100
    return round(probability, 1)


# Sample space
cards = 52

# Determine the probability of drawing a heart
hearts = 13
heartProbability = eventProbability(hearts, cards)

# Determine the probability of drawing a face card
faceCards = 12
faceCardsProbability = eventProbability(faceCards, cards)


# Determine the probability of drawing the queen of hearts
queenOfHearts = 1
queenOfHeartsProbability = eventProbability(queenOfHearts, cards)

# Print each probability
print("Heart Card Probability: " + str(heartProbability) + "%")
print("Face Card Probability: " + str(faceCardsProbability) + "%")
print("Queen Of Hearts Probability: " + str(queenOfHeartsProbability) + "%")








## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------

print("-------------------------------------------------------")
print("-------------------------------------------------------")

# Permutations Code

n = 4
k = 2

# Determine permutations and print result
permutations = math.factorial(n) / math.factorial(k)
print(permutations)

n = 52
k = 2
permutations = math.factorial(n) / math.factorial(n - k)
combinations = permutations / math.factorial(k)
print(combinations)





## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------



print("-------------------------------------------------------")
print("-------------------------------------------------------")




# Sample space
cards = 52
cardsDrawn = 1
cards -= cardsDrawn

# Determine the probability of drawing an Ace after drawing a King on the first draw
aces = 4
aceProbability1 = eventProbability(aces, cards)

# Determine the probability of drawing an Ace after drawing an Ace on the first draw
acesDrawn = 1
aces -= acesDrawn
aceProbability2 = eventProbability(aces, cards)

# Print each probability
print("Ace Probability 1: ", aceProbability1)
print("Ace Probability 2: ", aceProbability2)





## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------



print("-------------------------------------------------------")
print("-------------------------------------------------------")




# Sample space
cards = 52

# Calculate the probability of drawing a heart or a club
hearts = 13
clubs = 13
heartOrClub = eventProbability(hearts, cards) + eventProbability(clubs, cards)

# Calculate the probability of drawing an ace, king or a queen
aces = 4
kings = 4
queens = 4
aceKingOrQueen = eventProbability(aces, cards) + eventProbability(kings, cards) + eventProbability(queens, cards)

print("Heart Or Club : ", heartOrClub)
print("Ace King Or Queen: ", aceKingOrQueen)




## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------



print("-------------------------------------------------------")
print("-------------------------------------------------------")


# Sample Space
cards = 52

# Calculate the probability of drawing a heart or an ace
hearts = 13
aces = 4
aceOfHeart = 1
heartOrAce = eventProbability(hearts, cards) + eventProbability(aces, cards) - eventProbability(aceOfHeart, cards)


# Calculate the probability of drawing a red card or a face card
redCards = 26
faceCards = 12
redFaceCards = 6
redOrFaceCards = eventProbability(redCards, cards) + eventProbability(faceCards, cards) - eventProbability(redFaceCards, cards)

print("Heart Or Ace: ", round(heartOrAce, 1))
print("Red Or Face Cards: ", round(redOrFaceCards, 1))



## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------
## ------------------------------------------------------------------------------



print("-------------------------------------------------------")
print("-------------------------------------------------------")



