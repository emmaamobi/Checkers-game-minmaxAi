from board import Board
from piece import Piece
from rules import Rules
from board import Board
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD

class AIPlayer:
    def __init__(self):
        self.pieceColor = WHITE
        self.rules = Rules()
        
    def AITurn(self,b, piece): #used to simulate future turns for game lookahead
        moves=self.rules.possibleMoves(b,piece) #get possible moves for current board
        boards=[] #initialize list that will hold boards
        for move in moves: #go through all possible moves to be made
            newb=Board() #initialize new board as to not write over current game board
            newb.initializePossibleBoard(b) #update new board to be the same as current board
            row,col=move #unpack the current move
            newb.move_piece(piece,row,col) #move wanted piece to possible position on board copy
            boards.append(newb) #add new board to the board list
        return boards
        
        
    def minimax(self,piece,currentBoard, moveDepth, currentPlayer):
        maxEval = float('-inf')
        minEval=float('inf')
        row=None
        column=None
        score=self.getScore(currentBoard) #gets the score of the current board
        if moveDepth==0: #base case
            row=piece.getPosition()[0] #get position of given piece
            column=piece.getPosition()[1]
            return score ,piece, row, column
        boards=[]
        if(currentPlayer==WHITE):
            for pieceObj in currentBoard.getAllPieces(WHITE):
                boardList=self.AITurn(currentBoard,pieceObj)
                for x in boardList: 
                    boards.append([x,pieceObj])
            
            for x in boards: 
                if x!=None:
                    nextMove=self.minimax(x[1],x[0], moveDepth-1,RED)[0]
                    maxEval=max(nextMove,maxEval)
                    if maxEval==score: 
                        row=x[1].getPosition()[0]
                        column=x[1].getPosition()[1]
                        piece=x[1]
            return maxEval, piece, row, column
        else: 
            for pieceObj in currentBoard.getAllPieces(RED):
                boards.append([self.AITurn(currentBoard,pieceObj),pieceObj])
            
            for x in boards: 
                if x!=None:
                    nextMove=self.minimax(x[0],x[1], moveDepth-1,WHITE)[0]
                    maxEval=max(nextMove,maxEval)
                    if maxEval==score: 
                        row=x[1].getPosition()[0]
                        column=x[1].getPosition()[1]
                        piece=x[1]
            return minEval, piece, row, column
                
               
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
