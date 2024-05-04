import random



one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for i in range(10000000):
    dice = random.randint(1, 6)
    if(dice == 1):
        one += 1
    elif(dice == 2):
        two += 1
    elif(dice == 3):
        three += 1
    elif(dice == 4):
        four += 1
    elif(dice == 5):
        five += 1
    elif(dice == 6):
        six += 1


print("No of one : " + str(one))
print("No of two : " + str(two))
print("No of three: " + str(three))
print("No of four: " + str(four))
print("No of five: " + str(five))
print("No of six: " + str(six))
