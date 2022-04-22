from board import Board
from piece import Piece
from rules import Rules
from board import Board
from copy import deepcopy
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD

class AIPlayer:
    def __init__(self):
        self.pieceColor = WHITE
        self.rules = Rules()
        
    def AITurn(self,b, piece): #used to simulate future turns for game lookahead
        pieceCopy=deepcopy(piece)
        moves=self.rules.possibleMoves(b,pieceCopy) #get possible moves for current board
        boards=[] #initialize list that will hold boards
        for move in moves: #go through all possible moves to be made
            newb=deepcopy(b)
            row,col=move #unpack the current move
            print("Current position: ")
            print(pieceCopy.getPosition())
            print("Proposed Position")
            print(move)
            newb.move_piece(piece,row,col) #move wanted piece to possible position on board copy
            boards.append(newb) #add new board to the board list
        return boards
        
        
    def minimax(self,piece,currentBoard, moveDepth, currentPlayer):
        maxEval = float('-inf') #White piece maximization
        minEval=float('inf') #same, but for red pieces
        row=None #holds the row of the ideal piece
        column=None #holds the column of the ideal piece
        score=self.getScore(currentBoard) #gets the score of the current board
        idealBoard=None
        if moveDepth==0: #base case
            row=piece.getPosition()[0] #get row of given piece
            column=piece.getPosition()[1] #get column of given piece
            return score ,piece, row, column
        boards=[] #holds all of possible boards
        if(currentPlayer==WHITE): #if on the ai
            for pieceObj in currentBoard.getAllPieces(WHITE): #get all pieces for white player
                boardList=self.AITurn(currentBoard,pieceObj) #get a list of all possible boards for that piece move
                for x in boardList: 
                    boards.append([x,pieceObj]) #add the board and the piece thats moved 
            
            for x in boards:  #iterate thru all possible boards
                if x!=None: 
                    nextMove=self.minimax(x[1],x[0], moveDepth-1,RED)[0] #calling minmax again
                    maxEval=max(nextMove,maxEval)
                    if maxEval==nextMove: 
                        row=x[1].getPosition()[0]
                        column=x[1].getPosition()[1]
                        piece=x[1]
                        idealBoard=x[0]
            return maxEval, piece, row, column, idealBoard
        else: 
            for pieceObj in currentBoard.getAllPieces(RED):
                boardList=self.AITurn(currentBoard,pieceObj) #get a list of all possible boards for that piece move
                for x in boardList: 
                    boards.append([x,pieceObj]) #add the board and the piece thats moved 
            
            for x in boards: 
                if x!=None:
                    nextMove=self.minimax(x[1],x[0], moveDepth-1,WHITE)[0]
                    minEval=max(nextMove,minEval)
                    if minEval==nextMove: 
                        row=x[1].getPosition()[0]
                        column=x[1].getPosition()[1]
                        piece=x[1]
                        idealBoard=x[0]
            return minEval, piece, row, column, idealBoard
                
               
    def getScore(self, board): #get minimax evaluation score based on board pieces
        score=board.white_pieces-board.red_pieces+ (board.white_kings * 0.5 - board.red_kings * 0.5)
        return score
                
    def randomMove(self, board):
        allMoves = self.rules.getAllMoves(board, WHITE)
        # print("ALL MOVES, for all pieces: ", allMoves)

        for piece in allMoves:
            if allMoves[piece]:
                random_move = list(allMoves[piece].keys())[0]
                row, col = random_move[0], random_move[1]
                return piece, row, col

        return None
