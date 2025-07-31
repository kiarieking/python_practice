print("Welcome to 21 number game!! The goal is to avoid choosing 21 on your turn.")
import random
x =[]
turn_choice = input("Do you want to start first or second? Enter F for FIRST and S for SECOND : ")

def user_input():
    default_selections = 1
    selections = input("How many numbers do you want to input: ")
    last_entry = 0
    if len(x) != 0: 
        last_entry = x[len(x)-1]
    while default_selections <= int(selections):
        user_choice = input("Enter your number : ")
        if int(user_choice) < 21 and int(user_choice) > 0 and int(user_choice) > int(last_entry):
            x.append(user_choice)
        else :
            print("Invalid choice")
        default_selections +=1
    print(x)
    winning_value = x[len(x)-1]
    if winning_value == 21:
        print("Sorry!! You lost!!")
        return
    computer_input()

def computer_input():
    default_selections = 1
    selections = random.randint(1,6)
    last_entry = 0
   
    last_entry = x[len(x)-1]
    while default_selections <= selections :
        computer_choice = random.randint(int(last_entry)+1,21)
        x.append(computer_choice)
        default_selections +=1
    print(x)
    winning_value = x[len(x)-1]
    if winning_value == 21:
        print("Congratulations!! You win!!")
        return
    user_input()

y = 21
while y not in x:
    if turn_choice == "f":
        user_input()
    elif turn_choice == "s":
        computer_input()