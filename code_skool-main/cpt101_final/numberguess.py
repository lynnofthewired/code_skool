# Lynn Makowski
# 

import random

def start_game():
    # Initialize the answer and the turn counter
    answer = random.randint(1, 100)
    turns = 0

    while turns < 4:
        # Prompt the user for their guess
        guess = int(input("Enter your guess: "))

        # Check if the guess is too high, too low, or correct
        if guess > answer:
            print("Your guess is too high.")
        elif guess < answer:
            print("Your guess is too low.")
        else:
            print("Congratulations! You've guessed the number correctly.")
            return  # End the game if the guess is correct

        # Increment the turn counter
        turns += 1

    # If the while loop has ended, it means the user has had 3 incorrect guesses
    print(f"The answer is:  {answer}")
    print("Game Over")

# Start the game
start_game()



# variables called guess_prev, and guess? guess_prev gets its value from guess, passing into guess_prev in the next round? and then we have code for if the user guesses too high or too low. Adn then we ahve code for 

# certain number of guesses, takes your final guess, subtracts it from the answer, returns sum as absolute value, OR before running the sum, we have a function that checks for negatives, if negative multiplies  by -1. THEN it performs the subtraction.

# but, let's say it works like answer minus(-) guess
# 
# answer = 50,
# you guess 53
# your total is -3
# 
# You and I are software engineers writing an integer guessing game in Python. We have to think about our code's readability for a team of other developers, as well as code with optimal runtime. Our code will run the random number generator you've already sent me earlier, which stores the random integer value in "answer". It will then prompt for user input and pass that input's value into a variable called "guess". The program then uses  "if" loop to tell the user if their guess is over or under the answer. We'll need a counter for turns. A turn begins when the user gets the prompt for the guess. A turn ends after the print from the if loop. At the end of 3 turns, print "Game Over"
# Now I need a way of keeping score. We're going to do this by taking the user's final response, and subtracting it from the answer. 
# ^^ this is the very most basic game. Extra features come after ^^
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
 










