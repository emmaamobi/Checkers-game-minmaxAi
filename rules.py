from board import Board
from piece import Piece
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD

class Rules:
    def __init__(self):
        pass

    def possibleMoves(self, board, piece):
        moves = {} #empty dictionary with potential moves as the call.
        left = piece.col - 1 #We need to change this match the appropriate data structure
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.isKing ==True:
            moves.update(self.moveLeft(board, row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self.moveRight(board, row-1, max(row-3,-1), -1, piece.color,right))
        if piece.color == WHITE or piece.isKing == True:
            moves.update(self.moveLeft(board, row+1, min(row+3, 8), 1, piece.color, left))
            moves.update(self.moveRight(board, row+1, min(row+3, 8), 1, piece.color, right))

        return moves
    
    def getAllMoves(self, board,color):
        moves={}
        allPieces=board.getAllPieces(color)
        # print("ALL PIECES: ", allPieces)
        for piece in allPieces: 
            move=self.possibleMoves(board,piece)
            moves[piece]=move
        return moves
        
        # Need to decide how to assign a value for Kings by color
    def moveRight(self, board, start, stop, step, color, right, skipped=[]):
        # print("START: ", start)
        # print("STOP: ", stop)
        # print("STEP: ", step)
        #Skipped is for a recursive call. Tells us if we've skipped squares.
        moves = {}
        last = []
        for rows in range(start, stop, step):
            if right >= 8:
                break

            current = board.get_piece(rows,right)
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(rows, right)] = last + skipped
                else:
                    moves[(rows, right)] = last

                if last:
                    if step == -1:
                        row = max(rows-3,-1)
                    else:
                        row = min(rows+3, 8)
                    moves.update(self.moveRight(board,row+step, row, step, color, right-1, skipped=last))
                    moves.update(self.moveLeft(board,row+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right+=1

        return moves


    def moveLeft(self,board, start, stop, step, color, left, skipped=[]):
        moves={}
        last = []
        for rows in range(start, stop, step):
            if left <0:
                break

            current = board.get_piece(rows,left)
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(rows, left)] = last + skipped
                else:
                    moves[(rows, left)] = last

                if last:
                    if step == -1:
                        row = max(rows-3, -1)
                    else:
                        row = min(rows+3, 8)
                    moves.update(self.moveLeft(board,rows+step, row, step, color, left-1, skipped=last))
                    moves.update(self.moveRight(board,rows+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -=1

        return moves

        #We might need to relocate the left anf right traversal/moves to other classes


    def winner(self,board):
        if board.red_pieces <= 0:
            return WHITE
        elif board.white_pieces <= 0:
            return RED

        return None
