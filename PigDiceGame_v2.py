# Using a seperate module to control the main function and calling game logic from other modules.
## Important things to remember is how to import different methods and functions from other modules
## this will help when creating my own games with Pygame. 
from Game import Game

def display_welcome():
    print("Let's Play PIG!")
    print()
    print("* See how many turns it takes you to get to 20.")
    print("* Turn ends when you hold or roll a 1.")
    print("* If you roll a 1, you lose all points for the turn.")
    print("* If you hold, you save all points for the turn.")
    print()

def main():
    display_welcome()
    choice = "y"
    while choice.lower() == "y":
        game = Game()
        game.play()

        choice = input("Play again? (y/n): ")
        print()
    print("Goodbye!")

if __name__ == "__main__":
    main()