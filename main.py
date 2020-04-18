from .game import Game
from .input import get_number_of_rows_and_columns_from_user
from .player_tokens import Player

game = Game(get_number_of_rows_and_columns_from_user())
player1_move = choose_player()
player2_move = choose_player()

while game.if_sb_win_or_game_end():
    game.print_board()
    game.insert(player1_move, Player.X)
    if game.if_sb_win_or_game_end():
        break
    game.print_board()
    game.insert(player2_move, Player.O)

game.print_board()
game.print_winner_and_game_statistics()