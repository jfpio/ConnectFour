from ConnectFourGame.view.view import View
from ConnectFourGame.view.input import Input
from ConnectFourGame.model.player.player_token import PlayerToken
from ConnectFourGame.model.game.game import Game

view = View()
view.display_welcome_screen()
gameInput = Input()

first_player = gameInput.get_player_type(PlayerToken.X)
second_player = gameInput.get_player_type(PlayerToken.O)
game = Game(gameInput.get_board_cols(), gameInput.get_board_rows())


current_player = first_player

while not game.is_end():
    view.display_current_turn_player(current_player.get_token())
    view.display_board(game.get_board())

    move = current_player.get_move(game.get_board())
    if not game.insert(move, current_player.get_token()):
        print("Wrong move")
        continue
    current_player = first_player if current_player == second_player else second_player

view.display_board(game.get_board())
view.display_winner(game.get_winner().value)
