from .pieces import Piece

class Board:
    def __init__(self):
        self.grid = self.create_board()
        self.setup_pieces()

    def create_board(self):
        # Tạo bàn cờ 9x10 với None ở mỗi ô
        return [[None for _ in range(9)] for _ in range(10)]

    def get_piece(self, row, col):
        return self.grid[row][col]

    def set_piece(self, row, col, piece):
        self.grid[row][col] = piece

    def setup_pieces(self):
        # Đặt thử vài quân cờ để kiểm tra hiển thị
        self.set_piece(0, 0, Piece("Xe", "black", (0, 0)))
        self.set_piece(0, 8, Piece("Xe", "black", (0, 8)))
        self.set_piece(9, 0, Piece("Xe", "red", (9, 0)))
        self.set_piece(9, 8, Piece("Xe", "red", (9, 8)))
        self.set_piece(0, 4, Piece("Tướng", "black", (0, 4)))
        self.set_piece(9, 4, Piece("Tướng", "red", (9, 4)))
