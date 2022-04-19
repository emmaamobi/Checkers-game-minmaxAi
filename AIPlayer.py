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
        
    def AITurn(self,board, piece):
        moves=self.rules.possibleMoves(board,piece)
        boards=[]
        for move in moves: 
            row,col=move
            board.move_piece(piece,row,col)
            boards.append(board)
        return boards
        
        
    def minimax(self,currentBoard, moveDepth):  
        board=currentBoard
        maxEval = float('-inf')
        piece=None
        row=None
        column=None
        bestMove=None
        
        if moveDepth==0: 
            return maxEval,piece, row, column
        boards={}
        for piece in board.getAllPieces(WHITE):
            boards[piece]=self.AITurn(board,piece)
        
        for board in boards: 
            nextMove=self.minimax(board, moveDepth-1)
            score=self.getScore(board)
            maxEval=max(nextMove[0],maxEval)
            if maxEval==nextMove: 
                bestMove=nextMove
            return score, piece, row, column
                
               
    def getScore(self, board):
        score=board.white_pieces-board.red_pieces+ (board.white_kings * 0.5 - board.red_kings * 0.5)
                
    def randomMove(self, board):
        allMoves = self.rules.getAllMoves(board, WHITE)
        # print("ALL MOVESS, for all pieces: ", allMoves)

        for piece in allMoves:
            if allMoves[piece]:
                random_move = list(allMoves[piece].keys())[0]
                row, col = random_move[0], random_move[1]
                return piece, row, col

        return None
