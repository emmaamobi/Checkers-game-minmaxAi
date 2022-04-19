from board import Board
from piece import Piece
from rules import Rules
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD

class AIPlayer:
    def __init__(self):
        self.pieceColor = WHITE
        self.rules = Rules()
        
    def bestPiece():
        return 0
        
    def AITurn(self,game):
        row=5
        col=5
        piece=self.bestPiece()
        game.makeMove()
        
    def minimax(self,currentBoard, pieceDepth, currentGame):
        maxEval = float('-inf')
        best_move = None
        for move in Rules.getAllMoves(currentBoard, WHITE):
            evaluation = self.minimax(move, pieceDepth-1, False, g=currentGame)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
    def randomMove(self, board):
        allMoves = self.rules.getAllMoves(board, WHITE)
        # print("ALL MOVESS, for all pieces: ", allMoves)

        for piece in allMoves:
            if allMoves[piece]:
                random_move = list(allMoves[piece].keys())[0]
                row, col = random_move[0], random_move[1]
                return piece, row, col
