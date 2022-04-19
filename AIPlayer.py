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
        
def minimax(self,currentBoard, currentGame, moveDepth):
        maxEval = float('-inf')
        minEval=float('inf')
        piece=None
        row=None
        column=None
        bestMove=None
        for move in Rules.getAllMoves(currentBoard, WHITE):
            if moveDepth==0: 
                return move
            nextMove=self.minimax(currentBoard, currentGame,moveDepth-1)
            maxEval=max(nextMove,maxEval)
            if maxEval==nextMove: 
                bestMove=nextMove
                
        return piece, row, column

    def randomMove(self, board):
        allMoves = self.rules.getAllMoves(board, WHITE)
        # print("ALL MOVESS, for all pieces: ", allMoves)

        for piece in allMoves:
            if allMoves[piece]:
                random_move = list(allMoves[piece].keys())[0]
                row, col = random_move[0], random_move[1]
                return piece, row, col

        return None
