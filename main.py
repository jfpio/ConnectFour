from model.game.game import Game
from view.view import View
from model.player.player import Player
from model.player.player_token import PlayerToken
from model.player.player_type import PlayerType
from model.player.player_id import PlayerId

view = View()
view.display_welcome_screen()

first_player = Player(view.get_player_type("first"), PlayerToken.O, PlayerId.FIRST_PLAYER)
if first_player.type == PlayerType.AI:
    first_player.create_ai(view.get_search_depth())

second_player = Player(view.get_player_type("second"), PlayerToken.X, PlayerId.SECOND_PLAYER)
if second_player.type == PlayerType.AI:
    second_player.create_ai(view.get_search_depth())

game = Game(view.get_board_cols(), view.get_board_rows())

current_player = first_player

while 1:
    view.display_current_turn_player(current_player.get_id().value)
    view.display_board(game.get_board())

    if current_player.type == PlayerType.HUMAN:
        move = view.get_human_move(game.get_cols_amount() - 1)
        game.insert(move, current_player)

    if current_player.type == PlayerType.AI:
        move = current_player.ai.move(game.get_board())
        game.insert(move, current_player)

    if game.is_end():
        break

    current_player = first_player if current_player == second_player else second_player

view.display_winner(game.get_winner().value)
view.display_board(game.get_board())

