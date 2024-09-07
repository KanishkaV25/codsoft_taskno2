import random

options = ("rock","paper","scissors")
player = None
computer = random.choice(options)

input("1--> ROCK   2--> PAPER    3--> SCISSORS")
player = int(input("Enter your choice: "))


if(player ==1):
    player_choice = "rock"
    print("Player's choice : Rock")
     
elif(player ==2):
    player_choice = "paper"
    print("Player's choice : Paper")

elif(player ==3):
    player_choice = "scissors"
    print("Player's choice: Scissors")
else:
    print("Invalid choice")
    exit()

print(f"Computer's choice: {computer}")

if player_choice == computer:
    print("It's a tie")
elif player_choice =="rock" and computer =="Scissors":
    print("You won !!")
elif player_choice =="paper" and computer == "rock" :
    print("You won !!")
elif player_choice == "scissors" and computer == "paper":
    print("You won !!")

else:
    print("Computer won !!")




