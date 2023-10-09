import random

# generate a random number between 1 and 10
number = random.randint(1, 10)

# set the number of guesses to 0
guesses = 0

print("I'm thinking of a number between 1 and 10. Can you guess what it is?")

# loop until the player guesses the correct number
while True:
    # get the player's guess
    guess = int(input("Enter your guess: "))

    # increment the number of guesses
    guesses += 1

    # check if the guess is correct
    if guess == number:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break
    elif guess < number:
        print("Your guess is low.\n Try again.")
    else:
        print('Your guess is hight.\n Try again.')
