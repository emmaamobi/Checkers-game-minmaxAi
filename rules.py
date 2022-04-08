import board
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD

class Rules:
    #import board
    #import game logic
    #import piece
    def __init__(self, piece):
        self.possibleMoves = []
        self.king = True

    def possibleMoves(self, piece):
        moves = {} #empty dictionary with potential moves as the call.
        left = self.col - 1 #We need to change this match the appropriate data structure
        right = self.col + 1
        row = piece.row

        if piece.color == RED or piece.isKing ==True:
            moves.update(self.moveLeft(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self.moveRight(row-1, max(row-3,-1), -1, piece.color,right))
        if piece.color == WHITE or piece.isKing == True:
            moves.update(self.moveLeft(row+1, min(row+3, 8), 1, piece.color, left))
            moves.update(self.moveRight(row+1, min(row+3, 8), 1, piece.color, right))

        return moves
        # Need to decide how to assign a value for Kings by color
    def moveRight(self, start, stop, color, step, right, skipped=[]):
        #Skipped is for a recursive call. Tells us if we've skipped squares.
        moves = {}
        last = []
        for rows in range(start, stop, step):
            if right >= 8:
                break

            current = self.board[rows][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(rows, right)] = last + skipped
                else:
                    moves[(rows, right)] = last

                if last:
                    if step == -1:
                        row = max(rows-3,0)
                    else:
                        row = min(rows+3, 8)
                    moves.update(self.moveRight(row+step, row, step, color, right-1, skipped=last))
                    moves.update(self.moveLeft(row+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right+=1

        return moves


    def moveLeft(self, start, stop, step, color, left, skipped=[]):
        moves={}
        last = []
        for rows in range(start, stop, step):
            if left <0:
                break

            current = self.board[rows][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(rows, left)] = last + skipped
                else:
                    moves[(rows, left)] = last

                if last:
                    if step == -1:
                        row = max(rows-3, 0)
                    else:
                        row = min(rows+3, 8)
                    moves.update(self.moveLeft(rows+step, row, step, color, left-1, skipped=last))
                    moves.update(self.moveRight(rows+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -=1

        return moves

        #We might need to relocate the left anf right traversal/moves to other classes

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece.color == RED:
                self.board.red_left -= 1
            else:
                self.board.white_left -= 1

    def winner(self):
        if board.red_pieces <= 0 and board.red_kings <=0:
            return WHITE
        elif board.white_pieces <= 0 and board.white_kings <=0:
            return RED

        return None










