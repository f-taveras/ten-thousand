# game.py

from game_logic import GameLogic

class GamePlay:
    def __init__(self):
        self.total_score = 0
        self.current_score = 0
        self.dice_in_play = 6

    def roll_dice(self):
        return GameLogic.roll_dice(self.dice_in_play)
    
    def set_aside_dice(self, dice_to_set_aside):
        score = GameLogic.calculate_score(dice_to_set_aside)
        self.current_score += score
        self.dice_in_play -= len(dice_to_set_aside)

    def bank_score(self):
        self.total_score += self.current_score
        self.current_score = 0
        self.reset_round()

    def get_total_score(self):
        return self.total_score

    def reset_round(self, keep_score=False):
        self.dice_in_play = 6
        if not keep_score:
            self.current_score = 0

    def can_continue(self):
        return self.dice_in_play > 0
