from ConnectFourGame.model.player.player import Player
from ConnectFourGame.model.ai.alpha_beta import get_move_with_alpha_beta_pruning


class AiPlayer(Player):
    def __init__(self, token, search_depth):
        super().__init__(token)
        self.search_depth = search_depth

    def get_move(self, board):
        return get_move_with_alpha_beta_pruning(board, self.search_depth, self.get_token())
