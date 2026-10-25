import random
chosenNumber = random.randint(1,100)
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
    if userGuess > chosenNumber:
        attempts += 1
        print("Guess a lower number")
        userGuess = getNumberFromUser()

    elif userGuess < chosenNumber:
        attempts += 1
        print("Guess a higher number")
        userGuess = getNumberFromUser()
    else:
        attempts += 1
        solved = True
        print(f"Congratulations! Your Attempt : {attempts}")


