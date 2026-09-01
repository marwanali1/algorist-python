from types import Enum

from board import Board, DiscColor
from player import Player

"""
Build the object-oriented design for a two-player Connect Four game.
Players take turns dropping discs into a 7-column, 6-row board. The
first to align four of their own discs vertically, horizontally, or 
diagonally wins.
"""

"""
Core Entities:
- Game
- Board
- Player
"""


class GameState(Enum):
    WON = "WON"
    DRAW = "DRAW"
    IN_PROGRESS = "IN_PROGRESS"


class Game:
    def __init__(self):
        self._board: Board = Board()
        self._player_one: Player = Player(name="one", color=DiscColor.RED)
        self._player_two: Player = Player(name="two", color=DiscColor.YELLOW)

        self._game_state: GameState = GameState.IN_PROGRESS
        self._current_player: Player = None
        self._winner: Player = None

    @property
    def get_current_player(self) -> Player:
        return self._current_player

    @property
    def get_game_state(self) -> GameState:
        return self._game_state

    @property
    def get_winner(self) -> Player | None:
        return self._winner

    def make_move(self, player: Player, col: int) -> bool:
        if (
            (self._game_state != GameState.IN_PROGRESS)
            or (self._current_player != player)
            or (not self._board.can_place(col))
        ):
            return False

        row = self._board.place_disc(col, self._current_player.color)
        if row == -1:
            return False

        if self._board.check_win(row, col, player.color):
            self._game_state = GameState.WON
            self._winner = self._current_player
        elif self._board.is_full:
            self._game_state = GameState.DRAW
        else:
            self._current_player = (
                self._player_one
                if self._current_player == self._player_two
                else self._player_two
            )

        return True
