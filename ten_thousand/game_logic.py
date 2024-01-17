import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        # Initialize score to 0
        score = 0

        # Create a list that counts how many times each number appears in the dice roll
        counts = [dice_roll.count(number) for number in range(1, 7)]

        # Check for a straight (1, 2, 3, 4, 5, 6)
        if all(count == 1 for count in counts):
            return 1500  # Return 1500 points for a straight

        # Check for three pairs
        if len([count for count in counts if count == 2]) == 3:
            return 1500  # Return 1500 points for three pairs

        # Check for two sets of three of a kind (e.g., 1,1,1,2,2,2)
        if counts == [3, 3, 0, 0, 0, 0] or counts == [0, 0, 0, 3, 3, 3]:
            return 1200  # Return 1200 points for two triplets

        # Loop through each die value (1 through 6)
        for (index, count) in enumerate(counts, start=1):
            if count >= 3:  # Check if three or more of a kind
                # Score calculation for three or more of a kind
                score += (index * 100) * (10 if index == 1 else 1) * (count - 2)
            elif index == 1:  # Check for single ones (not part of a triplet or more)
                score += count * 100  # Add 100 points for each single one
            elif index == 5:  # Check for single fives (not part of a triplet or more)
                score += count * 50  # Add 50 points for each single five

        # Return the total score
        return score

    @staticmethod
    def roll_dice(num_dice):
        # Generate and return a tuple of random dice rolls
        return tuple(random.randint(1, 6) for _ in range(num_dice))

# # Example usage:
# dice_roll = GameLogic.roll_dice(5)  # Roll 5 dice
# score = GameLogic.calculate_score(dice_roll)  # Calculate the score of the roll
