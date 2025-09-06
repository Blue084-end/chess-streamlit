class Piece:
    def __init__(self, name, color, position):
        self.name = name  # Ví dụ: "Xe", "Mã"
        self.color = color  # "red" hoặc "black"
        self.position = position  # (row, col)

    def move(self, new_position):
        self.position = new_position

