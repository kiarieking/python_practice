print("Welcome to 21 number game!! The goal is to avoid choosing 21 on your turn.")
import random
x =[]
turn_choice = input("Do you want to start first or second? Enter F for FIRST and S for SECOND : ")

if turn_choice == "f" :
    user_choice = input("Enter your number : ")
    if int(user_choice) < 21 and int(user_choice) > 0:
        x.append(user_choice)
    else :
        print("Invalid choice")

elif turn_choice == "s" :
    computer_choice = random.randint(0,22)
    x.append(computer_choice)

print(x)