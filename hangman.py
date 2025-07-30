fruits = ["mango", "blueberry", "papaya", "pomegranate","dragon fruit","kiwi","lychee","plum","guava","apricot","passion fruit","starfruit" ]
import random
from collections import Counter
fruit=random.choice(fruits)
print(fruit)


dash="_"
entry = dash*len(fruit)

count = 0
chances = len(fruit)+3
print(f"you have {chances} chances")
greeting = "Welcome to hangman game!!"

print (greeting)



while count < chances :
    char_guess = input("Enter your first guess!: ")
    if char_guess in fruit:
        i = fruit.index(char_guess)
        # print(i)
        entry = ''.join([char_guess if fruit[i] == char_guess else entry[i] for i in range(len(fruit))])

        if entry == fruit:
            print(f"Congrats!! The fruit is {entry}.")
            break
        print(entry)
        
    elif char_guess not in fruit:
        print("That character does not exist")
        print (entry)

    count +=1
    print(f"count is {count}")




# name = "kiarie"
# name2 = name.replace("k","_")
# count=0
# while count < len(name):
#     name2 = name.replace(name[count],"_")
#     count +=1
#     print(name2)
