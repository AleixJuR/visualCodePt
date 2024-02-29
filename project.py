import random
#Aleix Part

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

Parameters()
FindTheSpot()
