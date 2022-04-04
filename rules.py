from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK,BLUE,GOLD

class Rules:
    #import board
    #import game logic
    #import piece
    def __init__(self, piece):
        self.possibleMoves = []
        self.king = True

    def possibleMoves(self, piece):
        moves = {}
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
    def moveRight(self, start, stop, color, step, right, skipped =[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= 8:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, 8)
                    moves.update(self.moveRight(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self.moveLeft(r+step, row, step, color, right+1, skipped =last))
                break
            elif current.color ==color:
                break
            else:
                last = [current]

            right+=1

        return moves


    def moveLeft(self, start, stop, step, color, left, skipped = []):
        moves={}
        last = []
        for r in range(start, stop, step):
            if left <0:
                break

            current = self.bord[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, 8)
                        moves.update(self.moveLeft(r+step, row, step, color, left-1, skipped = last))
                        moves.update(self.moveRight(r+step, row, step, color, left+1, skipped = last))
                    break
                elif current.color ==color:
                    break
                else:
                    last = [current]

                left -=1

            return moves

        #We might need to relocate the left anf right traversal/moves to other classes










