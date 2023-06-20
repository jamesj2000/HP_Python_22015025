import random

score = 0

tosses = 0

while True:

    command = input("Enter 'toss' to roll the dice or 'quit' to exit: ")

    

    if command == "toss":

        tosses += 1

        

        dice_roll = random.randint(1, 6)

        score += dice_roll

        

        print("You rolled a", dice_roll)

        print("Your total score is", score)

        print("Number of tosses:", tosses)

        

    elif command == "quit":

        print("Exiting the game...")

        break

        

    else:

        print("Invalid input. Try again.")
