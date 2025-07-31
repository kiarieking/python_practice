print("Winning rules of the game ROCK PAPER SCISSORS are: \nRock vs Paper -> Paper wins \nRock vs Scissors -> Rock wins \nPaper vs Scissors -> Scissors wins")
import random
choices = ["rock", "paper", "scissors"] 
turns = 6
count = 1
flag = 0
while count <= turns:
    user_choice = input("Enter your choice : ")
    cmp_choices = [choice for choice in choices if choice != user_choice]
    cmp_choice = random.choice(cmp_choices)
    
    if user_choice == "rock" and cmp_choice == "paper":
        print(f"Computer chooses {cmp_choice}")
        print("You lose!!")
    elif user_choice == "rock" and cmp_choice == "scissors":
        print(f"Computer chooses {cmp_choice}")
        print("You win!!")
    elif user_choice == "paper" and cmp_choice == "scissors":
        print(f"Computer chooses {cmp_choice}")
        print("You lose!!")
    elif user_choice == "paper" and cmp_choice == "rock":
        print(f"Computer chooses {cmp_choice}")
        print("You win!!")
    elif user_choice == "scissors" and cmp_choice == "paper":
        print(f"Computer chooses {cmp_choice}")
        print("You win!!")
    elif user_choice == "scissors" and cmp_choice == "rock":
        print(f"Computer chooses {cmp_choice}")
        print("You lose!!")
    count +=1
