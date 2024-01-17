import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        counts = [dice_roll.count(number) for number in range(1, 7)]

        # Scoring rules
        if all(count >= 1 for count in counts):
            return 1500  # Straight from 1 to 6

        if counts == [2, 2, 2, 0, 0, 0] or counts == [0, 0, 0, 2, 2, 2]:
            return 1500  # Three pairs

        for (index, count) in enumerate(counts, start=1):
            if count >= 3:
                score += (index * 100) * (10 if index == 1 else 1) * (count - 2)

        if counts[0] < 3:  # Ones not part of a triplet
            score += counts[0] * 100

        if counts[4] < 3:  # Fives not part of a triplet
            score += counts[4] * 50

        return score

    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1, 6) for _ in range(num_dice))

# Example usage
# dice_roll = GameLogic.roll_dice(5)
# score = GameLogic.calculate_score(dice_roll)
