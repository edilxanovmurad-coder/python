import random

chosenNumber = random.randint(1, 100)
attempts = 0
solved = False


def getNumberFromUser():

    while True:
        try:
            return int(input("Please enter your guess : "))
        except ValueError:
            print("please enter a number")


userGuess = getNumberFromUser()
while not solved:
    attempts += 1
    if userGuess > chosenNumber:
        print("Guess a lower number")
        userGuess = getNumberFromUser()

    elif userGuess < chosenNumber:
        print("Guess a higher number")
        userGuess = getNumberFromUser()
    else:
        solved = True
        print(f"Congratulations! Your Attempt : {attempts}")
