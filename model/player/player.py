from model.player.player_type import PlayerType
from model.player.player_token import PlayerToken
from model.ai.ai import Ai


class Player:
    def __init__(self, type, token, id):
        self.type = type
        self.token = token
        self.id = id

    def get_type(self):
        return self.type.value

    def get_token(self):
        return self.token.value

    def get_id(self):
        return self.id

    def create_ai(self, search_depth):
        self.ai = Ai(search_depth, self.token)


