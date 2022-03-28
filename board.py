class Board: 
    """
    Standard Checkers board, 8 x 8 grid, red vs white pieces. 
    """

    def __init__(self):
        self.board = []
        self.rows = 8
        self.cols = 8
        self.initializeBoard()

    def initializeBoard(self):
        square = 1 # white

        for row in range(self.rows):
            self.board.append([])
            for col in range(self.cols):
                self.board[row].append(square)
                if col == self.cols-1:
                    continue
                square = 0 if square == 1 else 1
    def get_board(self):
        return self.board



