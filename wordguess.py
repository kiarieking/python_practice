import random
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
name = input("What is your name:")
print(f"Hello {name}. Welcome to word guesser")
count = 1
from math import ceil, log2
chances = ceil(log2(len(words)))
print(chances)
while count <= chances:
    count +=1
    guess = input("Enter your word guess: ")
    if word != guess:
        print("Incorrect! Try again")
        if count == chances:
            print ("Last chance")
    elif word == guess:
        print(f"Great job {name}!")
        break
