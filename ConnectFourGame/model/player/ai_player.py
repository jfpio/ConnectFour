from ConnectFourGame.model.player.player import Player
from ConnectFourGame.model.ai.ai import Ai


class AiPlayer(Player):
    def __init__(self, token, search_depth):
        super().__init__(token)
        self.ai = Ai(search_depth, self.token)

    def get_move(self, board):
        return 0
