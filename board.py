import pygame
from ui_consts import EACH_SQUARE, W,H,RED,WHITE,BLACK
from piece import Piece
class Board: 
    """
    Standard Checkers board, 8 x 8 grid, red vs white pieces. 
    """

    def __init__(self):
        self.board = []
        self.rows = 8
        self.cols = 8
        self.initializeBoard()

        # pygame UI variables

        

    def initializeBoard(self):

        for row in range(self.rows):
            self.board.append([])
            for col in range(self.cols):
                if col % 2 == ((row + 1) % 2): # draw only on black squares
                    if row < 3:# white on first 3 rows
                        white_piece = Piece(WHITE,row,col)
                        self.board[row].append(white_piece)

                    elif row > 4: #red on bottom 3 rows
                        red_piece = Piece(WHITE,row,col)
                        self.board[row].append(red_piece)

                    else: # fill empty playable slots with 0
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    def get_board(self):
        return self.board

    def draw_board(self,win):
        win.fill(BLACK)
        for row in range(self.rows):
            x_cord = row*EACH_SQUARE
            width, height = EACH_SQUARE, EACH_SQUARE
            for col in range(row % 2, self.rows, 2):
                y_cord = col*EACH_SQUARE
                mini_square = (x_cord, y_cord, width, height)
                pygame.draw.rect(win, WHITE, mini_square)

    
    def draw_pieces(self, win): 
        # TODO: draw the pieces
        return 0





