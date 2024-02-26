from game import GamePlay
from game_logic import GameLogic

def play():
    game = GamePlay()
    print("Welcome to Ten Thousand")

    valid_answers = ["y", "yes", "go", "sure", "okay", "ok"]

    user_input = input("(y)es to play or (n)o to decline\n> ")
    if user_input.lower() not in valid_answers:
        print("Maybe next time!")
        return

    round_number = 1
    while True:
        print(f"\nStarting round {round_number}")
        game.reset_round()
        while game.can_continue():
            print(f"Rolling {game.dice_in_play} dice...")
            roll = game.roll_dice()
            print(f"*** {' '.join(map(str, roll))} ***")

            valid_input = False
            while not valid_input:
                keepers_input = input("Enter dice to keep, or (q)uit:\n> ")
                if keepers_input.lower() == 'q':
                    print(f"Thanks for playing. You earned {game.get_total_score()} points")
                    return
                
                try:
                    keepers = tuple(map(int, keepers_input.split()))
                    if not GameLogic.validate_keepers(roll, keepers):
                        print("Cheater!!! Or possibly made a typo...")
                        print(f"*** {' '.join(map(str, roll))} ***")
                        continue
                    valid_input = True
                except ValueError:
                    print("Invalid input. Please enter the dice as numbers separated by spaces or 'q' to quit.")
                    continue

            game.set_aside_dice(keepers)
            print(f"You have {game.current_score} unbanked points and {game.dice_in_play} dice remaining")
            next_action = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
            if next_action == 'b':
                game.bank_score()
                print(f"Total score is now {game.get_total_score()}.")
                break
            elif next_action == 'q':
                print(f"Thanks for playing. You earned {game.get_total_score()} points")
                return
            # No need for an explicit 'roll again' action as it's the default behavior

        if game.get_total_score() >= 10000:
            print("Congratulations! You've reached 10,000 points!")
            break

        round_number += 1
        user_input = input("Play another round? (y/n): ")
        if user_input.lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play()
