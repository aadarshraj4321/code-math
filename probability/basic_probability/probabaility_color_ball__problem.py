
import random
import math



whiteBalls = int(input("Enter how many white balls: "))
redBalls = int(input("Enter how many red balls: "))


whichBallSeclected = ""

userDec = input("Which ball first selected: ")
finalAns = 0

if(userDec == "white"):
    finalAns = redBalls / ((whiteBalls - 1) + redBalls) 
elif(userDec == "red"):
    finalAns = whiteBalls / ((redBalls - 1) + whiteBalls)

print(finalAns)
