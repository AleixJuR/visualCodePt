import time
import os
import random
#Aleix Part

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def rockPaperScissors():
    options = ['pedra', 'paper', 'tisora']
    bot = random.choice(options)
    correct = False
    wins = 0
    answer =""
    times = int(input("How many times you want to play --> "))
    
    for i in range(0,times):
        while correct == False:
            user = input("Choose, rock, paper o scissors (en minúscula)")
            if user != "rock" and user != "paper" and user != "scissors":
                print("Invalid option")
            else:
                correct = True
        
        if user == bot:
            print("tie")
        elif (user == "rock" and bot == "scissors") or (user == "scissors" and bot == "paper") or (user == "paper" and bot == "rock" ):
            print("You win!")
            wins +=1
        else:
            print("You lose")
    print(f"You have won {wins} times of a total of {times}")


#Arnau Part

#David Part