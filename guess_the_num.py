import random


def should_continue():
    playAgain = input("\n\nDo you want to play again 'y/n' :  ")
    if playAgain == 'y' or playAgain == 'n':
        return playAgain
    else:
        return should_continue()


def printing(userNum, computerNum, score):
    print(f"UserNum = {userNum }.\n ComputerNum = {computerNum} .\nYour updated score is {score}. ")


def guessGame():
    playAgain = 'y'
    score = 0

    while playAgain == 'y':

        computerNum = random.randint(1, 100)
        userNum = int(input("\nEnter a number between 1 to 100 - "))

        difference = computerNum - userNum

        if computerNum == userNum:
            print("It's the same number, congratulations you get 50 Points .")
            score = score + 50
            print("Your updated score is ", score)
        elif -5 <= difference <= 5:
            print("This number is very close to real number. ")
            score = score + 25
            printing(userNum, computerNum, score)
        elif - 10 <= difference <= 10:
            print("This number is close to real number. ")
            score = score + 10
            printing(userNum, computerNum, score)
        else:
            print("Sorry! your guess didnt make it. ")
            printing(userNum, computerNum, score)

        playAgain = should_continue()
    else:
        print("Final Score = ", score)


guessGame()
