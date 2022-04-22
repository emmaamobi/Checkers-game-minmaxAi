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
        
    def AITurn(self,b,row,col): #used to simulate future turns for game lookahead
        piece=b.board[row][col]
        moves=self.rules.possibleMoves(b,piece) #get possible moves for current board
        boards=[] #initialize list that will hold boards
        for move,skipped in moves.items(): #go through all possible moves to be made
            newb=deepcopy(b)
            pieceCopy=newb.board[row][col]
            newrow,newcol=move #unpack the current move
            oldrow,oldcol=pieceCopy.getPosition()
            newb.move_piece(pieceCopy,newrow,newcol) #move wanted piece to possible position on board copy
            if skipped:
                newb.remove(skipped)
            boards.append([newb,oldrow,oldcol,newrow,newcol]) #add new board to the board list
        return boards
        
        
    def minimax(self,currentBoard, oldrow,oldcol,newrow,newcol,moveDepth, currentPlayer):
        maxEval = float('-inf') #White piece maximization
        minEval=float('inf') #same, but for red pieces
        score=self.getScore(currentBoard) #gets the score of the current board
        if moveDepth==0: #base case
            return score ,oldrow,oldcol,newrow, newcol
        boards=[] #holds all of possible boards
        if(currentPlayer==WHITE): #if on the ai
            for pieceObj in currentBoard.getAllPieces(WHITE): #get all pieces for white player
                row,col=pieceObj.getPosition()
                boardList=self.AITurn(currentBoard,row,col) #get a list of all possible boards for that piece move
                for x in boardList: 
                    boards.append(x) #add the board and the piece thats moved 
            
            for x in boards:  #iterate thru all possible boards
                if x!=None: 
                    nextMove=self.minimax(x[0], x[1],x[2],x[3],x[4],moveDepth-1,RED) #calling minmax again
                    nextMoveScore=nextMove[0]
                    maxEval=max(nextMoveScore,maxEval)
                    if maxEval==nextMoveScore: 
                        oldrow=nextMove[1]
                        oldcol=nextMove[2]
                        newrow=nextMove[3]
                        newcol=nextMove[4]
            return maxEval, oldrow,oldcol,newrow,newcol
        else: 
            for pieceObj in currentBoard.getAllPieces(RED):
                boardList=self.AITurn(currentBoard,pieceObj) #get a list of all possible boards for that piece move
                for x in boardList: 
                    boards.append([x,pieceObj]) #add the board and the piece thats moved 
            
            for x in boards: 
                if x!=None:
                    nextMove=self.minimax(x[0], x[1],x[2],x[3],x[4],moveDepth-1,WHITE) #calling minmax again
                    nextMoveScore=nextMove[0]
                    minEval=min(nextMoveScore,maxEval)
                    if maxEval==nextMoveScore: 
                        oldrow=nextMove[1]
                        oldcol=nextMove[2]
                        newrow=nextMove[3]
                        newcol=nextMove[4]
            return minEval, oldrow,oldcol,newrow,newcol
                
               
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
