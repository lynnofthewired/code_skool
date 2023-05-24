# Lynn Makowski
# Fifth Guess
# This program is a number guessing game where the player has five tries to guess a random number between 1 and 100.
# The program prompts the player for their guess and provides feedback if the guess is too high or too low. At the
# end of the game, the program calculates and displays the player's score based on how close their guesses are.

# importing math for determining score, and random for the random number
import math
import random

# Dividend used later to determine the score if the answer is never guessed, using a prime number,
# which is intentionally bizarre, for the purpose of obfuscating the point system from the user
# the way most older video games tend to.
LOSE_DIVIDEND = 1399

# Constant to store full points
WIN_SCORE = 2000000

def main():
    # Initialization for the randomly generated answer and the turn counter
    answer = random.randint(1, 100)
    turns = 0
    scores = []  # List to store all the scores

    print(f"Welcome to Fifth Guess\nthe number guessing game that you can play for eternity! \nI am thinking of a number between 1 and 100. \nSee if you can guess what it is in 5 tries!")

    # While logic handles the first four turns the same way
    while turns < 4:
        # Prompt the user for their guess
        guess = int(input("Enter your guess: "))

        # Check if the guess is too high, too low, or correct
        if guess > answer:
            print("That's too high!")
        elif guess < answer:
            print("That's too low!")
        else:
            divisor = abs(answer - guess)  # Calculate the score based on the distance
            quotient = WIN_DIVIDEND
            exponent = 2  # Adjust the exponent as needed for the desired rate of increase
            score = WIN_SCORE
            print(f"🐬✨Congrats, you did it!✨🌊 \nThank you for playing \nYour score is: {score}")
            scores.append(int(score))  # Add the score to the list
            break

        # Increment the turn counter
        turns += 1

    # If logic will run when the turn counter exceeds 4 and handles the fifth and final turn
    if turns == 4:
        if answer % 2 == 0:
            print(f"I'll give you one more hint; the number is even.")
        else:
            print(f"I'll give you one more hint; the number is odd.")
        guess = int(input(f"Enter guess {turns + 1} of 5: "))

        if guess == answer:
            print(f"🐬✨Congrats, you did it!✨🌊 \nThank you for playing \nYour score is: {score}")
        else:
            divisor = abs(answer - guess)  # Calculate the score based on the distance
            quotient = LOSE_DIVIDEND / divisor
            exponent = 2  # Adjust the exponent as needed for the desired rate of increase
            score = int(quotient ** exponent)
            print(f"Game Over \nBetter luck next time! The number was:  {answer} \nYour final guess was {divisor} numbers off. Your score is: {score} \nThank you for playing")

    # If the while loop has ended, it means the user has had 3 incorrect guesses

# Start the game
main()