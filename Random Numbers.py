import random

#low = 1
#high = 100
#options = ("rock", "paper", "scissors")
#cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#print(help(random))


#number = random.randint(low, high)
#option = random.choice(options)
#random.shuffle(cards)


#print(cards)



#low = 1
#high = 100
#guesses = 0
#number = random.randint(low, high)

#while True:
#    guess = int(input(f"Guess a number between {low} - {high}: "))
#    guesses += 1
#    if guess == number:
#        print(f"You guessed it in {guesses} guesses!")
#        break
#    elif guess < number:
#        print("Too low!")
#    elif guess > number:
#        print("Too high!")
#    else:
#        print("You guessed it in " + str(guesses) + " guesses!")

import random

options = ("rock", "paper", "scissors")

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, or scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("player wins!")
    elif player == "sciccors" and computer == "paper":
        print("player wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
    else:
        print("computer wins!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        running = False


print("Thanks for playing!")












