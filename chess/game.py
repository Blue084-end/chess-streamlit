from .board import Board
from .pieces import Piece

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "red"

    def make_move(self, from_pos, to_pos):
        piece = self.board.get_piece(*from_pos)
        if piece and piece.color == self.turn:
            piece.move(to_pos)
            self.board.set_piece(*to_pos, piece)
            self.board.set_piece(*from_pos, None)
            self.switch_turn()

    def switch_turn(self):
        self.turn = "black" if self.turn == "red" else "red"

