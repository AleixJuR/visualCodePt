import random
import time
import os
#Aleix Part
def menu():
    correct = False
    while(not correct):
        try:
            print("Choose a option")
            print("1 - Rock Paper Scissors")
            print("2 - Hanged")
            print("3 - Parameters")
            print("4 - Find The Spot")
            print("0 - Exit")
    
            option = int(input())
            if option == 1 or option == 2 or option== 3 or option ==4 or option ==0: #If you select a answer that's not on the menu it raise exception
                correct = True
            else:
                raise Exception
        except:
            print("Error")
    return option
    
def regressive(): #Do a regressive count of 3 seconds clearing console every second
    clear_console()
    print("3")
    time.sleep(1)
    clear_console()
    print("2")
    time.sleep(1)
    clear_console()
    print("1")
    time.sleep(1)
    clear_console()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear') #If the OS is Windows it executes cls on the cmd, if is Linux it executes clear on terminal
def rockPaperScissors():
    options = ["rock", "paper", "scissors"]
    bot = random.choice(options)
    correct = False
    wins = 0
    answer =""
    times = int(input("How many times you want to play --> "))
    
    for i in range(0,times):
        bot = random.choice(options) #it generate a random option of rock paper scissors
        while correct == False:
            user = input("Choose, rock, paper o scissors (en minúscula) --> ")
            if user != "rock" and user != "paper" and user != "scissors": 
                print("Invalid option")
            else:
                correct = True
        regressive()
        if user == bot: # If your answers is the same of the bot is tie
            print("tie")
        elif (user == "rock" and bot == "scissors") or (user == "scissors" and bot == "paper") or (user == "paper" and bot == "rock" ):
            print("You win!") #If the option is any of these, you win
            wins +=1
        else:
            print("You lose")
        correct = False
    print(f"You have won {wins} times of a total of {times}") #It print the total of wins of the game
    input("Press any Key to Continue")
    clear_console()

def Hanged():
    words = ['python', 'github', 'git', 'enviorments', 'development', 'dam', 'montilivi'] #The words that are in the game
    randomWord = random.choice(words)
    answers = ['_'] * len(randomWord) #It prints _ hiding the answer
    tries = 7
    saidLetters=""
    win = False
    while tries >0 and  win == False:
        letter = input("Say a letter --> ")
        if letter in randomWord:
            for i in range(len(randomWord)):
                if randomWord[i] == letter:
                    answers[i] = letter #If is correct it substitute _ for the letter
        else:
            tries -=1
            print(f"INCORRECT ANSWERS - {tries} TRIES REMAINING")
        saidLetters+=letter
        print(f"Said Letters -> {saidLetters}")
        
        print(' '.join(answers))

        if '_' not in answers:
            print("You Win!") #If it doesn't find _ in the answer, it's correct
            win = True
    else:
            if win == False:
                print(f"You Lose. The word was {randomWord}")

#Arnau Part
def Parameters():
    print("-------------------------------------------------------<()>-------------------------------------------------------")
    print("Basiclly in this game the computer will choose 2 random numbers between 1 and 20, this 2 random numbers are the parameters in which luckily your number will be in, if it's not then you lose. Good luck.")
    print("-------------------------------------------------------<()>-------------------------------------------------------")
    correct = False
    while not correct:
        num = int(input("Choose a number between 1 and 20 --> "))
        bot1 = random.randint(1,20) #bot1 will choose a random number between 1 and 20
        bot2 = random.randint(1,20) #bot2 will make the same as bot1
        if bot1 > bot2:
            bot1, bot2 = bot2, bot1
            if num < 1 or num > 20:
                print("The number is not between 1 and 20!!")
        if num < bot1 or num > bot2:
            print(f"The {num} was not within the parameters, you lost!! :C")
        else:
            print(f"The {num} was within the parameters, you won!! :D")
            correct = True
        print(f"The parameters are {bot1, bot2}")#here it will be shown the parameters wich were randomly choosed.
        

def FindTheSpot():
    print("-------------------------------------------------------<()>-------------------------------------------------------")
    print("Basically in this game the computer will choose up to 15 random numbers between 1 and 20. You must avoid writing the same number. Good luck.")
    print("-------------------------------------------------------<()>-------------------------------------------------------")
    correct = False
    while not correct:
        num = int(input("Choose a number between 1 and 20 --> "))
        bot = []
        for i in range(0,15):
            bot.append(random.randint(1,20)) # bot will choose a random number between 1 and 20, 15 times and will add them to the list.
        if num in bot:
            print(f"The {num} is within the random numbers chosen, you lost!! :C")#if you write the same number computer will print the following text.
        else:
            print(f"The {num} is not within the random numbers chosen, you won!! :D")
            correct = True

        print(f"The random numbers are {bot}")

#Main
option = menu()
while (option != 0):
    if option ==1:
        rockPaperScissors()
    if option == 2:
        Hanged()
    if option ==3:
        Parameters()
    if option ==4:
        FindTheSpot()
    option = menu()
