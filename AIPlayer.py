from board import Board
from piece import Piece
from rules import Rules
from board import Board
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD

class AIPlayer:
    def __init__(self):
        self.pieceColor = WHITE
        self.rules = Rules()
        
    def AITurn(self,b, piece): 
        moves=self.rules.possibleMoves(b,piece)
        boards=[]
        for move in moves:
            newb=Board()
            newb.initializePossibleBoard(b)
            row,col=move
            newb.move_piece(piece,row,col)
            boards.append(newb)
        return boards
        
        
    def minimax(self,currentBoard, moveDepth):  
        b=currentBoard
        maxEval = float('-inf')
        piece=None
        row=None
        column=None
        if moveDepth==0 and piece!=None: 
            return maxEval,piece, row, column
        boards={}
        for piece in b.getAllPieces(WHITE):
            boards[piece]=self.AITurn(b,piece)
        
        for x in boards.keys(): 
            for board in boards[x]: 
                nextMove=self.minimax(board, moveDepth-1)
                score=self.getScore(board)
                maxEval=max(score,maxEval)
                if maxEval==score: 
                    row=x.getPosition()[0]
                    column=x.getPosition()[1]
                    piece=x
        return maxEval, piece, row, column
        
                
               
    def getScore(self, board): #get minimax evaluation score based on board pieces
        score=board.white_pieces-board.red_pieces+ (board.white_kings * 0.5 - board.red_kings * 0.5)
        return score
                
    def randomMove(self, board):
        allMoves = self.rules.getAllMoves(board, WHITE)
        # print("ALL MOVESS, for all pieces: ", allMoves)

        for piece in allMoves:
            if allMoves[piece]:
                random_move = list(allMoves[piece].keys())[0]
                row, col = random_move[0], random_move[1]
                return piece, row, col

        return None
