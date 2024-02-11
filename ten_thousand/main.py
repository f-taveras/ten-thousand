# main.py

from game import GamePlay
from game_logic import GameLogic

def play():
    game = GamePlay()
    print("Welcome to Ten Thousand")

    user_input = input("(y)es to play or (n)o to decline\n> ")
    if user_input.lower() != 'y':
        print("Maybe next time!")
        return

    # The rest of the game logic goes here
    # ...

if __name__ == "__main__":
    play()
