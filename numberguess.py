print("Welcome to guessing game!!")
print("Choose the range from which to guess your number")
print("Enter lower bound:")
lowerbound=input()
print("Enter upper bound")
upperbound=input()
count = 0
from math import ceil, log2
rangesize = int(upperbound)-int(lowerbound) +1
totalchances = ceil(log2(rangesize))
import random
correctguess=random.randint(int(lowerbound),int(upperbound))
print(totalchances)
while count < totalchances:
    print("Enter your guess:")
    userguess=input()

    if int(userguess) < correctguess:
        print("Too low: Try again!")
    elif int(userguess) > correctguess:
        print("Too high: Try again!")
    elif int(userguess) == int(correctguess):
        print("Correct, Good job!")
        break 
