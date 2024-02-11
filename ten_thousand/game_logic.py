# game_logic.py

import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        counts = [dice_roll.count(number) for number in range(1, 7)]

        if all(count == 1 for count in counts):
            return 1500
        if len([count for count in counts if count == 2]) == 3:
            return 1500
        if sorted(counts) == [0, 0, 0, 3, 3, 3]:
            return 1200

        for index, count in enumerate(counts, start=1):
            if count >= 3:
                score += (index * 100) * (10 if index == 1 else 1) * (count - 2)
            elif index == 1:
                score += count * 100
            elif index == 5:
                score += count * 50

        return score

    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1, 6) for _ in range(num_dice))

    @staticmethod
    def is_zilch(dice_roll):
        return GameLogic.calculate_score(dice_roll) == 0

    @staticmethod
    def get_scorers(dice_roll):
        scoring_dice = []
        counts = [dice_roll.count(number) for number in range(1, 7)]
        if counts[0] < 3:
            scoring_dice.extend([1] * counts[0])
        if counts[4] < 3:
            scoring_dice.extend([5] * counts[4])
        return tuple(scoring_dice)

    @staticmethod
    def validate_keepers(roll, keepers):
        roll_counts = {number: roll.count(number) for number in roll}
        keepers_counts = {number: keepers.count(number) for number in keepers}

        for keeper in keepers_counts:
            if keeper not in roll_counts or keepers_counts[keeper] > roll_counts[keeper]:
                return False
        return True
