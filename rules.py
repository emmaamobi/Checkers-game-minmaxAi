class Rules:
    #import board
    #import game logic
    #import piece
    def __init__(self, piece):
        self.possibleMoves = []
        self.king = True
    def possibleMoves(self, piece):
        moves = {}
        left = self.col + 1 #We need to change this match the appropriate data structure
        right = self.col + 1
        row = piece.row

        if piece.color == RED or piece.isKing ==True:
            moves left - 1 max -3
            moves right - 1 max -3
        if piece.color == BLACK or piece.isKing == True:
            moves left + 1 max + 3
            moves right + 1 max + 3
        # Need to decide how to assign a value for Kings by color







