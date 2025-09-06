class Board:
    def __init__(self):
        self.grid = self.create_board()

    def create_board(self):
        # Tạo bàn cờ 9x10 với None ở mỗi ô
        return [[None for _ in range(9)] for _ in range(10)]

    def get_piece(self, row, col):
        return self.grid[row][col]

    def set_piece(self, row, col, piece):
        self.grid[row][col] = piece

