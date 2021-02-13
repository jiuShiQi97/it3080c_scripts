import random

game = 1
ram = random.randint(0,101)

print("Welcome to gurss the number game!")
while(game == 1): 
    print("inter your number (between 0-100):")
    guessNumber = int(input())
    if guessNumber > ram:
        print("you guess higher than the correct!")
    elif guessNumber < ram:
        print("you guess lower than the correct!")
    elif guessNumber == ram:
        print("you are correct!")
        print("Do you want play again? (y/n):")
        choose = input()
        if choose == 'y':
            game = 1
        if choose == 'n':
            game = 0
            print("Exit success!")
    else:
        print("error:your input is wrong")
