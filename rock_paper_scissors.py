import random
print("WELCOME to the Rock Paper & Scissors Game. You will be playing against the computer.")
print("Rules of the game are:")
print("1. You have to input any no between 0-2. 0 stands for Rock, 1 stands for Paper and 2 stands for Scissors.")
print("2. Then the computer will choose a no between 0-2")
print("Rock beats Scissors, Paper beats Rock, Scissor beats Paper")
def game():
 user_choice=int(input("Enter your choice:(enter 0 for Rock, 1 for Paper, 2 for Scissors)"))
 computer_choice=random.randint(0,2)
 print("Computer Choose: ")
 print(computer_choice)
 if user_choice>=3:
    print("Unknown Choice")
 if computer_choice == user_choice:
    print("Its a draw")
 elif computer_choice == 0 and user_choice == 2:
    print("You Lose")
 elif user_choice == 0 and computer_choice == 2:
    print("You win!")
 elif computer_choice>user_choice:
    print("You Lose. Computer Wins!")
 elif user_choice>computer_choice:
    print("Computer lose. You Win!")
 else:
    print("Inconclusive")
game()

print("Do you want to play again?: ")
another_round=input("YES or NO: ")

if another_round=="YES":
    game()
else:
   print("Thank you for playing")
