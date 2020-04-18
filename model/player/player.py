from model.player.player_type import PlayerType
from model.player.player_token import PlayerToken
from model.ai.ai import Ai


class Player:
    def __init__(self, type, token, name):
        self.type = type
        self.token = token
        self.name = name

    def get_type(self):
        return self.type

    def get_token(self):
        return self.token

    def get_name(self):
        return self.name

    def create_ai(self, search_depth):
        self.ai = Ai(search_depth, self.token)


