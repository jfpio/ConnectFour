from ConnectFourGame.model.player.human_player import HumanPlayer
from ConnectFourGame.model.player.ai_player import AiPlayer
from ConnectFourGame.model.utils import get_input_from_range


class Input:
    def get_player_type(self, token):
        print("PlayerToken types: \n1. human\n2. ai")
        print(f"Choose {token} player type: ")
        current_input = get_input_from_range(1, 2)
        if current_input is 1:
            return HumanPlayer(token)
        else:
            return AiPlayer(token, self.get_search_depth())

    @staticmethod
    def get_search_depth():
        print("Choose search depth for AI: ")
        # TODO Check depth limit
        return get_input_from_range(1, 100)

    @staticmethod
    def get_board_rows():
        print("Choose get_board rows amount: ")
        return get_input_from_range(4, 100)

    @staticmethod
    def get_board_cols():
        print("Choose get_board columns amount: ")
        return get_input_from_range(4, 100)


