import random
exit = False
user_point =  0
computer_point = 0
while exit == False:
    options = ['rock', 'paper', 'scissors']
    user_input = input('Choose rock, Paper, scissors or exit: ')
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        print("you won a total score of " + str(user_point )+  " and the computer total score is "+ str(computer_point))
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a Tie!")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer inpput is paper")
            print("computer Wins")
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You Win!")
            user_point =user_point+1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You  win!")
            user_point = user_point+1
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer inpput is paper")
            print("It's a Tie!")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("computer Win!")
            computer_point = computer_point +1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is Scissors")
            print("Computer input is rock")
            print("Computer win!")
            computer_point = computer_point + 1

        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer inpput is paper")
            print("You Wins")
            user_point = user_point+1
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("Its's a Tie!")
        elif user_input != "rock" or user_input != "paper" or user_input !="scissors":
            print("Invalid input")
